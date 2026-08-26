---
type: concept
status: developing
created: 2026-08-22
tags: [personal-data, data-sovereignty, physical-ai, elsi]
concept_origin: project-working-concept
origin_field: "本研究のデータ設計・循環型marketplace構想"
canonical_sources:
  - "[[2026-08-12-AIへの自由意志と責任の帰属可能性#^260811-231628|Soroeruを着想源として記録した会話]]"
  - "[[chanDeclutterARMobileDiminished2022]]"
---

# Personal Asset Data Store

<!-- concept-provenance-note:start -->
> [!abstract] 概念の来歴
> **区分**：本研究で導入した作業概念。
> **概念自体の来歴**：Personal Data StoreとMercariの持ち物一覧の発想を所有物データへ拡張するため、このVaultで導入した作業名称である。
> **本研究で加えた部分**：家庭内の所有物について、本人が保有・訂正・削除・移転・選択的開示できるデータ基盤として具体化する。
> **主な根拠**：[[2026-08-12-AIへの自由意志と責任の帰属可能性#^260811-231628|Soroeruを着想源として記録した会話]]、[[chanDeclutterARMobileDiminished2022]]。
> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。
> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。
> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。
> **注意**：この区分は、このVaultで研究用語として導入したことだけを示す。世界初の命名や、先行する同名用法の不存在は主張しない。
<!-- concept-provenance-note:end -->

個人が所有物について、何を所有するか、どこにあるか、状態、市場価値、本人が許可したpreferenceやdecision historyを、自ら保有・訂正・削除・移転できるデータ基盤。「ものの個人情報」を企業側profileではなく本人側のresourceとして構造化する。

## Architecture

```text
Physical AI / VLA
  -> real-world asset discovery and labeling
  -> Personal Asset Data Store on user device
  -> local structured retrieval + vector retrieval
  -> minimal task-specific context
  -> human or Personal Agent action
```

Physical AIはPADSを生成する手段、Personal Agentは活用手段であり、PADS自体は特定agentやmarketplaceから独立した価値を持つ。

## Data-Sovereignty Requirements

- Personal Asset Dataは端末内で暗号化し、企業サーバへ恒久保存しない。
- model trainingへ利用しない。
- 本人が確認、訂正、削除、exportできる。
- Personal Agentはfine-tuningではなくlocal retrievalで必要最小限のみ参照する。
- cloud inferenceではretrieved contextが送信される事実を明示し、on-device inferenceまたはconfidential computingを検討する。
- VLA研究データ、3D生成用一時動画、PADSを別目的・別同意・別retention policyで分離する。

## ELSI Significance

家庭内asset graphは窃盗、保険差別、経済状態推定、同居人profilingに悪用可能な高リスクデータである。同時に、本人管理なら家財管理、相続、保険、防災、data portabilityを支える。したがってPADSはprivacy riskの単なる保存先ではなく、AI時代のinformational self-governmentをarchitectureとして実装する提案である。

## Relation to Agency

PADSを外部記憶として使うPersonal Agentでは、agent identityとhardwareを分離できる。レンタルrobotが交換されても、本人が統制するmemory scaffoldが継続するため、[[AI Individuation]]における`model / physical instance / persona / scaffolded system`の区別を具体化する。
