---
name: paper-quick-scan
description: "5分钟论文快速扫描 — 提取核心画像：贡献类型、方法快照、关键数字、红/绿旗、预估评分"
version: 4.0.0
author: TheeTarnished
license: MIT
---
# 快速扫描 · Quick Scan

5 分钟生成论文一页纸画像。投稿前自查或批量筛选。

## 工作流

### Step 1: 提取元信息 (30s)
```
- 标题、作者、机构、年份
- 会议/期刊 (如有)
- 页数、图表数、引用数
```

### Step 2: 贡献类型分类 (30s)
```
方法创新 / 理论分析 / 应用系统 / Benchmark / 综述
```

### Step 3: 方法快照 (1min)
```
一句话总结方法: "用 [X] 解决 [Y] 问题，关键创新是 [Z]"
```

### Step 4: 关键数字 (1min)
```
- 最重要的一个数字 (Table 1 或 Abstract)
- 对比 strongest baseline 的提升
- 数据集规模
- 参数量/训练时间
```

### Step 5: 风险标记 (2min)
```
红旗 🔴: 无消融 / 不报告 seed / 无代码 / 样本<1000 / 无SOTA对比 / 单seed
绿旗 🟢: 开源 / 多seed / 大规模实验 / strong baselines / 诚实讨论局限
```

### Step 6: 预估评分
```
基于红/绿旗和关键数字，预估 CCF 6维评分 (1-5)
+ 建议: 投稿 / 修改后投稿 / 不建议投稿
```

## 输出格式
```json
{
  "title": "...",
  "authors": "...",
  "contribution_type": "method",
  "method_snapshot": "用 Kronos 基础模型解决 E2E 股票预测，关键创新是零特征工程 + TPE 贝叶斯优化",
  "key_result": {"metric": "Rank IC", "value": 0.185, "baseline": -0.055},
  "data_scale": {"samples": 2146, "stocks": 10},
  "red_flags": ["单seed", "无GPU实验", "样本<5000"],
  "green_flags": ["开源代码", "贝叶斯HPO", "明确局限讨论"],
  "estimated_ccf_score": 18,
  "recommendation": "修改后投稿 — 补GPU实验 + 多seed后可达24+"
}
```

## 使用
```
快速扫描: path/to/paper.pdf
```
