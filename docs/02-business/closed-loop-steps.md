# 数学首闭环 · 逐步规格（P0）

**决策：** D-001、D-025…D-030  
**案例科目：** 数学（结构可换科目）  
**状态：** 规格 v0  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | ITS/作业批改流水线：提交→识别→诊断→反馈→再练；掌握学习「测-学-测」；BPMN/FSM 状态机 |
| **搬运** | 有限状态机表达闭环；诊断与反馈分离；再练用新作答 |
| **自研** | 映射到本系统对象与纸质约束；状态命名避免「再收集作答」误解 |

## 状态机（相对旧稿的澄清）

旧名 `COLLECTING_RESPONSES` **易误解为屏幕作答**。纸质闭环改为：

```text
CREATED
→ AWAITING_UPLOAD          # 纸质已完成，等待照片
→ INGESTING / PARSING      # OCR
→ NEEDS_CONFIRMATION       # 仅低置信/失败项
→ READY_FOR_DIAGNOSIS      # 已确认内容可诊断
→ BATCH_DIAGNOSING
→ AUTO_MERGING_ISSUES      # D-028
→ DECIDING_NEXT            # 薄 Decision
→ INTERVENTION_ACTIVE      # 薄干预（无 Stage 树）
→ VERIFYING                # 即时/延迟验证（新 Response）
→ REVIEWING
→ COMPLETED
```

（Workflow 真表用 DefinitionVersion 固定以上节点；U-006 最小校验稍后补。）

## 逐步说明

| 步 | 系统做 | 人做 | 产出对象 | 失败处理 |
|---|---|---|---|---|
| 1 建 Task | 写 subject/stage=数学/学段 | 可选 | LearningTask | — |
| 2 上传 | 存只读照片 Evidence | 上传 | Evidence | 重传 |
| 3 OCR | 适配层识别 | 仅低置信确认 | Evidence 候选/校正链 | 单题跳过不堵整卷 |
| 4 确认门槛 | 未确认不进归因 | 确认不确定项 | Response CONFIRMED | 保持 PENDING |
| 5 诊断 | 批诊断→Finding | 无 | Diagnosis/Finding | 重跑新 Diagnosis |
| 6 自动归并 | 规则 v0 | 无 | KI + Link | UNCONFIRMED/待观察 |
| 7 决策 | 生成下一步建议 | 默认无闸门 | DecisionRecord… | 降级为监控 |
| 8 薄干预 | 教练式提示，不代做 | 孩子再学/再答 | Intervention+新 Task | 暂停 |
| 9 验证 | 即时/延迟新作答 | 纸质再做可再传 | 新 Response | 回写 KI/State |
| 10 State | 更新 KnowledgeState | 无 | StateRevision+Refs | OCC 重试 |

## 与目的对齐的检查

- 每步是否可无「人当裁判」？（OCR 确认除外）  
- 是否保留原始作答？  
- 是否自动归并？  
- 干预是否像教练而非代做？  

## 相关

- `ocr-human-boundary.md`  
- `auto-merge-rules-v0.md`  
- `subject-and-catalog.md`  
