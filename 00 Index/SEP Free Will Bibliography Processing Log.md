---
type: index
status: active
created: 2026-08-22
source: https://plato.stanford.edu/entries/freewill/#Bib
---

# SEP Free Will Bibliography Processing Log

<!-- concept-provenance-note:start -->
> [!info]- 概念の来歴
> **ノートの性格**：索引・進捗管理ノート。掲載順やリンクは知的来歴を示さない。
> **分析哲学の標準概念**：[[Alternative Possibilities]]。
> **隣接分野・文献由来**：該当なし。
> **本研究による再構成**：該当なし。
> **本研究で導入した作業概念**：該当なし。
> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。
> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。
> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
<!-- concept-provenance-note:end -->

## Scope

Stanford Encyclopedia of Philosophyの「Free Will」Bibliographyに掲載された298件を処理した。

## Zotero Registration

- SEP Bibliography抽出件数: 298
- 処理開始時にZoteroに存在した件数: 3
- 新規登録件数: 295
- Zoteroとの照合完了件数: 298
- 未登録件数: 0

各項目にはSEPの原引用をnoteとして保持し、書誌情報が不足する場合でも出典を追跡できるようにした。

## PDF Discovery

OpenAlexとCrossrefを用いて、DOI、公開URL、open-access locationを探索した。

- 公開PDF候補として検出した文献: 40
- PDFとして検証し、ダウンロードとZotero添付を完了した文献: 5
- 候補URLが購読認証、配信元の403、text-and-data-mining token要求、または非PDF応答のため取得できなかった文献: 35

取得制限の回避や非正規な配布元からの取得は行っていない。

「候補なし」はPDFが世界のどこにも存在しないことを意味せず、今回照会した公開書誌APIから検証可能な公開PDFを発見できなかったことを意味する。

## PDFs Read and Registered in Obsidian

- [[elzeinFrankfurtStyleCounterexamplesImportance2017]]
- [[franklinFarewellLuckMind2011]]
- [[franklinNeoFrankfurtiansBufferCases2011]]
- [[hofmannExplainingFreeWill2022]]
- [[moyaVeryIdeaRobust2011]]

## Complete Literature Import

PDFを取得できなかった文献と、PDFを取得しても本文処理の対象外だった文献についても、Zoteroのメタデータから`04 Literature`へ取り込んだ。

- SEP BibliographyのLiterature Note総数: 298
- 今回新規作成した空分析ノート: 290
- 既存ノートとして保持した文献: 8
- 今回作成したノートのうちZoteroにAbstractが存在した文献: 0

新規ノートは`Core Idea`、`Key Claims`、`Relevance to My Theory`、`My Evaluation`、関連項目、質問、Notesをすべて空欄のままにした。

既存8件は、ユーザーが作成した内容または先行処理で精読済みの内容を保護するため上書きしていない。

## Metadata and PDF Refresh

2026-08-22に、タイトル完全一致検索、Crossref、出版社ページ、公開リポジトリを使って全298件を再調査した。

- DOIを確定できた文献: 221
- Abstractを取得できた文献: 70
- 空欄だったObsidian Abstractへ反映した文献: 64
- 既存Abstractを保護した文献: 6
- PDF候補を検出した文献: 44
- PDF実体とページ構造を検証できた文献: 6
- 既取得PDFとの重複: 5
- 新規取得・Zotero登録したPDF: 1

新規PDFは[[toddNewApproachManipulation2010]]である。

Zoteroのローカル読取APIは既存項目の更新を提供しないため、Abstract付き70件とDOIのみ151件を`SEP Metadata Refresh`タグ付きの補完レコードとして登録した。

補完レコードのNoteには元のZotero item keyとAbstract取得元を保存している。

元項目との統合はZoteroの「重複アイテム」機能で行えるが、既存データを誤って失わないよう今回の自動処理ではマージしていない。

## Concepts and Arguments Updated

- [[Alternative Possibilities]]
- [[Frankfurt Cases Do Not Establish the Irrelevance of Alternatives]]

## Data Artifacts

- `data/sep-freewill/bibliography.json`: SEPの全298件とZotero照合結果
- `data/sep-freewill/openalex.json`: OpenAlex照会結果
- `data/sep-freewill/crossref-sequential.json`: Crossref照会結果
- `data/sep-freewill/downloads-sequential.json`: PDF候補の取得結果
- `data/sep-freewill/literature-import-report.json`: Literature Note作成件数とcitekey一覧
- `data/sep-freewill/metadata-refresh.json`: 全298件の再検索結果、DOI、Abstract候補、出典URL、PDF候補
- `data/sep-freewill/pdf-refresh-downloads.json`: PDF候補の取得・検証結果
- `data/sep-freewill/abstract-enrichment.ris`: Abstract付き補完レコード70件
- `data/sep-freewill/doi-enrichment.ris`: DOIのみの補完レコード151件
