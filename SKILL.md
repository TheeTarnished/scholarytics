---
name: paper-super-reviewer
description: "集成 CCFA-Skills + Nature-Skills + PaperSpine 三大论文审核体系，提供从科学创新性、技术健全性、写作逻辑、格式规范到完整性审计的全方位论文审核。覆盖定量评分卡、3位模拟审稿人、跨审稿综合、关注-行动表、引用质量审计、LaTeX检查。"
version: 2.0.0
author: Zhenhao Li
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paper-review, academic, peer-review, latex-audit, multi-reviewer]
    category: research
    homepage: https://github.com/user/paper-super-reviewer
    integrates:
      - "CCFA-Skills (mikubaka88/CCFA-Skills): ccf-paper-reviewer — 定量评分、审稿人面板、AC/meta-review、关注-行动表"
      - "Nature-Skills (Yuan1z0825/nature-skills): nature-reviewer — 3审稿人+跨审稿综合、Nature风格评审轴"
      - "PaperSpine (WUBING2023/PaperSpine): paper-spine-audit — 完整性审计、claim支撑检查、结构化多智能体审稿、LaTeX守卫"
---

# Paper Super Reviewer — 论文超审

集成三大论文审核体系的端到端论文质量审核工具。模拟真实学术评审流程，输出结构化审稿报告。

## 三大来源

| 来源 | 核心能力 | 上游仓库 |
|------|---------|---------|
| **CCFA-Skills** | 量化评分卡（1-5分）、3审稿人面板、AC/meta-review、关注-行动表、写作/格式审核 | mikubaka88/CCFA-Skills |
| **Nature-Skills** | 3审稿人+跨审稿综合、Nature评审轴（原创性/重要性/跨学科/健全性/可读性） | Yuan1z0825/nature-skills |
| **PaperSpine** | 完整性审计、Claim支撑检查、3-agent并行审稿、引用质量审计、LaTeX守卫 | WUBING2023/PaperSpine |

## 使用方式

加载 skill 后，提供论文文件（.tex / .pdf / .md），指定审核模式即可：

```
审核这篇论文: path/to/paper.tex
模式: full
```

### 审核模式

| 模式 | 覆盖内容 | 耗时 |
|------|---------|:--:|
| `scientific` | 科学创新性、技术健全性、实验证据、相关工作、可复现性、评分 | 中 |
| `writing` | 段落逻辑、章节流、贡献展示、claim-evidence、术语一致性、图表叙述 | 快 |
| `format` | LaTeX格式、引用完整性、图表质量、页面限制、盲审匿名性 | 快 |
| `full` | 以上全部 + 完整性审计 + 3审稿人面板 + 跨审稿综合 | 慢 |

## 完整工作流

### 1. 输入识别
- 确定审核模式、目标会议/期刊、年份、track
- 识别输入文件（.tex、.pdf、.md、补充材料）
- 标记缺失材料

### 2. 论文摘要提取
- 提取摘要、声称贡献、证据包、主要声称、局限
- 建立 shared manuscript fact base（供3审稿人共享基础事实）

### 3. 科学审核 (scientific/full)
按以下维度评估：

**CCFA 评分维度 (1-5分制)：**

| 维度 | 评估内容 |
|------|---------|
| Novelty (创新性) | 与SOTA的差异程度、方法原创性 |
| Soundness (健全性) | 方法论正确性、实验设计严谨性 |
| Evidence (证据) | 实验充分性、统计显著性、消融完整性 |
| Related Work (相关工作) | 覆盖度、定位准确性、缺失关键基线 |
| Reproducibility (可复现性) | 代码可用性、数据可获取性、超参完整 |
| Significance (重要性) | 对领域的潜在影响、实用价值 |

**Nature 评估轴：**
- Originality: 是否真正新颖
- Scientific Importance: 对学科的重要性
- Interdisciplinary Readership: 跨学科吸引力
- Technical Soundness: 技术健全性
- Readability for Nonspecialists: 非专家可读性

### 4. 写作审核 (writing/full)
- **段落逻辑流**: 每段是否有清晰的 topic sentence → evidence → transition
- **贡献展示**: Introduction 是否清晰列出贡献
- **Claim-evidence 一致性**: 每个声称是否有证据支撑
- **术语一致性**: 关键术语是否全文统一
- **图表叙述**: 图表是否在正文中被充分讨论
- **摘要质量**: 是否覆盖 motivation→method→results→implication

### 5. 格式审核 (format/full)
- LaTeX 编译检查（pdflatex 三遍，0 errors）
- 引用完整性：所有 `\cite` 是否在 `.bib` 中，无未引用参考文献
- 图表分辨率、清晰度
- 页面/字数限制
- 盲审匿名性
- 公式编号和引用
- ACM/CCF 元数据完整性

### 6. 三审稿人面板
生成3位独立审稿人意见，共享事实基础，不同侧重：

- **Reviewer 1 (方法论专家)**: 侧重技术健全性、实验设计、消融严谨性
- **Reviewer 2 (领域专家)**: 侧重创新性、与SOTA对比、贡献显著性
- **Reviewer 3 (通才审稿人)**: 侧重可读性、写作质量、跨学科吸引力

### 7. 跨审稿综合
- 共识优势 — 三位审稿人均认可的强项
- 共识技术风险 — 三位审稿人均关注的问题
- 审稿人间侧重差异 — 意见分歧点
- 最需解决的关键问题 — 按优先级排序

### 8. AC/meta-review 与量化评分
- 每维度 1-5 分，附扣分理由和修复条件
- 任何 ≤3 分的维度必须有具体扣分和修复条件
- 总分 + 置信度
- 建议决定：Accept / Weak Accept / Borderline / Weak Reject / Reject

### 9. 引用质量审计
- 引用数量是否充足（short paper ≥10, full paper ≥20）
- 时效性（近3年引用占比）
- 每篇引用是否在正文中被实质性讨论（非"also works on X"堆砌）
- 是否存在未引用但已在参考文献中的条目
- 会议/期刊名称和年份是否正确

### 10. 完整性审计 (PaperSpine)
- 所有声称是否有证据支撑
- 图表-正文一致性（table中的数据 = text中的数字）
- 跨章节一致性（introduction的声称 = conclusion的总结）
- 数字一致性（table vs text vs source data）

### 11. 关注-行动表
每个关注点格式：

| # | Severity | Criterion | Evidence | Fix Class | Score Impact |
|---|----------|-----------|----------|-----------|:-----------:|
| 1 | Fatal | claim-evidence gap | 23 models claimed, 6 tested | 需要新实验 | +4 pts |

**严重度定义：**
- **Fatal**: 不修复则论文不可接受
- **Major**: 严重影响评分，必须修复
- **Moderate**: 应修复，但不致命
- **Minor**: 建议修复，不影响决定

**修复类别：**
- 需要新实验 / 需要重写 / 需要澄清 / 格式修复

## 输出格式 (full mode)

```markdown
# Paper Super Review Report
## Review Setup
## Paper Summary
## Quantitative Scorecard
## Reviewer Panel (3 reviewers)
## Cross-Review Synthesis
## Writing & Presentation Audit
## Format & LaTeX Audit
## Reference Quality Audit
## Integrity Audit
## Concern-to-Action Table
## AC / Meta-Review
```

## 红线和禁止事项

- ❌ 不编造审稿人身份、机构、专业
- ❌ 不编造实验、验证、引用、图表细节
- ❌ 不编造分数变化、接受概率、缺失相关工作
- ❌ 不将审稿转为作者 rebuttal 撰写
- ❌ 不以编辑决定信形式呈现
- ❌ 不声称论文"一定"属于某会议/期刊
- ❌ 不省略技术缺陷（当证据不足时）
- ❌ 不强制审稿人间一致或矛盾；分歧必须来自实际证据

## 注意事项

- 审稿报告应**诚实透明**：如果论文有严重缺陷，直接指出
- 评分应当**严格但有建设性**：每个扣分都附带明确的修复路径
- 引用审计是**客观检查**：不编造"缺失的引用"
- LaTeX检查应运行**实际编译**，不靠肉眼推测
- 审稿人面板的不同意见是**正常现象**，不必强行调和

## 参考来源

本 skill 整合自以下仓库：
- CCFA-Skills `ccf-paper-reviewer`: mikubaka88/CCFA-Skills
- Nature-Skills `nature-reviewer`: Yuan1z0825/nature-skills
- PaperSpine `paper-spine-audit`: WUBING2023/PaperSpine
