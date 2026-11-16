# LearningIntervention

Decision 提出干预意图；Learning Domain 创建与管理；LDSM 持久化；Workflow **不**直接管理 Intervention（D-014）。

## 生命周期

`PLANNED → ACTIVE → PAUSED → COMPLETED | CANCELLED | CLOSED`

- COMPLETED：目标达成且有证据  
- CLOSED：结束但不代表达成  
- CANCELLED：取消，不代表问题已解决  

## 对象（完整设计）

Intervention / Revision、Goal / GoalRevision / Link / Progress、Stage / StageGoal / Acceptance、StageTask / InterventionTask、Dependency、Relation 等。

## V1 建议（未决 U-013）

完整 Stage 依赖图过重。建议 MVP：`LearningIntervention` + `InterventionGoalRevision` + Task 链接；Stage 图延后。

共享 LearningTask 时：同一次真实行为默认只执行一次；各 Intervention 独立评价目标。
