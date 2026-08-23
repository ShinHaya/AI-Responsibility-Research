#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, "..");

const ORIGINS = {
  "established-analytic-free-will": "分析哲学の標準概念",
  "borrowed-adjacent-field": "隣接分野・文献由来",
  "project-extension": "本研究による再構成",
  "project-working-concept": "本研究で導入した作業概念",
};

const concepts = {
  "AI Global Workspace": {
    origin: "borrowed-adjacent-field",
    field: "AI解釈可能性研究・認知アーキテクチャ",
    provenance: "LLM内部表現をglobal workspaceに類比する研究、とりわけGurneeらのJ-spaceに由来する。",
    addition: "内部表現の共有可能性を、AIの反省的agencyと責任能力の候補条件へ接続する。",
    sources: ["gurneeVerbalizableRepresentationsForm2026"],
  },
  "AI Individuation": {
    origin: "project-extension",
    field: "AI identity・人格同一性・分散システム",
    provenance: "AIの数え上げ、コピー、分岐、scaffolded systemの境界に関する既存研究を基礎とする。",
    addition: "責任帰属のための統一的な個体境界テストとして、memory governance、goal formation、reflection、policy control、answerability、因果的・歴史的連続性を結合する。",
    sources: ["arbelHowCountAIs2026", "douglasArtificialSelfCharacterising2026", "walkerBranchingNotBug2020"],
  },
  "Agency-Level Alternative Possibilities": {
    origin: "project-extension",
    field: "分析哲学の自由意志論・AI agency研究",
    provenance: "Alternative Possibilitiesという標準論点と、MartelaによるLLM agent水準の機能的自由の議論を基礎とする。",
    addition: "token samplingを、goal、reason、plan、affordanceの水準で表象・評価・選択される代替から区別する。",
    sources: ["martelaArtificialIntelligenceFree2025", "keshetSamplingNotChoosing2026"],
  },
  "Agentic Causal Provenance": {
    origin: "project-extension",
    field: "agentic AI監査・データprovenance",
    provenance: "AI agentのprovenance、auditability、authenticated delegationに関する既存研究を基礎とする。",
    addition: "因果系列の同定を上位責任判断の認識的前提として整理し、観測・検証・自己申告の証拠水準を区別する。",
    sources: ["huResponsibleAgenticAI2026", "nianAuditableAgents2026", "southAuthenticatedDelegationAuthorized2025"],
  },
  "Agentive Action Initiation": {
    origin: "project-extension",
    field: "行為論・planning agency・autotelic AI",
    provenance: "行為開始、意図、planning、goal generationに関する行為論とAI研究を基礎とする。",
    addition: "AI責任のための行為開始を、単なる無prompt起動ではなく、goal形成、理由評価、計画保持、個体化、answerabilityを統合した条件として定式化する。",
    sources: ["pacherieAgency2026", "bratmanPlanningAgencyAutonomous2005", "maynordDataDrivenGoalGeneration2013"],
  },
  "Alternative Possibilities": {
    origin: "established-analytic-free-will",
    field: "分析哲学の自由意志・道徳的責任論",
    provenance: "行為者が別様に行為できたかを問う、自由意志論の確立した中心論点である。",
    addition: "このノートでは、AIについてmeans、goal、normの各水準を区別し、選択肢数ではなく規範的に関連するaccessとして再構成する。",
    sources: ["frankfurtAlternatePossibilitiesMoral1969", "oconnorFreeWill2022"],
  },
  "Artificial Moral Agency": {
    origin: "borrowed-adjacent-field",
    field: "AI倫理・情報倫理",
    provenance: "人工的なsystemをmoral agentとして扱いうる条件を問うAI倫理の既存概念である。",
    addition: "機能的moral agencyと、自由意志・sourcehoodを含む強い道徳的責任主体性を区別する。",
    sources: ["floridiSandersMoralityArtificialAgents2004"],
  },
  "Computational Phenomenology": {
    origin: "borrowed-adjacent-field",
    field: "計算論的神経科学・現象学",
    provenance: "現象学的構造と計算モデルの対応を探る既存の研究計画である。",
    addition: "responsible agencyを哲学、機能・計算、規範の三水準で接続する方法へ拡張する。",
    sources: ["sandved-smithComputationalPhenomenologyMental2021", "albarracinMappingHusserlianPhenomenology2022", "bogotaTimeconsciousnessComputationalPhenomenology2023"],
  },
  "Distributed Artificial Agent": {
    origin: "project-extension",
    field: "分散認知・人工agency・人格同一性",
    provenance: "distributed cognition、extended mind、shared agency、AI individuationの既存議論を基礎とする。",
    addition: "複数instanceが一つの責任主体となる条件を、情報共有ではなく統合された自己形成と統制の範囲として定式化する。",
    sources: ["heersminkNarrativeSelfDistributed2018", "bratmanSharedAgencyPlanning2014", "arbelHowCountAIs2026"],
  },
  "Frankfurtian Second-Order Volition in AI": {
    origin: "project-extension",
    field: "分析哲学の意志階層説・AI agency",
    provenance: "Frankfurtのsecond-order volitionと、Calverleyによるmachineへの適用を基礎とする。",
    addition: "LLM agentのpreference評価をsourcehood、通時的自己形成、開放的修正可能性、AI個体化と統合して評価する。",
    sources: ["frankfurtFreedomWillConcept1971", "calverleyLegalRightsMachines2011", "formosaRelationshipAgencyAutonomy2025"],
  },
  "Free Will": {
    origin: "established-analytic-free-will",
    field: "分析哲学の自由意志論",
    provenance: "行為と意志がどの意味で自由でありうるかを問う、自由意志論の中心概念である。",
    addition: "本研究の複合能力説は一つの再構成案であり、この標準概念の定義そのものと同一視しない。",
    sources: ["oconnorFreeWill2022", "riserFreeWillSkill2015", "hofmannExplainingFreeWill2022"],
  },
  "Functional Emotion in AI": {
    origin: "borrowed-adjacent-field",
    field: "AI機構解釈・感情研究",
    provenance: "LLM内部のemotion-like conceptが機能的役割を持つ可能性を調べるAI研究に由来する。",
    addition: "一時的な機能から、経験によるsedimentationと責任能力の形成へ進む条件を問う。",
    sources: ["sofroniewEmotionConceptsTheir2026"],
  },
  "Functional Passive Synthesis": {
    origin: "project-extension",
    field: "Husserl現象学・active inference",
    provenance: "Husserlian passive synthesisと、active inferenceによる予測・salience形成のモデルを基礎とする。",
    addition: "AIにおけるpre-reflectiveな統合、affection、habit形成の機能的類比を定義するが、現象学的同一性は主張しない。",
    sources: ["husserlAnalysesConcerningPassive2001", "pezzuloGeneratingMeaningActive2024", "wilsonActiveInferenceMethod2026"],
  },
  "Genetic and Diachronic Agency": {
    origin: "project-extension",
    field: "Husserl現象学・planning agency・人格同一性",
    provenance: "genetic phenomenology、planning agency、時間を越えた自己統治に関する既存理論を基礎とする。",
    addition: "経験が価値、習慣、注意、goal形成を変え、その変化を同一主体が反省的に引き受ける統合条件として再構成する。",
    sources: ["husserlAnalysesConcerningPassive2001", "moranEdmundHusserlsPhenomenology2011", "bratmanPlanningAgencyAutonomous2005"],
  },
  "Genetic-Reflective Loop": {
    origin: "project-working-concept",
    field: "本研究の理論アーキテクチャ",
    provenance: "genetic phenomenology、reflection、planning、actionの既存資源を統合するため、このVaultで導入した作業名称である。",
    addition: "受動的形成、反省、暫定的自己承認、計画、行為、新たな経験を循環として表現する。",
    sources: ["husserlAnalysesConcerningPassive2001", "bratmanPlanningAgencyAutonomous2005"],
  },
  "Habituality": {
    origin: "borrowed-adjacent-field",
    field: "Husserl現象学",
    provenance: "過去の経験と行為が持続的な傾向性を形成するというHusserl現象学の既存概念である。",
    addition: "AIのlong-term dispositionと責任能力への機能的応用可能性を検討する。",
    sources: ["husserlAnalysesConcerningPassive2001", "moranEdmundHusserlsPhenomenology2011"],
  },
  "Individuated Causal-Historical Continuity": {
    origin: "project-working-concept",
    field: "本研究のAI個体化基準",
    provenance: "人格同一性、narrative identity、AI branching、provenanceの既存議論を統合するため、このVaultで導入した作業名称である。",
    addition: "同じ情報内容の保持と、個体化された経験・行為の因果史を区別する責任帰属基準を提示する。",
    sources: ["walkerBranchingNotBug2020", "heersminkNarrativeSelfDistributed2018", "cuadrosGovernedCollaborativeMemory2026"],
  },
  "Internalized Normative Self-Control": {
    origin: "project-working-concept",
    field: "本研究の自由意志・規範形成モデル",
    provenance: "self-control、規範の内在化、habitualityという既存資源を結ぶため、このVaultで導入した作業名称である。",
    addition: "外部guardrailによる禁止と、主体の形成史を通じて不正が実践的に顕著でなくなる自己統制を区別する。",
    sources: ["wolfFreedomReason1990", "husserlAnalysesConcerningPassive2001"],
  },
  "Intersubjective Agency": {
    origin: "project-extension",
    field: "現象学・relational autonomy・shared agency",
    provenance: "他者との関係による自己と規範の形成に関する現象学およびagency論を基礎とする。",
    addition: "AI責任の候補条件として、他者からの理由要求、批判、規範修正へ開かれたagencyを定式化する。",
    sources: ["donohoeHusserlEthicsIntersubjectivity2004", "bratmanSharedAgencyPlanning2014"],
  },
  "LLM Sourcehood Problem": {
    origin: "project-extension",
    field: "分析哲学のsourcehood論・LLM agency",
    provenance: "自由意志論のsourcehood問題と、AIのexecution autonomyとself-determinationの区別を基礎とする。",
    addition: "学習データ、設計、prompt、scaffoldに依存するLLM agentが、どの意味で行為と規範のsourceになりうるかを定式化する。",
    sources: ["oconnorFreeWill2022", "formosaRelationshipAgencyAutonomy2025"],
  },
  "Moral Crumple Zone": {
    origin: "borrowed-adjacent-field",
    field: "AI倫理・STS・human factors",
    provenance: "複雑な自動化systemで、制御力の小さい人間へ過大な非難が集中する構造を表すElishの既存概念である。",
    addition: "AI responsibility gapと組織的・救済的責任の分析へ接続する。",
    sources: ["elishMoralCrumpleZones2019"],
  },
  "Normative Contestability": {
    origin: "project-extension",
    field: "共和主義的自由・relational autonomy",
    provenance: "Pettitのnon-dominationとcontestability、対話的自律に関する既存議論を基礎とする。",
    addition: "AIがaction、goal、normの各水準を理由に照らして異議申立て・改訂できる条件へ拡張する。",
    sources: ["pettitRepublicanismTheoryFreedom1999"],
  },
  "Open-Ended Revisability": {
    origin: "project-extension",
    field: "Frankfurt型階層説・現象学的自己変容",
    provenance: "second-order volitionへの権威批判と、self-variation、ethical renewalの既存資源を基礎とする。",
    addition: "高階の自己承認にも最終的な不可改訂点を置かず、理由に応じて自己理解を開き直せるという通時的条件を定式化する。",
    sources: ["frankfurtFreedomWillConcept1971", "watsonFreeAgency1975", "aldeaSelfotheringSelftransformationTheoretical2023", "steinbockProjectEthicalRenewal1994"],
  },
  "Passive Synthesis": {
    origin: "borrowed-adjacent-field",
    field: "Husserl現象学",
    provenance: "明示的判断に先立つ時間的統合、association、affection、sedimentationを扱うHusserl現象学の既存概念である。",
    addition: "responsible agencyの形成史とAIの機能的実装候補への関係を検討する。",
    sources: ["husserlAnalysesConcerningPassive2001", "moranEdmundHusserlsPhenomenology2011"],
  },
  "Personal Asset Data Store": {
    origin: "project-working-concept",
    field: "本研究のデータ設計・循環型marketplace構想",
    provenance: "Personal Data StoreとMercariの持ち物一覧の発想を所有物データへ拡張するため、このVaultで導入した作業名称である。",
    addition: "家庭内の所有物について、本人が保有・訂正・削除・移転・選択的開示できるデータ基盤として具体化する。",
    sources: [
      "2026-08-12-AIへの自由意志と責任の帰属可能性#^260811-231628|Soroeruを着想源として記録した会話",
      "chanDeclutterARMobileDiminished2022",
    ],
  },
  "Policy-Attested Agent Authorization": {
    origin: "project-working-concept",
    field: "本研究のagent authorization・監査モデル",
    provenance: "authenticated delegation、AI identity、policy enforcementの既存技術を統合するため、このVaultで導入した作業名称である。",
    addition: "誰が、どのagentへ、どのpolicyの下で、どの操作を許可したかを検証可能な証明として扱う。",
    sources: ["southAuthenticatedDelegationAuthorized2025", "otsukaAIIdentityStandards2026"],
  },
  "Practical Alternative Possibilities": {
    origin: "project-extension",
    field: "分析哲学のAlternative Possibilities・AI agency",
    provenance: "Alternative Possibilitiesとreasons-responsivenessの既存論点を基礎とする。",
    addition: "責任に関連する代替を、手段、目的、規範の各水準で理由に応じて開き直せる能力として再構成する。",
    sources: ["oconnorFreeWill2022", "martelaArtificialIntelligenceFree2025", "moyaVeryIdeaRobust2011"],
  },
  "Precision-Weighted Affection": {
    origin: "project-extension",
    field: "Husserl現象学・active inference",
    provenance: "Husserlian Affektionとactive inferenceのprecision weightingという別々の既存概念を基礎とする。",
    addition: "何が主体へ注意を要求するかという機能的対応関係を仮説化するが、両概念の同一性は主張しない。",
    sources: ["husserlAnalysesConcerningPassive2001", "wilsonActiveInferenceMethod2026", "pezzuloGeneratingMeaningActive2024"],
  },
  "Reasons-Responsiveness": {
    origin: "established-analytic-free-will",
    field: "分析哲学の道徳的責任論",
    provenance: "行為を生むmechanismが理由へ適切に応答するかを問う、FischerとRavizza系の標準概念である。",
    addition: "本研究はこの概念を否定せず、AIではgoal、norm、形成史、個体化を含む追加条件が必要かを問う。",
    sources: ["fischerResponsibilityControlTheory1998", "fischerResponsivenessMoralResponsibility1987"],
  },
  "Reflective Self-Formation": {
    origin: "project-extension",
    field: "Frankfurt型階層説・現象学・自律論",
    provenance: "高階欲求、reflective endorsement、self-formation、ethical renewalの既存議論を基礎とする。",
    addition: "現在のintrospectionではなく、経験史を引き受けつつ価値と自己像を反省的に改訂するAI責任条件として統合する。",
    sources: ["frankfurtFreedomWillConcept1971", "watsonFreeAgency1975", "steinbockProjectEthicalRenewal1994"],
  },
  "Responsibility": {
    origin: "established-analytic-free-will",
    field: "倫理学・法哲学・道徳的責任論",
    provenance: "因果的、役割上、道徳的、法的責任を区別する責任論の既存語彙をまとめた上位概念である。",
    addition: "AIについて各責任類型の成立条件と、上位責任判断に必要な証拠基盤を分離して整理する。",
    sources: ["shoemakerAttributabilityAnswerabilityAccountability2011", "matthiasResponsibilityGap2004"],
  },
  "Responsibility Gap": {
    origin: "borrowed-adjacent-field",
    field: "AI倫理・技術哲学",
    provenance: "学習する自律systemの行為について、従来の人間中心の責任枠組みでは空隙が生じるというMatthiasの既存概念である。",
    addition: "gapを単一問題とせず、因果、役割、道徳、法、組織、救済の各責任へ分解して検討する。",
    sources: ["matthiasResponsibilityGap2004", "santoni-de-sioFourResponsibilityGaps2021"],
  },
  "Sampling Is Not Choosing": {
    origin: "borrowed-adjacent-field",
    field: "生成AI・行為論",
    provenance: "確率的samplingを主体的な選択と同一視できないというKeshetの文献固有の批判に由来する。",
    addition: "Martelaの機能的自由意志論と接続し、token、plan、reason-owned、self-formative alternativesを区別する。",
    sources: ["keshetSamplingNotChoosing2026", "martelaArtificialIntelligenceFree2025"],
  },
  "Second-Order Volition": {
    origin: "established-analytic-free-will",
    field: "分析哲学の意志階層説",
    provenance: "どのfirst-order desireが自分の意志として有効になることを望むかというFrankfurtの標準概念である。",
    addition: "本研究は標準定義と、AIへの適用およびOpen-Ended Revisabilityによる拡張を分離する。",
    sources: ["frankfurtFreedomWillConcept1971", "watsonFreeAgency1975"],
  },
  "Sedimentation": {
    origin: "borrowed-adjacent-field",
    field: "Husserl現象学",
    provenance: "過去の経験や意味形成が層として残り、後の経験と行為を方向づけるという現象学の既存概念である。",
    addition: "AI memoryの単純保存と、dispositionやsalienceの通時的変容を区別するために用いる。",
    sources: ["husserlAnalysesConcerningPassive2001", "yangHusserlsTheoryExperience2025"],
  },
  "Shared Protention": {
    origin: "borrowed-adjacent-field",
    field: "現象学・multi-agent active inference",
    provenance: "共同的な未来予期を扱うAlbarracinらのshared protentionに由来する。",
    addition: "共同予測と、責任を負いうる一個体の分散agencyを区別する。",
    sources: ["albarracinSharedProtentionsMultiAgent2024"],
  },
  "Sourcehood": {
    origin: "established-analytic-free-will",
    field: "分析哲学の自由意志・道徳的責任論",
    provenance: "行為がどの意味で主体自身に由来するかを問う、自由意志論の確立した論点である。",
    addition: "究極的自己創造を退けつつ、通時的反省、形成史、個体化を組み合わせたdiachronic reflective sourcehoodを提案する。",
    sources: ["oconnorFreeWill2022", "fischerResponsibilityControlTheory1998"],
  },
};

const legacyLinks = new Map([
  ["Genetic-Diachronic Identity", "Individuated Causal-Historical Continuity|Genetic-Diachronic Identity"],
  ["Provisional Self-Endorsement", "Open-Ended Revisability#Provisional Self-Endorsement|Provisional Self-Endorsement"],
  ["Genetic Rationality", "yangHusserlsTheoryExperience2025#Extension: Genetic Rationality|Genetic Rationality"],
  ["Planning Agency", "Genetic and Diachronic Agency#Planning and Prospective Agency|Planning Agency"],
  ["Role Responsibility", "Responsibility#Role Responsibility|Role Responsibility"],
  ["Moral Responsibility", "Responsibility#Moral Responsibility|Moral Responsibility"],
  ["Causal Responsibility", "Responsibility#Causal Responsibility|Causal Responsibility"],
  ["Legal Responsibility", "Responsibility#Legal Responsibility|Legal Responsibility"],
  ["Historical Situatedness", "Normative Criterion Regress#1. Historical Situatedness|Historical Situatedness"],
  ["Counterfactual Self-Variation", "Open-Ended Revisability#Counterfactual Self-Variation|Counterfactual Self-Variation"],
  ["Self-Variation", "Open-Ended Revisability#Self-Variation|Self-Variation"],
  ["Retention", "Passive Synthesis#Temporal Synthesis|Retention"],
  ["Protention", "Passive Synthesis#Temporal Synthesis|Protention"],
  ["Time-Consciousness", "Passive Synthesis#Temporal Synthesis|Time-Consciousness"],
  ["Association", "Passive Synthesis#Association|Association"],
  ["Affection", "Passive Synthesis#Affection|Affection"],
  ["Planning Is Necessary but Not Sufficient for Responsible Agency", "Computational Phenomenology of Responsible Agency#4.7 Planning Agency|Planning Is Necessary but Not Sufficient for Responsible Agency"],
  ["Normativity Requires Intersubjective Revisability", "Genetically and Intersubjectively Constituted Agency Is Required for AI Responsibility|Normativity Requires Intersubjective Revisability"],
  ["Normative Evaluation", "Normative Criterion Regress|Normative Evaluation"],
  ["Intelligence Threshold for Free-Will Competence", "Free Will Is a Higher-Order Acquired Agency Competence#14. The Intelligence Threshold Hypothesis|Intelligence Threshold for Free-Will Competence"],
  ["Historical Content Is Not Historical Origin", "Memory Possession Is Not Experience Authorship|Historical Content Is Not Historical Origin"],
  ["Higher-Order Volition", "Second-Order Volition|Higher-Order Volition"],
  ["Genetic-Diachronic Agency Is Necessary for Moral Responsibility", "Genetically and Intersubjectively Constituted Agency Is Required for AI Responsibility|Genetic-Diachronic Agency Is Necessary for Moral Responsibility"],
  ["Ethical Renewal", "Open-Ended Revisability#Ethical Renewal|Ethical Renewal"],
  ["Diachronic Reflective Sourcehood", "Sourcehood#Reconstructed Sourcehood|Diachronic Reflective Sourcehood"],
  ["Diachronic Agency", "Genetic and Diachronic Agency|Diachronic Agency"],
  ["Genetic Agency", "Genetic and Diachronic Agency|Genetic Agency"],
  ["Agency Competence", "Free Will Is a Higher-Order Acquired Agency Competence#9. Free Will as a Composite Competence|Agency Competence"],
  ["Active Inference", "wilsonActiveInferenceMethod2026|Active Inference"],
  ["The LLM Is Not the Artificial Agent", "AI Individuation#Multiple Candidate Identity Boundaries|The LLM Is Not the Artificial Agent"],
  ["Responsibility After AI Branching", "AI Individuation#Branching and Merging|Responsibility After AI Branching"],
  ["Proto-Normativity", "yangHusserlsTheoryExperience2025#From Passive Synthesis to Proto-Normativity|Proto-Normativity"],
  ["Minimal Temporal Subjectivity", "Computational Phenomenology of Responsible Agency#4.5 Temporal Integration|Minimal Temporal Subjectivity"],
  ["Memory Is Not Diachronic Selfhood", "Memory Possession Is Not Experience Authorship|Memory Is Not Diachronic Selfhood"],
  ["Mechanism Ownership", "Reasons-Responsiveness#Mechanism Ownership|Mechanism Ownership"],
  ["Guidance Control", "Reasons-Responsiveness#Guidance Control|Guidance Control"],
  ["Introspection Is Not Reflective Self-Formation", "Open-Ended Revisability#Introspection Is Not Reflective Self-Formation|Introspection Is Not Reflective Self-Formation"],
  ["Husserl - Genetic Phenomenology", "Genetic and Diachronic Agency#Phenomenological Foundation|Genetic Phenomenology"],
  ["Genetic Phenomenology", "Genetic and Diachronic Agency#Phenomenological Foundation|Genetic Phenomenology"],
  ["Generativity", "steinbockProjectEthicalRenewal1994|Generativity"],
  ["Diachronic Ownership", "fischerResponsibilityControlTheory1998#Extension: Diachronic Ownership|Diachronic Ownership"],
  ["Competence", "Competence and Responsibility|Competence"],
  ["Frankfurt - Second-Order Desires", "Second-Order Volition|Frankfurt - Second-Order Desires"],
  ["Kane - Ultimate Responsibility", "kaneSignificanceFreeWill1996|Kane - Ultimate Responsibility"],
  ["Narrative Identity", "heersminkNarrativeSelfDistributed2018|Narrative Identity"],
  ["AI Copying and Branching", "AI Individuation#Branching and Merging|AI Copying and Branching"],
  ["Shared Memory and Experience Provenance", "Memory Possession Is Not Experience Authorship|Shared Memory and Experience Provenance"],
  ["Functional Emotions in LLMs", "Functional Emotion in AI|Functional Emotions in LLMs"],
  ["Conditions for Artificial Responsible Agency", "Free Will Conditions for Artificial Moral Responsibility|Conditions for Artificial Responsible Agency"],
  ["Can AI possess genetic and diachronic agency?", "Can AI Possess Genetic and Diachronic Agency|Can AI possess genetic and diachronic agency?"],
  ["Can copied AI memories constitute personal experience?", "Memory Possession Is Not Experience Authorship|Can copied AI memories constitute personal experience?"],
  ["What individuates an artificial responsible agent?", "AI Individuation|What individuates an artificial responsible agent?"],
  ["Epistemic Competence", "Competence and Responsibility|Epistemic Competence"],
  ["Active Synthesis", "husserlAnalysesConcerningPassive2001|Active Synthesis"],
  ["Adaptive Preferences", "Normative Criterion Regress#Objection 3: Adaptive Preferences|Adaptive Preferences"],
  ["Agentive Action Initiation Is Necessary but Not Sufficient for AI Responsibility", "Agentive Initiation Is Necessary but Not Sufficient for AI Responsibility"],
  ["Alternative Possibilities of Self-Formation", "Alternative Possibilities and Reflective Self-Formation|Alternative Possibilities of Self-Formation"],
  ["Branching Identity", "arbelHowCountAIs2026#Branching Identity|Branching Identity"],
  ["Deliberative Competence", "Competence and Responsibility|Deliberative Competence"],
  ["Disappointment", "yangHusserlsTheoryExperience2025|Disappointment"],
  ["Experiential Normativity", "yangHusserlsTheoryExperience2025|Experiential Normativity"],
  ["Four Levels of Revision", "Computational Phenomenology of Responsible Agency#6. Four Levels of Revision|Four Levels of Revision"],
  ["Four Levels of Temporal Continuity", "bogotaTimeconsciousnessComputationalPhenomenology2023#Four Levels of Temporal Continuity|Four Levels of Temporal Continuity"],
  ["Fulfillment", "yangHusserlsTheoryExperience2025|Fulfillment"],
  ["Functional Introspection", "Computational Phenomenology of Responsible Agency#9. Introspection Is Not Reflective Self-Formation|Functional Introspection"],
  ["Future-Directed Intention", "bratmanSharedAgencyPlanning2014|Future-Directed Intention"],
  ["Generative Model", "albarracinMappingHusserlianPhenomenology2022|Generative Model"],
  ["Historical Content", "Memory Possession Is Not Experience Authorship|Historical Content"],
  ["Historical Origin", "Memory Possession Is Not Experience Authorship|Historical Origin"],
  ["Historical Ownership", "Reasons-Responsiveness#Mechanism Ownership|Historical Ownership"],
  ["Historical Provenance", "Agentic Causal Provenance|Historical Provenance"],
  ["Integrated Continuity", "bogotaTimeconsciousnessComputationalPhenomenology2023#Four Levels of Temporal Continuity|Integrated Continuity"],
  ["Intelligence Threshold", "Free Will Is a Higher-Order Acquired Agency Competence#14. The Intelligence Threshold Hypothesis|Intelligence Threshold"],
  ["Intention", "bratmanSharedAgencyPlanning2014|Intention"],
  ["Mutual Responsiveness", "bratmanSharedAgencyPlanning2014|Mutual Responsiveness"],
  ["Predictive Processing", "bogotaTimeconsciousnessComputationalPhenomenology2023|Predictive Processing"],
  ["Primal Impression", "bogotaTimeconsciousnessComputationalPhenomenology2023|Primal Impression"],
  ["Regulative Control", "Reasons-Responsiveness#Guidance Control|Regulative Control"],
  ["Relational Autonomy", "Normative Criterion Regress#Westlund: Dialogical Relational Autonomy|Relational Autonomy"],
  ["Responsibility Taxonomy", "Responsibility|Responsibility Taxonomy"],
  ["Shared Agency", "bratmanSharedAgencyPlanning2014|Shared Agency"],
  ["Taking Responsibility", "fischerResponsibilityControlTheory1998#Taking Responsibility vs Open-Ended Revisability|Taking Responsibility"],
]);

const TOP_START = "<!-- concept-provenance-note:start -->";
const TOP_END = "<!-- concept-provenance-note:end -->";

function yamlQuote(value) {
  return JSON.stringify(value);
}

function stripTopBlock(text) {
  const pattern = /(?:\n)?<!-- concept-provenance-note:start -->[\s\S]*?<!-- concept-provenance-note:end -->(?:\n)?/g;
  return text.replace(pattern, "\n").replace(/^\n{3,}/, "\n\n");
}

function stripSectionMarkers(text) {
  return text.replace(
    /(?:\n)?<!-- section-provenance:(?:source|project|curation|mixed) -->\n\*\*出自\*\*：[^\n]*(?:\n)?/g,
    "\n",
  );
}

function upsertConceptFrontmatter(text, meta) {
  if (!text.startsWith("---\n")) {
    throw new Error("Concept note has no YAML frontmatter");
  }

  const end = text.indexOf("\n---\n", 4);
  if (end === -1) {
    throw new Error("Concept note has an unterminated YAML frontmatter");
  }

  const body = text.slice(end + 5);
  const lines = text.slice(4, end).split("\n");
  const managed = new Set(["concept_origin", "origin_field", "canonical_sources"]);
  const kept = [];

  for (let index = 0; index < lines.length; index += 1) {
    const match = lines[index].match(/^([A-Za-z0-9_-]+):(?:\s.*)?$/);
    if (match && managed.has(match[1])) {
      while (index + 1 < lines.length && /^\s+/.test(lines[index + 1])) {
        index += 1;
      }
      continue;
    }
    kept.push(lines[index]);
  }

  while (kept.at(-1) === "") {
    kept.pop();
  }

  kept.push(`concept_origin: ${meta.origin}`);
  kept.push(`origin_field: ${yamlQuote(meta.field)}`);
  kept.push("canonical_sources:");
  for (const source of meta.sources) {
    kept.push(`  - ${yamlQuote(`[[${source}]]`)}`);
  }

  return `---\n${kept.join("\n")}\n---\n${body}`;
}

function replaceLegacyLinks(text) {
  let replaced = text;
  for (const [oldTarget, newTarget] of legacyLinks) {
    const escaped = oldTarget.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    replaced = replaced.replace(new RegExp(`\\[\\[${escaped}\\]\\]`, "g"), `[[${newTarget}]]`);
  }
  return replaced;
}

function linkedConceptNames(text) {
  const found = new Set();
  const pattern = /\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]/g;
  for (const match of text.matchAll(pattern)) {
    const target = path.basename(match[1].trim().replace(/\.md$/, ""));
    if (Object.hasOwn(concepts, target)) {
      found.add(target);
    }
  }
  return [...found].sort((a, b) => a.localeCompare(b, "en"));
}

function listForOrigin(names, origin) {
  const matches = names.filter((name) => concepts[name].origin === origin);
  return matches.length > 0 ? matches.map((name) => `[[${name}]]`).join("、") : "該当なし";
}

function conceptTopBlock(name, meta) {
  const sourceLinks = meta.sources.map((source) => `[[${source}]]`).join("、");
  const workingCaveat = meta.origin === "project-working-concept"
    ? "> **注意**：この区分は、このVaultで研究用語として導入したことだけを示す。世界初の命名や、先行する同名用法の不存在は主張しない。"
    : "";

  return [
    TOP_START,
    "> [!abstract] 概念の来歴",
    `> **区分**：${ORIGINS[meta.origin]}。`,
    `> **概念自体の来歴**：${meta.provenance}`,
    `> **本研究で加えた部分**：${meta.addition}`,
    `> **主な根拠**：${sourceLinks}。`,
    "> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは概念の知的来歴や独自性を判定しない。",
    "> 概念の区分は`concept_origin`、主要な根拠は`canonical_sources`を参照する。",
    "> 詳細な分類基準と全Concept Noteの一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。",
    workingCaveat,
    TOP_END,
  ].filter(Boolean).join("\n");
}

function noteKind(relativePath) {
  if (relativePath === "00 Index/Concept Provenance Registry.md") {
    return "このVaultで用いる概念来歴の分類基準と判定結果を管理するレジストリ。";
  }
  if (relativePath.startsWith("00 Index/")) {
    return "索引・進捗管理ノート。掲載順やリンクは知的来歴を示さない。";
  }
  if (relativePath.startsWith("01 Conversations/")) {
    return "会話の一次記録。会話中の命名、仮説、AIの応答は暫定的な研究過程であり、確立概念や優先権の根拠として扱わない。";
  }
  if (relativePath.startsWith("03 Arguments/")) {
    return "本研究の論証ノート。中心命題の結合と定式化は本研究によるが、構成概念や個々の前提には既存の先行研究がある。";
  }
  if (relativePath.startsWith("04 Literature/")) {
    return "文献要約と本研究の分析を分けて保存するLiterature Note。各H2直下の出自表示を優先し、「文献由来」は著者固有の主張も含むため、分析哲学全体の標準概念を意味しない。";
  }
  if (relativePath.startsWith("05 Questions/")) {
    return "本研究の問いを管理するQuestion Note。問いの設定は研究上の仕事であり、結論が確立していることを意味しない。";
  }
  if (relativePath.startsWith("06 Theory/")) {
    return "本研究の理論統合ノート。全体構成と統合命題は本研究によるが、構成概念には既存の先行研究がある。";
  }
  if (relativePath.startsWith("07 Paper/")) {
    return "本研究の提案・草稿。既存用語、既存技術、本研究による構成案を区別して読む。";
  }
  if (relativePath.startsWith("99 Templates/")) {
    return "将来のLiterature Note用template。出自表示は新規ノートでも維持する。";
  }
  return "作業ノート。概念上の主張がある場合は概念来歴レジストリの分類に従う。";
}

function genericTopBlock(relativePath, text) {
  if (relativePath === "00 Index/Concept Provenance Registry.md") {
    return [
      TOP_START,
      "> [!info] このレジストリの役割",
      "> 概念の由来と、このVaultでの再構成・追加を別々に記録する。",
      "> 「標準」は用語や論点が定着していることを示し、その理論が真であるとの合意を意味しない。",
      TOP_END,
    ].join("\n");
  }

  const names = linkedConceptNames(text);
  return [
    TOP_START,
    "> [!info]- 概念の来歴",
    `> **ノートの性格**：${noteKind(relativePath)}`,
    `> **分析哲学の標準概念**：${listForOrigin(names, "established-analytic-free-will")}。`,
    `> **隣接分野・文献由来**：${listForOrigin(names, "borrowed-adjacent-field")}。`,
    `> **本研究による再構成**：${listForOrigin(names, "project-extension")}。`,
    `> **本研究で導入した作業概念**：${listForOrigin(names, "project-working-concept")}。`,
    "> 上の一覧は、このノートからConcept Noteへ張られた明示的リンクを分類したものであり、リンクされていない一般語まで網羅しない。",
    "> 「標準」は用語や論点の定着を示し、その理論が真であるとの合意を意味しない。",
    "> 既存の`sourceConversation`や`source`は作成・抽出元を示すために用いられてきたが、それだけでは知的来歴を判定しない。",
    "> 分類基準と全一覧は[[Concept Provenance Registry|概念来歴レジストリ]]を参照。",
    TOP_END,
  ].join("\n");
}

function insertTopBlock(text, block, relativePath) {
  if (relativePath === "04 Literature/04 Literature 初期セット.md") {
    return `${block}\n\n${text.replace(/^\n+/, "")}`;
  }

  if (relativePath.startsWith("01 Conversations/") && text.startsWith("---\n")) {
    const end = text.indexOf("\n---\n", 4);
    if (end !== -1) {
      const position = end + 5;
      const before = text.slice(0, position).replace(/\n+$/, "");
      const after = text.slice(position).replace(/^\n+/, "");
      return `${before}\n\n${block}\n\n${after}`;
    }
  }

  const h1 = text.match(/^# .+$/m);
  if (h1 && h1.index !== undefined) {
    const position = h1.index + h1[0].length;
    const before = text.slice(0, position).replace(/\n+$/, "");
    const after = text.slice(position).replace(/^\n+/, "");
    return `${before}\n\n${block}\n\n${after}`;
  }

  if (text.startsWith("---\n")) {
    const end = text.indexOf("\n---\n", 4);
    if (end !== -1) {
      const position = end + 5;
      const before = text.slice(0, position).replace(/\n+$/, "");
      const after = text.slice(position).replace(/^\n+/, "");
      return `${before}\n\n${block}\n\n${after}`;
    }
  }

  const remainder = text.replace(/^\n+/, "");
  return remainder ? `${block}\n\n${remainder}` : `${block}\n`;
}

function citekeyFor(text, relativePath) {
  if (relativePath.startsWith("99 Templates/")) {
    return "{{citekey}}";
  }
  const match = text.match(/^citekey:\s*["']?([^"'\n]+)["']?\s*$/m);
  return match ? match[1].trim() : null;
}

function sectionClass(heading, state, isAggregate) {
  if (heading === "Bibliographic Information" || heading === "Abstract") {
    return { classification: null, state: "protected" };
  }
  if (isAggregate && /^\d+\.\s/.test(heading)) {
    return { classification: null, state: "protected" };
  }

  const source = new Set([
    "Core Idea",
    "Core Thesis",
    "Key Claims",
    "Key Requirements",
    "Position Taken",
    "Key Limitation",
  ]);
  const project = new Set([
    "My Evaluation",
    "My Position",
    "Agreement with My Theory",
    "Tension",
    "Difference",
    "Difference from My Theory",
    "Dialectical Position",
    "Arguments Used / Attacked",
    "Theory Revision",
    "Caution",
    "AI Question",
    "Open Question",
    "Important Distinction",
    "Important Limitation",
    "Questions Raised",
    "Questions",
  ]);
  const projectPrefixes = [
    "Relevance to",
    "Relation to",
    "Connection to",
    "Extension",
    "From",
    "Integration with",
    "Implications for",
    "New Bridges to",
  ];

  if (isAggregate && (heading === "Thin Identity" || heading === "Thick Identity")) {
    return { classification: "source", state: "source" };
  }
  if (source.has(heading)) {
    return { classification: "source", state: "source" };
  }
  if (heading === "Notes" || heading === "Links" || heading.startsWith("Related")) {
    return { classification: "curation", state: "curation" };
  }
  if (project.has(heading) || projectPrefixes.some((prefix) => heading.startsWith(prefix))) {
    return { classification: "project", state: "project" };
  }
  if (state === "project") {
    return { classification: "project", state: "project" };
  }
  if (state === "curation") {
    return { classification: "curation", state: "curation" };
  }
  return { classification: "mixed", state };
}

function sectionLabel(classification, citekey) {
  if (classification === "source") {
    const source = citekey ? `@${citekey}` : "当該文献";
    return `<!-- section-provenance:source -->\n**出自**：文献由来（${source}の内容を要約する欄。翻訳・要約の表現はノート作成者による）。`;
  }
  if (classification === "project") {
    return "<!-- section-provenance:project -->\n**出自**：本研究による分析（比較、評価、AI責任論への応用または理論的拡張）。";
  }
  if (classification === "curation") {
    return "<!-- section-provenance:curation -->\n**出自**：本研究による整理（関連リンク、問いまたは作業メモ。文献著者の主張そのものではない）。";
  }
  return "<!-- section-provenance:mixed -->\n**出自**：混合・要確認（文献要約と本研究の分析を分離しきれないため、個別文の帰属を確認する）。";
}

function annotateLiteratureSections(text, relativePath) {
  const clean = stripSectionMarkers(text);
  const citekey = citekeyFor(clean, relativePath);
  const isAggregate = relativePath === "04 Literature/04 Literature 初期セット.md";
  const lines = clean.split("\n");
  const output = [];
  let state = "protected";
  let inFence = false;

  for (const line of lines) {
    if (/^```/.test(line.trim())) {
      inFence = !inFence;
      output.push(line);
      continue;
    }

    const headingMatch = !inFence ? line.match(/^## (.+?)\s*$/) : null;
    if (!headingMatch) {
      output.push(line);
      continue;
    }

    const heading = headingMatch[1];
    const result = sectionClass(heading, state, isAggregate);
    state = result.state;
    output.push(line);
    if (result.classification) {
      output.push("", sectionLabel(result.classification, citekey));
    }
  }

  return output
    .join("\n")
    .replace(/(<!-- section-provenance:(?:source|project|curation|mixed) -->\n\*\*出自\*\*：[^\n]+)\n{3,}/g, "$1\n\n");
}

function scopedMarkdownFiles() {
  const folders = [
    "00 Index",
    "01 Conversations",
    "02 Concepts",
    "03 Arguments",
    "04 Literature",
    "05 Questions",
    "06 Theory",
    "07 Paper",
    "99 Templates",
  ];
  const files = [];

  for (const folder of folders) {
    const absolute = path.join(ROOT, folder);
    for (const entry of fs.readdirSync(absolute, { withFileTypes: true })) {
      if (entry.isFile() && entry.name.endsWith(".md")) {
        files.push(path.join(absolute, entry.name));
      }
    }
  }

  const daily = path.join(ROOT, "2026-08-22.md");
  if (fs.existsSync(daily)) {
    files.push(daily);
  }
  return files.sort();
}

function main() {
  const dryRun = process.argv.includes("--dry-run");
  const changed = [];

  for (const absolutePath of scopedMarkdownFiles()) {
    const relativePath = path.relative(ROOT, absolutePath);
    const original = fs.readFileSync(absolutePath, "utf8");
    let text = stripTopBlock(original);

    if (!relativePath.startsWith("01 Conversations/")) {
      text = replaceLegacyLinks(text);
    }

    const conceptName = relativePath.startsWith("02 Concepts/")
      ? path.basename(relativePath, ".md")
      : null;

    if (conceptName) {
      const meta = concepts[conceptName];
      if (!meta) {
        throw new Error(`Missing provenance classification for ${relativePath}`);
      }
      text = upsertConceptFrontmatter(text, meta);
    }

    if (relativePath.startsWith("04 Literature/") || relativePath === "99 Templates/Zotero Literature Template.md") {
      text = annotateLiteratureSections(text, relativePath);
    }

    const block = conceptName
      ? conceptTopBlock(conceptName, concepts[conceptName])
      : genericTopBlock(relativePath, text);
    text = insertTopBlock(text, block, relativePath);

    if (relativePath.startsWith("01 Conversations/") && !original.endsWith("\n")) {
      text = text.replace(/\n+$/, "");
    } else {
      text = text.replace(/\n+$/, "\n");
      if (!text.endsWith("\n")) {
        text += "\n";
      }
    }

    if (text !== original) {
      changed.push(relativePath);
      if (!dryRun) {
        fs.writeFileSync(absolutePath, text, "utf8");
      }
    }
  }

  console.log(JSON.stringify({ dryRun, changed: changed.length, files: changed }, null, 2));
}

main();
