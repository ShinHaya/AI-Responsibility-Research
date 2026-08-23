# Codex Working Notes

## Obsidian Access

- The Obsidian Local REST API with MCP endpoint is `https://127.0.0.1:27124/mcp/`.
- Codex is configured with an `obsidian` MCP server using `OBSIDIAN_API_KEY`.
- If the active Codex session does not expose the Obsidian MCP tools directly, use the local vault files when the working directory is the vault, or use the MCP HTTP endpoint when the API key is available in the shell.

## Zotero Literature Workflow

1. Register the paper in Zotero first. Prefer the Zotero local API/helper workflow so the Zotero item key and Better BibTeX citation key are known.
2. Do not use Obsidian's interactive `Zotero Integration: Literature Note` command from Codex. It depends on the Zotero picker and macOS UI automation, which is not reliable enough for repeatable Codex work.
3. Use the direct API-based route:
   - Read the Zotero item from `http://127.0.0.1:23119/api/users/0/items/<ZOTERO_ITEM_KEY>`.
   - When Better BibTeX fields are needed, export metadata by citation key through `http://127.0.0.1:23119/better-bibtex/json-rpc`.
   - Generate `04 Literature/{{citekey}}.md` in the structure of `99 Templates/Zotero Literature Note.md`.
   - Include the bibliographic fields and abstract from Zotero.
   - Fill `## Core Thesis` and later sections with substantive analysis.
4. For existing literature notes, preserve the frontmatter, `## Bibliographic Information`, and `## Abstract` sections unless they are clearly wrong. Codex should normally edit from `## Core Thesis` onward.
5. Keep Zotero item keys and citation keys distinct. Zotero item keys look like `682F9958`; Better BibTeX citation keys look like `martelaArtificialIntelligenceFree2025`.

## Conversation Processing Workflow

- Track progress in `00 Index/Conversation Processing Log.md`.
- Current processed offset: `1114588` of `1114588` chars for `01 Conversations/2026-08-12-AIへの自由意志と責任の帰属可能性.md` (complete; re-export offsets reindexed on 2026-08-23).
- Process the conversation in semantic chunks, usually around 5000-12000 chars, ending at a message or section boundary when possible.
- Extract only points that are not already knowledgeized into `02 Concepts`, `03 Arguments`, and `04 Literature`.
- When a later chunk deepens an existing note, update that note instead of creating a shallow duplicate.
- Use the depth and cross-linking style of:
  - `04 Literature/riserFreeWillSkill2015.md`
  - `04 Literature/arbelHowCountAIs2026.md`
  - `03 Arguments/Free Will Is a Higher-Order Acquired Agency Competence.md`
  - `03 Arguments/Second-Order Volition Requires Open-Ended Revisability.md`
