# 薄干预 · 教练行为（P1）

**决策：** D-014、D-025（无 Stage）、D-030  
**状态：** 规格 v0  

## 学自 / 搬运 / 自研

| | 内容 |
|---|---|
| **学自** | Cognitive Tutor / ASSISTments：**hints + scaffolds**；苏格拉底式追问；提示逐渐撤除（fading） |
| **搬运** | 提示强度阶梯；先独立再提示；脚手架拆步；成功后降强度 |
| **自研** | 映射到无 Stage 的 `LearningIntervention` + 新 LearningTask/Response；纸质再练上传 |

## 最小干预循环（无 Stage 树）

```text
选中开放 KI（自动）
→ 生成练习/引导任务（新 LearningTask，subject/stage 继承）
→ 提示强度 = f(KI 历史, SupportLevel)
→ 孩子纸质作答 → 上传 → 诊断/归并/State
→ 成功则降强度；失败则同 KC 换角度，仍禁止直接给最终答案
```

## 提示强度（对齐 Response.SupportLevel）

| 级别 | 行为 | 学自 |
|---|---|---|
| NONE | 只出题，无讲解 | 独立练习 |
| HINT | 概念提醒/方向 | ITS hint |
| GUIDED | 拆步脚手架 | ASSISTments scaffold |
| DIRECT_INSTRUCTION | 短示范（仍要求孩子再做一题） | 最小直接教学 |

**禁止：** 把原题标准答案直接交给孩子当「完成」。

## 反馈

`guidance_algorithm_version`；延迟验证通过率；同 KI 上 SupportLevel 是否下降（P5：不用 AI 时长）。
