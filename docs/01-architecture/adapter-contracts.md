# 适配层契约（闭环）

**决策：** D-030、U-001、D-031  

凡外部引擎/模型经适配层接入；契约稳定，实现可换。

## OCR Adapter

```
recognize(pages, meta) -> { candidates[], confidence, engine_id, engine_version }
apply_correction(candidate_ref, patch) -> Evidence (CORRECTED_FROM)
```

## Diagnose Adapter

```
diagnose(confirmed_responses, catalog_ctx) -> Diagnosis + Finding[]
  Finding 须尽量含 knowledge_point_id, error_class, is_primary_blame
```

## AutoMerge Service（规则，非黑盒）

```
merge(findings) -> FindingIssueLink[] + KnowledgeIssue create/update
  algorithm_id = ki_merge.kc_newman.v0
```

## Coach / Guidance Adapter

```
propose_guidance(ki, learner_state) -> { tasks[], support_level, guidance_algorithm_version }
```

## 反馈字段（所有适配输出）

`algorithm_id`, `algorithm_version`, `correlation_id`, 可选 `model_id`；业务落库后写 LearningEvent。
