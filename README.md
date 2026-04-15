# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-04-15 03:58 UTC
- Relevant papers: 14

| Title | Type | Authors |
|---|---|---|
| [Robotic Manipulation is Vision-to-Geometry Mapping ($f(v) \rightarrow G$): Vision-Geometry Backbones over Language and Video Models](https://arxiv.org/abs/2604.12908) | Robot Foundation / VLA | Zijian Song, Qichang Li, Jiawei Zhou, Zhenlong Yuan, Tianshui Chen, Liang Lin, Guangrun Wang |
| [HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models](https://arxiv.org/abs/2604.12447) | Robot Foundation / VLA | Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, Yu-Gang Jiang |
| [StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems](https://arxiv.org/abs/2604.11757) | Robot Foundation / VLA | Jinhui Ye, Ning Gao, Senqiao Yang, Jinliang Zheng, Zixuan Wang, Yuxin Chen, Pengguang Chen, Yilun Chen, Shu Liu, Jiaya Jia |
| [Grounded World Model for Semantically Generalizable Planning](https://arxiv.org/abs/2604.11751) | World Model | Quanyi Li, Lan Feng, Haonan Zhang, Wuyang Li, Letian Wang, Alexandre Alahi, Harold Soh |
| [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689) | Robot Foundation / VLA | Dujun Nie, Fengjiao Chen, Qi Lv, Jun Kuang, Xiaoyu Li, Xuezhi Cao, Xunliang Cai |
| [GeomPrompt: Geometric Prompt Learning for RGB-D Semantic Segmentation Under Missing and Degraded Depth](https://arxiv.org/abs/2604.11585) | Robot Foundation / VLA | Krishna Jaganathan, Patricio Vela |
| [DA-PTQ: Drift-Aware Post-Training Quantization for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2604.11572) | Robot Foundation / VLA | Siyuan Xu, Tianshi Wang, Fengling Li, Lei Zhu, Heng Tao Shen |
| [Dyadic Partnership(DP): A Missing Link Towards Full Autonomy in Medical Robotics](https://arxiv.org/abs/2604.11423) | Robot Foundation / VLA | Nassir Navab, Zhongliang Jiang |
| [ComSim: Building Scalable Real-World Robot Data Generation via Compositional Simulation](https://arxiv.org/abs/2604.11386) | World Model | Yiran Qin, Jiahua Ma, Li Kang, Wenzhan Li, Yihang Jiao, Xin Wen, Xiufeng Song, Heng Zhou, Jiwen Yu, Zhenfei Yin, Xihui Liu, Philip Torr, Yilun Du, Ruimao Zhang |
| [WM-DAgger: Enabling Efficient Data Aggregation for Imitation Learning with World Models](https://arxiv.org/abs/2604.11351) | World Model | Anlan Yu, Zaishu Chen, Peili Song, Zhiqing Hong, Haotian Wang, Desheng Zhang, Tian He, Yi Ding, Daqing Zhang |
| [3D-Anchored Lookahead Planning for Persistent Robotic Scene Memory via World-Model-Based MCTS](https://arxiv.org/abs/2604.11302) | World Model | Bronislav Sidik, Dror Mizrahi |
| [EmbodiedGovBench: A Benchmark for Governance, Recovery, and Upgrade Safety in Embodied Agent Systems](https://arxiv.org/abs/2604.11174) | Robot Foundation / VLA | Xue Qin, Simin Luan, John See, Cong Yang, Zhijun Li |
| [AIM: Intent-Aware Unified world action Modeling with Spatial Value Maps](https://arxiv.org/abs/2604.11135) | Robot Foundation / VLA | Liaoyuan Fan, Zetian Xu, Chen Cao, Wenyao Zhang, Mingqi Yuan, Jiayu Chen |
| [From Topology to Trajectory: LLM-Driven World Models For Supply Chain Resilience](https://arxiv.org/abs/2604.11041) | World Model | Jia Luo |
<!-- AUTO_RESULTS_END -->

这个项目会自动抓取 arXiv 最近 2 天的新论文，分析摘要，筛选出和以下方向相关的论文：

- 世界模型
- 机器人大模型
- Vision-Language-Action
- Embodied / Generalist Robot
- 基于 learned dynamics 的机器人规划 / 学习

命中结果会：

- 写入 `reports/latest_report.md`，包含中文摘要总结和筛选原因
- 把每次筛出来的标题累积记录到 `reports/title_history.json`
- 把已经发过的 arXiv id 记录到 `reports/sent_paper_ids.json`，避免下次重复发
- 每两天发送一封邮件到 `18735461194@163.com`
- 每次只发送“最近 2 天里还没发过”的论文

## 本地运行

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_monitor.py --dry-run
```

如果你希望本地直接发邮件，需要设置环境变量：

```bash
export SMTP_USERNAME="你的163邮箱"
export SMTP_PASSWORD="你的163邮箱SMTP授权码"
export OPENAI_API_KEY="可选，不填则使用规则筛选"
export EMAIL_TO="1234567788@163.com"
python run_monitor.py
```

## GitHub Actions

仓库已经带了工作流，每两天执行一次，当前 cron 是 `0 1 */2 * *`，也就是 UTC 01:00，按中国时间是上午 09:00：

- `.github/workflows/arxiv-monitor.yml`

把当前目录推到 GitHub 之后，配置以下仓库 Secrets：

- `SMTP_USERNAME`
- `SMTP_PASSWORD`
- `EMAIL_TO`
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

其中：

- `SMTP_USERNAME` 建议就是你的 163 发件箱账号
- `SMTP_PASSWORD` 不是登录密码，而是 163 邮箱的 SMTP 授权码
- `EMAIL_TO` 可以继续设置为 `18735461194@163.com`
- `OPENAI_API_KEY` 不填也能跑，只是会退化成关键词规则判断
- `OPENAI_MODEL` 可以不填，默认用 `gpt-5-mini`

## 文件说明

- `config.yaml`: 抓取、筛选、邮件和输出配置
- `run_monitor.py`: 启动入口
- `src/arxiv_monitor/arxiv_client.py`: arXiv 抓取逻辑
- `src/arxiv_monitor/analyzer.py`: 摘要分析逻辑
- `src/arxiv_monitor/emailer.py`: 邮件发送
- `reports/latest_report.md`: 最近一次报告
- `reports/title_history.json`: 历史标题归档
- `reports/sent_paper_ids.json`: 已发送 arXiv id 去重状态
