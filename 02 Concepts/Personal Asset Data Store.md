---
type: concept
status: developing
created: 2026-08-22
tags: [personal-data, data-sovereignty, physical-ai, elsi]
---

# Personal Asset Data Store

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
