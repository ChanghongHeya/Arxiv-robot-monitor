# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-10-31 06:33 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565) | Robot Foundation / VLA | Pranjal Aggarwal, Sean Welleck |
| [BURGER: Benchmarking and Understanding Robotic Generalization via Embodied Drawing](https://arxiv.org/abs/2610.40532) | Robot Foundation / VLA | Xiangyu Xu, Bangshuai Peng, Ziyi Liu, Mengjie Zhao, Chenhao Lu, Zhengyang Fan, Huazhe Xu, Kaizhe Hu |
| [Improving Fine-Grained Manipulation through Demonstration Expansion and Execution Design](https://arxiv.org/abs/2610.40430) | Robot Foundation / VLA | Jingxu Gu, Dongze Lian |
| [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](https://arxiv.org/abs/2610.40401) | World Model | Liangyu Li, Qingwen Liu |
| [HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373) | Robot Foundation / VLA | Rongxing Ding, Hongyu Qu, Kehong Wu, Xudong Wang, Fan Zhang, Xinguang Xiang, Xiangbo Shu |
| [JEDI: Joint-Embedding Demonstration Compression for In-Context Imitation Learning](https://arxiv.org/abs/2610.40356) | Robot Foundation / VLA | Jiazhao Liang, Zhewen He, Shuaihang Yuan, Hao Huang, Yi Fang |
| [TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation](https://arxiv.org/abs/2610.40349) | Robot Foundation / VLA | Haozhe Zhang, Gu Zhang, Zirui Zou, Yuzheng Chen, Jinlong Wu, Zixuan Hu, Jianke Zhang, Yucheng Hu, Zhecheng Yuan, Huazhe Xu |
| [Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339) | World Model | Yuzhe Wu, Zijun Lin, Yeying Jin |
| [Learning Safe Flow Matching Robot Policies from Binary Feasibility Oracles](https://arxiv.org/abs/2610.40075) | Robot Foundation / VLA | Jianming Ma, Rongjun Jin, Yizhi Chen, Yue Gao |
| [RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence](https://arxiv.org/abs/2610.40026) | Robot Foundation / VLA | Xin Ma, Furong Chen, Xinlong Man, Bo Zhang, Yalong Guo, Haolan Lei, Chaochen Cui, Hongyuan Zhang, Mulin Chen, Yi Wang, Lap-pui Chau, Chuang Yang |
| [LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks](https://arxiv.org/abs/2610.40016) | Robot Foundation / VLA | Enqiao Lu, Yuxiang Xie, Xingrui Yu, Yuyang Wang, Yipeng Gu, Zhenglin Wan, Pengfei Zhou, Wangbo Zhao, Yang You, Yuxiang Gao, Ivor Tsang |
| [How Much Should a VLA Trust Its Reasoning? Step-Level Guidance as a Measured Action-Value Function](https://arxiv.org/abs/2610.40002) | Robot Foundation / VLA | Dabin Seo, Eunhyek Joa |
| [Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay](https://arxiv.org/abs/2610.39775) | Robot Foundation / VLA | Kristian Ceder, Kilian Freitag, Knut Åkesson |
| [WorldProbe: When Video World Models Fall Apart under Long-Horizon Spatial Exploration](https://arxiv.org/abs/2610.39721) | World Model | Minqi Wang, Jie Peng, Hejun Dong, Ruchang Yao, Puyi Wang, Siyuan Huang, Jihai Zhang, Yafu Li, Qi Dou, Xiaoye Qu, Yu Cheng |
| [From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2610.39543) | Robot Foundation / VLA | Yixue Zhang, Wenke Xia, Kun Wu, Wenbo Yu, Pei Ren, Junnan Nie, Di Hu, Zhengping Che, Chang Liu |
| [PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528) | Robot Foundation / VLA | Huabin Peng, Fagang Jin, Yancong Wei, Tengfei Ma, Chuhang Liu, Chao Yu, Liqing Chen |
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
