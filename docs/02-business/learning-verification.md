# 学习验证

## 即时验证与延迟验证

干预后的验证必须是**新的真实作答**（新 LearningTask / 新 LearningResponse），不得覆盖原始作答（D-002、D-009）。

- 即时验证：干预后较短周期内检查是否掌握。  
- 延迟验证 / 迁移验证：间隔后或变式题上检查迁移。  

同一次真实学习行为可被多个 Intervention 引用评价，但默认只执行一次。

## 与 LearningState

验证产生的 Evidence / Finding 可作为 StateRevisionReference；状态更新使用 OCC（D-012）。
