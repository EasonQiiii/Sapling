# Daily Learning Workflow（纸质数学首闭环）

**权威逐步规格：** [closed-loop-steps.md](./closed-loop-steps.md)  
**人机边界：** [ocr-human-boundary.md](./ocr-human-boundary.md)  
**决策：** D-001、D-025…D-031  

## 状态机（已对齐纸质优先）

```
CREATED
→ AWAITING_UPLOAD
→ INGESTING / PARSING
→ NEEDS_CONFIRMATION      # 仅低置信
→ READY_FOR_DIAGNOSIS
→ BATCH_DIAGNOSING
→ AUTO_MERGING_ISSUES     # D-028 / D-031
→ DECIDING_NEXT           # 默认自动出练习建议
→ INTERVENTION_ACTIVE     # 薄干预，无 Stage 树
→ VERIFYING
→ REVIEWING
→ COMPLETED
```

旧名 `COLLECTING_RESPONSES` / `AWAITING_STUDENT_CONFIRMATION` **已废弃**（易误解为屏幕作答）。

## 产品时序约束（D-001）

孩子先完成纸质作业，再上传照片，然后才 OCR 与统一诊断。  
禁止要求 OCR 前后重复完成同一份数字作业。

图源：`docs/diagrams/learning-workflow.mmd`。
