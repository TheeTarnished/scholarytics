---
name: paper-format-guardian
description: "LaTeX 格式审计智能体 — 3遍编译 × 全部warning分析 × 精确修复代码生成"
version: 4.0.0
author: TheeTarnished
license: MIT
---
# 格式守卫者 · Format Guardian

真正的 LaTeX 审计——不只是列出 warning，而是运行 pdflatex 三遍，解析每个 warning，生成精确的修复代码。

## 工作流

### Phase 1: 编译审计
```bash
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

解析 .log 文件，分类所有 warning：

| Warning 类型 | 严重度 | 说明 |
|-------------|:----:|------|
| `Overfull \hbox` | minor | 文字溢出，通常需要断词或 rephrase |
| `Underfull \hbox` | minor | 文字稀疏，通常可忽略 |
| `Citation undefined` | **fatal** | \cite 的 key 不在 .bib 中 |
| `Reference undefined` | **fatal** | \ref 的 label 不存在 |
| `Font shape undefined` | major | 字体缺失，PDF 显示异常 |
| `Rerun to get cross-references right` | info | 需要再次编译（正常） |
| `No file *.aux` | info | 首次编译（正常） |

### Phase 2: 引用完整性
```
解析 .aux 文件:
  \citation{key} → text 中所有 \cite
  \bibcite{key}  → .bib 中所有条目

检查:
  □ text 中引用但 .bib 中缺失
  □ .bib 中条目但 text 中未引用 (orphaned)
  □ \cite 但无实质性讨论 (token cite)
```

### Phase 3: 格式合规
```
□ 页数/字数是否符合 venue 要求？
  - CVPR: 8 pages + references
  - NeurIPS: 9 pages
  - ICML: 8 pages + appendix
  - ACL: 8 pages + references

□ 图表分辨率:
  - 矢量图 (PDF/EPS): OK
  - 位图 (PNG/JPG): 检查实际像素 vs 渲染尺寸

□ 盲审匿名:
  - 搜索 "our previous work" → 应改为 "prior work"
  - 搜索作者名 → 不应出现
  - 搜索机构名 → 不应出现
  - PDF metadata 是否包含作者信息

□ 公式质量:
  - 所有 \ref{eq:*} 是否解析
  - 公式是否溢出
  - 是否有未编号但被引用的公式
```

### Phase 4: 表格审计
```
对每个 table 环境:
  □ 是否溢出页面/栏宽？
  □ caption 是否在 table 上方？
  □ 是否有 \label？
  □ 是否在正文中被 \ref 引用？
  □ 表格内数据是否有 NA/NaN？
```

## 输出格式

```json
{
  "agent": "format-guardian",
  "compilation": {
    "errors": 0,
    "warnings": 12,
    "warning_breakdown": {
      "overfull_hbox": 8,
      "citation_undefined": 0,
      "reference_undefined": 2,
      "font_warnings": 2
    }
  },
  "reference_integrity": {
    "citations_in_text": 35,
    "entries_in_bib": 37,
    "undefined_citations": [],
    "orphaned_entries": ["hochreiter1997long", "cho2014learning"]
  },
  "venue_compliance": {
    "venue": "ACML",
    "page_limit": 8,
    "actual_pages": 4,
    "compliant": true
  },
  "blind_review_issues": [],
  "table_issues": [
    {"table": 1, "issue": "overflows column by 3.2mm", "fix": "\\resizebox{\\columnwidth}{!}{...}"}
  ],
  "verdict": "Minor — 2 undefined refs + 1 table overflow"
}
```

## 使用

```
检查格式: path/to/paper.tex
```
