#!/usr/bin/env python3
"""Build Zotero Run-JavaScript code for conservative metadata enrichment."""

import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
records = json.load(open(root / "data/sep-freewill/metadata-refresh.json"))
updates = []
for record in records:
    chosen = record.get("chosen_abstract") or {}
    abstract = chosen.get("text", "")
    doi = record.get("doi", "")
    if not abstract and not doi:
        continue
    updates.append(
        {
            "key": record["zotero_key"],
            "abstract": abstract,
            "abstractSource": chosen.get("source", ""),
            "doi": doi,
        }
    )

payload = json.dumps(updates, ensure_ascii=False)
script = f"""const updates = {payload};
const libraryID = Zotero.Libraries.userLibraryID;
let changed = 0;
let abstracts = 0;
let dois = 0;
let missing = [];
for (const update of updates) {{
    const item = Zotero.Items.getByLibraryAndKey(libraryID, update.key);
    if (!item) {{ missing.push(update.key); continue; }}
    let dirty = false;
    if (update.abstract && !item.getField('abstractNote')) {{
        item.setField('abstractNote', update.abstract);
        abstracts++;
        dirty = true;
    }}
    if (update.doi && !item.getField('DOI') && Zotero.ItemFields.isValidForType('DOI', item.itemTypeID)) {{
        item.setField('DOI', update.doi);
        dois++;
        dirty = true;
    }}
    if (update.abstractSource) {{
        const oldExtra = item.getField('extra') || '';
        if (!oldExtra.includes('Abstract source:')) {{
            item.setField('extra', (oldExtra ? oldExtra + '\\n' : '') + 'Abstract source: ' + update.abstractSource);
            dirty = true;
        }}
    }}
    if (dirty) {{ await item.saveTx(); changed++; }}
}}
return JSON.stringify({{changed, abstracts, dois, missing}});
"""
(root / "tmp/zotero-sep-refresh.js").write_text(script)
print(json.dumps({"updates": len(updates), "with_abstract": sum(bool(x["abstract"]) for x in updates), "output": str(root / "tmp/zotero-sep-refresh.js")}, ensure_ascii=False))
