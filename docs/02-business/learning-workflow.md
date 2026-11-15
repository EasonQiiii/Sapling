# Daily Learning Workflow

## 状态机（设计）

```
CREATED
  → INGESTING
  → PARSING
  → NEEDS_CONFIRMATION
  → PLANNING
  → AWAITING_STUDENT_CONFIRMATION
  → COLLECTING_RESPONSES
  → BATCH_DIAGNOSING
  → LEARNING_PLAN_READY
  → INTERVENTION
  → REVIEWING
  → COMPLETED
```

## 产品时序约束（D-001）

孩子先完成纸质作业，再上传照片，然后才 OCR 与统一诊断。  
禁止要求 OCR 前后重复完成同一份数字作业。

转换守卫、各状态责任人、异常/恢复路径：**尚未规格化**（设计缺口）。

图源：`docs/diagrams/learning-workflow.mmd`。
