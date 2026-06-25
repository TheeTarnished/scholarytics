# paper-super-reviewer · Skill 生成日志

## 2026-06-25 | v3.0 架构

每个 skill 是一个独立的审查智能体，可单独调用也可通过主 skill 编排。

```
skills/
├── paper-super-reviewer/     # 主编排器 — 调用所有子 skill
├── paper-methodology-reviewer/  # Agent 1: 方法论仲裁者
├── paper-domain-reviewer/       # Agent 2: 领域导航者
├── paper-narrative-editor/      # Agent 3: 叙事编辑者
├── paper-format-guardian/       # Agent 4: 格式守卫者
├── paper-reference-auditor/     # Agent 5: 引用审计者
├── paper-integrity-detective/   # Agent 6: 完整性侦探
├── paper-quick-scan/            # 快速扫描 (5 min)
├── paper-latex-check/           # LaTeX 专项检查
├── paper-citation-check/        # 引用专项检查
├── paper-claim-tracker/         # 声称-证据追踪
└── paper-venue-matcher/         # 会议/期刊匹配
```

每个 skill 独立运行，输出结构化 JSON + Markdown。
skill 生成完全透明——每个智能体的 prompt、审查清单、输出格式均可见。
