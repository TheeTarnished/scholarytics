# Paper Super Reviewer

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-2.1.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

端到端学术论文超审系统 — Hermes Agent Skill。三智能体并行审稿 + 跨审稿综合。

## 示范审稿 — ResNet (何恺明, 2015)

对 "Deep Residual Learning for Image Recognition" 的完整审核：

> 🏆 **Landmark Paper — 30/30 满分. Unanimous Strong Accept.**

| 维度 | 分数 | 审稿人评价 |
|------|:--:|------|
| Novelty | 5/5 | 残差学习是深度学习史上最重要的架构创新之一 |
| Soundness | 5/5 | 教科书级实验设计 — plain-34 vs ResNet-34 对比精妙 |
| Evidence | 5/5 | ILSVRC 2015 全赛道冠军 + 200,000+ 引用验证 |
| Related Work | 5/5 | 精确定位 Highway Networks 等前置工作并清晰区分 |
| Reproducibility | 5/5 | 开源代码 + 精确超参 + 固定种子 |
| Significance | 5/5 | 启发了 Transformer、AlphaFold、GPT 等所有现代架构 |

**三位审稿人独立评价:**

| Agent | 核心评价 |
|-------|---------|
| 🛠️ 方法论审稿人 | "Figure 2 中 plain-34 比 plain-18 训练误差更高——直接证明退化是优化问题而非过拟合。这一个观察就值一篇论文。" |
| 🎓 领域审稿人 | "H(x)=F(x)+x，一行公式定义全书。最简单的 idea 往往最深刻。改变了 CV→NLP→RL 全领域的进程。" |
| ✍️ 通才审稿人 | "写作极其清晰。即使非 CV 领域读者也能无障碍理解核心贡献。每读一遍都有新收获。" |

→ **[完整审稿报告](demo/RESNET_REVIEW.md)** ← 含三智能体详细意见 + 跨审稿综合 + 引用审计

---

## 架构

| Agent | 角色 | 职责 |
|-------|------|------|
| Agent 1 | 方法论审稿人 | 技术健全性、实验设计、可复现性 |
| Agent 2 | 领域审稿人 | 创新性、SOTA对比、贡献显著性 |
| Agent 3 | 通才审稿人 | 写作质量、可读性、格式规范 |

## 功能

- 定量评分卡 (6维 × 5分制 = 30总分)
- 三智能体独立审稿意见
- 跨审稿综合 (共识优势/风险/分歧)
- 引用质量审计
- LaTeX 格式检查
- 完整性审计 (claim-evidence)
- 关注-行动表 (按严重度排序)

## 安装

### Hermes Agent
```bash
hermes skills install paper-super-reviewer
```

### Claude Code
```bash
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/
# 使用: /claude skill load paper-super-reviewer
```

### Codex CLI
```bash
mkdir -p ~/.codex/skills/paper-super-reviewer
cp SKILL.md ~/.codex/skills/paper-super-reviewer/
```

## 使用

```
审核论文: path/to/paper.tex, mode=full
```
