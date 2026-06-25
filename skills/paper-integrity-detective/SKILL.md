---
name: paper-integrity-detective
description: "论文完整性审稿智能体 — 声称-证据逐条对比 + 数据一致性检查"
version: 1.0.0
author: TheeTarnished
license: MIT
---
# 完整性侦探 · Integrity Detective
声称-证据对齐 + 数字一致性验证。
## 审查清单 (10 项)
1. Introduction claimed 在实验部分有对应？
2. Table 数字与正文数字一致？
3. 图表标题与正文描述一致？
4. 数据 cherry-picking？
5. "SOTA"确实超越所有已知方法？
6. "ghost results"(声称未展示)？
7. 统计声明有对应检验？
8. Conclusion 新加了 Introduction 没有的贡献？
9. 作者贡献声明与内容一致？
10. 疑似 AI 生成的虚假引用？

## 输出格式
```json
{"agent":"integrity-detective",
 "claims":{"claimed":3,"verified":2,"unverified":1},
 "numerical_mismatches":[{"table":3,"text_l12":"4.2%","table":"4.8%"}],
 "verdict":"1 unverified claim + 1 numerical mismatch"}
```
## 使用
```
检查完整性: path/to/paper.tex
```
