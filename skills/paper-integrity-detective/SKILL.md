---
name: paper-integrity-detective
description: "完整性审计智能体 — Claim提取 × 证据定位 × 数字一致性 × 数据诚实 × 虚假引用检测"
version: 4.0.0
author: TheeTarnished
license: MIT
---
# 完整性侦探 · Integrity Detective

## 工作流

### Phase 1: Claim 提取
从 Introduction + Abstract 提取所有 claimed contributions:
```
1. 搜索: "we propose", "we introduce", "our method", "we present",
         "contributes", "contributions", "novel", "first"
2. 提取每个 claim 的原文 + 位置 (§L行号)
3. 分类: method / result / application / theoretical
```

### Phase 2: Evidence 定位
对每个 claim, 在 Experiment/Results 中搜索对应证据:
```
claim_id: 1
text: "We propose method X that achieves SOTA on dataset Y"
evidence_search:
  → Table containing "method X" and "Y"
  → Figure comparing X vs baselines
  → Line stating "X outperforms"
status: verified / partial / unverified
```

### Phase 3: 数字一致性
```
对每个 Table:
  □ 每个数字与正文中引用该数字处是否一致？
  □ 同一数字在不同位置是否一致？
  □ percentage/ratio 计算是否正确？

检测模式:
  "Table 3 shows 4.2%" vs "as shown, X achieves 4.8%"
  → 数字不一致 → 标记
```

### Phase 4: 数据诚实检测
```
□ Conclusion 是否新增了 Introduction 未声称的贡献？
□ 是否存在 "SOTA" 声称但实际未超越最强 baseline？
□ 是否存在 "ghost results" (text 声称但找不到对应 table/figure)？
□ 作者贡献声明与实际内容是否一致？
□ 是否存在疑似 AI 生成的虚假引用 (格式异常 + 无法检索到)？
```

## 输出格式
```json
{
  "agent": "integrity-detective",
  "claims": {
    "total_claimed": 3,
    "verified": 2,
    "partial": 1,
    "unverified": 0,
    "new_in_conclusion": 0,
    "details": [
      {"id":1, "text":"...", "location":"§1 L45", "evidence":"Table 3 row 4", "status":"verified"},
      {"id":3, "text":"...", "location":"§1 L52", "evidence":"Table 2 contradicts", "status":"partial"}
    ]
  },
  "numerical_mismatches": [
    {"table": 3, "table_value": "4.2%", "text_value": "4.8%", "text_location": "§4 L12"}
  ],
  "data_honesty_flags": [],
  "ai_generated_reference_suspects": [],
  "verdict": "1 partial claim + 1 numerical mismatch — minor revision"
}
```

## 使用
```
检查完整性: path/to/paper.tex
```
