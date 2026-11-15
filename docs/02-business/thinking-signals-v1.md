# V1 思维能力弱信号（P2 预澄清）

**决策：** D-003（知识与思维分别评价）、D-025（ThinkingState 缓建）、D-030  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | 知识与过程/策略分离（Newman transformation vs process）；ITS 对策略性错误的区分 |
| **搬运** | V1 不建 ThinkingState 表，但 Finding.ErrorClass / 引导 Event 保留策略类信号 |
| **自研** | 明确「暂缓建表 ≠ 放弃目的」 |

## V1 做法

- `STRATEGY_TRANSFORM` 等 Finding 计入分析报表与干预选题，**不**写入 ThinkingState。  
- 引导过程 Event 可标 `thinking_prompt_used=true`（元数据）。  
- V1.1+ 再落 ThinkingState，用历史 Finding/Event 回填校准。

避免实现时静默丢掉「批判/策略思维」产品目的。
