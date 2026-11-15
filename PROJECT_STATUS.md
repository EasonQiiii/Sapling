# PROJECT_STATUS

**最后更新：** 2026-11-15 21:30（Asia/Shanghai）  
**项目状态：** P0+P1 闭环设计规格已齐；下一刀 = 数学目录充实 + 精简 Migration 可执行化  
**当前分支目标：** 不等人追问——按计划推进落库必用表与种子

## 已完成

- [x] 文档地图、Recovery Baseline、D-001…D-032
- [x] D-030 搬运优先；D-031 KI=KC+Newman；D-032 练习自动
- [x] P0：科目目录骨架、归并、闭环步骤、OCR 人机边界
- [x] P1：薄干预、决策权限、验证/掌握度、思维弱信号
- [x] 适配层契约初稿；workflow 状态机对齐纸质闭环
- [x] entity-dictionary 挂学段/科目/KC/ErrorClass

## 进行中 / 下一步（自动推进顺序）

1. **充实数学课标目录节点**（从课标/教材公开结构继续搬运，扩 `math-knowledge-catalog-v0`）  
2. **写精简可执行 Migration 001→004→007→008→009**（005/006 DEFERRED）  
3. **种子 SQL + 空库执行**，结果写入 `docs/06-validation/`（NOT_RUN→PASS/FAIL）  
4. 归并/掌握度 **评测样例集**（关 U-011）

## 当前问题 / 阻塞

- OCR **引擎**未选型（适配层已定，不挡表结构）  
- 数学目录仍是骨架，需继续搬运填充  
- Migration 仍 PLACEHOLDER，尚无空库 PASS  

## 关键文档

| 文档 | 路径 |
|---|---|
| 整图 | `docs/DOC_MAP.md` |
| 闭环步骤 | `docs/02-business/closed-loop-steps.md` |
| 归并解法 | `docs/02-business/auto-merge-rules-v0.md` |
| 教练干预 | `docs/02-business/thin-intervention-coach.md` |
| 缺口审核 | `docs/06-validation/design-gap-audit.md` |
