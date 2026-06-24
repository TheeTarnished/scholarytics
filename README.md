# Paper Super Reviewer

端到端学术论文超审系统 — Hermes Agent Skill。

## 架构

三智能体并行审稿 + 跨审稿综合：

| Agent | 角色 | 职责 |
|-------|------|------|
| Agent 1 | 方法论审稿人 | 技术健全性、实验设计、可复现性 |
| Agent 2 | 领域审稿人 | 创新性、SOTA对比、贡献显著性 |
| Agent 3 | 通才审稿人 | 写作质量、可读性、格式规范 |

## 功能

- 定量评分卡 (6维 × 5分制)
- 三智能体独立审稿意见
- 跨审稿综合 (共识优势/风险/分歧)
- 引用质量审计
- LaTeX 格式检查
- 完整性审计 (claim-evidence)
- 关注-行动表 (按严重度排序)

## 使用

加载 skill 后提供论文路径和审核模式：

```
审核论文: path/to/paper.tex, mode=full
```

## 安装

将 `SKILL.md` 放入 Hermes Agent 的 skills 目录：

```
~/.hermes/skills/research/paper-super-reviewer/
```

或通过 Hermes Hub 安装：

```
hermes skills install paper-super-reviewer
```
