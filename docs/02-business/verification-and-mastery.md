# 验证与掌握度（P1）

**决策：** D-002、D-009、D-012、D-025（仅 KnowledgeState）、D-030、D-031  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 掌握学习「测–学–测」；BKT 可解释更新思想；间隔复习（先极简，不一次上完整 FSRS） |
| **搬运** | 即时验证 + 延迟验证用**新** LearningTask/Response；同 KC；State 按对错更新 |
| **自研** | 与纸质上传链路、KI 反馈指标对接 |

## 即时验证

干预后尽快：同 `KnowledgePointID` 变式题（或拆步题）→ 新作答 → 诊断。  
对：可降低提示强度、KI 可转 MONITORING。  
错：保留 OPEN，归并规则再挂 Finding；不覆盖原始卷。

## 延迟验证

间隔后（v0：按天简单档，如 1/3/7，可配置；**不**宣称完整间隔算法）。  
结果写入归并/State **反馈信号**（D-031 §6）。

## KnowledgeState 更新（v0 可解释）

搬运简化 mastery 计数 / BKT 直觉：

- 观测正确 → 提高 mastery 估计（有上限）  
- 观测错误（非 CARELESS 或 CARELESS 单独轨）→ 降低或维持  
- 每次更新：`StateRevision` + References（Finding/Response/Evidence）+ Event/Outbox 原子  

完整 BKT 四参数拟合：**后置**；v0 用可解释启发式 + `state_update_algorithm_version`。

## 成功信号（对齐目的，非 AI 时长）

- 同 KC 延迟验证通过率  
- 同 KI 上 SupportLevel 下降  
- INDEPENDENT 作答占比上升  
