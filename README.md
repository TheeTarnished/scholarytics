# Paper Super Reviewer / 论文超审

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-2.1.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

**[English](#english) | [中文](#中文)**

---

## English

End-to-end academic paper review system — Hermes Agent Skill. Three specialized AI agents conduct parallel peer review, then synthesize findings into a structured review report.

### Live Demo — ResNet (He et al., 2015)

> 🏆 **30/30 — Landmark Paper. Unanimous Strong Accept.**

| Dimension | Score |
|-----------|:--:|
| Novelty | 5/5 |
| Soundness | 5/5 |
| Evidence | 5/5 |
| Related Work | 5/5 |
| Reproducibility | 5/5 |
| Significance | 5/5 |

→ **[Full Review Report →](demo/RESNET_REVIEW.md)** ← Three-agent panel + cross-review synthesis

### Architecture

| Agent | Role | Focus |
|-------|------|-------|
| Agent 1 | Methodology Reviewer | Technical soundness, experimental design, reproducibility |
| Agent 2 | Domain Reviewer | Novelty, SOTA comparison, contribution significance |
| Agent 3 | General Reviewer | Writing quality, readability, formatting |

### Features
- Quantitative scorecard (6 dimensions × 5-point scale = 30 total)
- Three independent agent opinions
- Cross-review synthesis (consensus / risks / disagreements)
- Reference quality audit
- LaTeX format check
- Integrity audit (claim-evidence alignment)
- Concern-to-action table (sorted by severity)

### Install

**Hermes Agent**
```bash
hermes skills install paper-super-reviewer
```

**Claude Code**
```bash
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/
# Usage: /claude skill load paper-super-reviewer
```

**Codex CLI**
```bash
mkdir -p ~/.codex/skills/paper-super-reviewer
cp SKILL.md ~/.codex/skills/paper-super-reviewer/
```

### Usage
```
Review paper: path/to/paper.tex, mode=full
```

---

## 中文

端到端学术论文超审系统 — Hermes Agent Skill。三个专业化 AI 智能体并行审稿，模拟真实学术评审全流程，输出结构化审稿报告。

### 示范审稿 — ResNet (何恺明, 2015)

> 🏆 **30/30 满分 — Landmark Paper. 三位审稿人一致 Strong Accept.**

| 维度 | 分数 | 审稿人评价 |
|------|:--:|------|
| 创新性 | 5/5 | 残差学习是深度学习史上最重要的架构创新 |
| 健全性 | 5/5 | 教科书级实验设计 |
| 证据 | 5/5 | ILSVRC 2015 全赛道冠军 + 20万+ 引用 |
| 相关工作 | 5/5 | 准确定位并区分 Highway Networks |
| 可复现 | 5/5 | 开源代码 + 精确超参 |
| 重要性 | 5/5 | 启发了 Transformer、AlphaFold、GPT |

→ **[完整审稿报告 →](demo/RESNET_REVIEW.md)** ← 三智能体详细意见 + 跨审稿综合

### 三智能体架构

| 智能体 | 角色 | 审查重点 |
|--------|------|---------|
| Agent 1 | 方法论审稿人 | 技术健全性、实验设计、可复现性 |
| Agent 2 | 领域审稿人 | 创新性、SOTA 对比、贡献显著性 |
| Agent 3 | 通才审稿人 | 写作质量、可读性、格式规范 |

### 功能
- 定量评分卡（6 维 × 5 分制 = 30 总分）
- 三位智能体独立审稿意见
- 跨审稿综合（共识优势 / 风险 / 分歧）
- 引用质量审计
- LaTeX 格式检查
- 完整性审计（声称-证据对齐）
- 关注-行动表（按严重度排序）

### 安装

**Hermes Agent**
```bash
hermes skills install paper-super-reviewer
```

**Claude Code**
```bash
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/
# 使用: /claude skill load paper-super-reviewer
```

**Codex CLI**
```bash
mkdir -p ~/.codex/skills/paper-super-reviewer
cp SKILL.md ~/.codex/skills/paper-super-reviewer/
```

### 使用方式
```
审核论文: path/to/paper.tex, mode=full
```
