# 诊断过程

## Diagnosis

一次独立诊断活动；同一对象可被多次诊断。记录输入上下文、依据、时间、版本、结果。采用**追加新诊断**，不原地改写。

## Finding

- 不可变；新诊断产生新 Finding（D-010）。  
- 有效性通过 FindingValidity 追加。  
- 可关联多个 Evidence；证据不足允许 UNCONFIRMED。  

## 错误归因

多重原因可并存；区分共存与因果；不能仅凭一道错题认定长期原因。

## KnowledgeIssue

长期问题对象，可关联多个 Finding / 题 / 作答 / 诊断 / 干预（D-011）。

### 归并方式（D-028）

- **自动归并**：诊断流水线将 Finding 自动创建或挂接到 KnowledgeIssue，**不依赖**家长/老师点选作为必经步骤。  
- 与 D-004 一致：模型原始输出不是事实；归并结果须经诊断/归并服务写入 `finding_issue_link`（及 Event）并绑定证据。  
- 置信不足 → UNCONFIRMED 或待观察 Issue，而不是改回人工闸门。  
- **算法细则**（相似度、合并/拆分、阈值）仍见 U-011，可迭代。

> 说明：Recovery Baseline 写了「归并到 KnowledgeIssue」，但未写死「必须人工」；曾出现的「V1 先人工」是精简提案误加，已废止。
