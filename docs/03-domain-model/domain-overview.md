# 领域模型总览

十大逻辑领域：

1. Platform / Identity  
2. Learning  
3. Assessment  
4. Evidence / Event  
5. Diagnosis  
6. Learning State  
7. Decision  
8. Policy  
9. Workflow / Methodology  
10. AI Execution / Audit  

## 关键不变式

- 稳定全局 ID；需要版本的对象用独立 Revision ID。  
- 有业务意义的关联有独立 ID；历史关系固定必要版本。  
- 核心关系优先专用关联实体 + 真外键；通用多目标才用 target_type/id。  
- Diagnosis 追加新诊断；Finding 不可变。  

详见 [logical-data-model.md](./logical-data-model.md)、[entity-catalog.md](./entity-catalog.md)、[entity-dictionary.md](./entity-dictionary.md)。
