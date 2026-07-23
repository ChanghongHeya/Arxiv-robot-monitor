# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-07-23 04:11 UTC
- Relevant papers: 15

| Title | Type | Authors |
|---|---|---|
| [Distributed Motion Planning with Safety Guarantees for Self-Reconfiguring Robotic Boats](https://arxiv.org/abs/2607.20352) | World Model | Alejandro Gonzalez-Garcia, Wei Wang, Wei Xiao, Wilm Decre, Jan Swevers, Carlo Ratti, Daniela Rus |
| [Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids](https://arxiv.org/abs/2607.20345) | Robot Foundation / VLA | Roger Sala Sisó, Tiago Silvério, Jakob Sand, Tran Nguyen Le |
| [ReferTrack: Referring Then Tracking for Embodied Visual Tracking](https://arxiv.org/abs/2607.20061) | Robot Foundation / VLA | Hanjing Ye, Tianle Zeng, Jiazhao Zhang, Shaoan Wang, Zibo Zhang, Weisi Situ, Yuchen Zhou, Yonggen Ling, Hong Zhang |
| [LAVIFT: Latent-Action-Guided Vision Fine-Tuning for Surgical Interaction Recognition](https://arxiv.org/abs/2607.19889) | World Model | Jiajun Cheng, Subarna Tripathi, Sainan Liu, Xiaofan Yu, Shan Lin |
| [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876) | Robot Foundation / VLA | Zeyu Liu, Zhangzhe Zhu, Yang Zhang, Chenyou Fan, Chenjia Bai, Xuelong Li |
| [Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning](https://arxiv.org/abs/2607.19809) | World Model | Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi |
| [Koopman Dreamer: Spectrally Constrained Latent Dynamics for Stable World-Model Imagination](https://arxiv.org/abs/2607.19719) | World Model | Jiaqi Li, Xinglong Zhang, Haibin Xie, Yixing Lan, Wei Pan, Xin Xu |
| [LENS: LLM-guided Environment Simplification for Planning and Control in Clutter](https://arxiv.org/abs/2607.19633) | Robot Foundation / VLA | Aileen Liao, Rachel Holladay, Dinesh Jayaraman, Michael Posa |
| [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) | World Model | Hadi Alzayer, Wenlong Huang, Haonan Chen, Christopher Luey, Lvmin Zhang, Maneesh Agrawala, Gordon Wetzstein, Li Fei-Fei, Yilun Du, Jiajun Wu, Jia-Bin Huang |
| [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190) | Robot Foundation / VLA | Guanxiong Chen, Qianjun Xia, Jiawei Peng, Heng Zhang, Bole Ma, Justin Qian, Ziyi Jiao, Bingyang Zhou, Luoxin Ye, Kaifeng Zhang, Kunyi Wang, Weijia Zeng, Yunuo Chen, Pengzhi Yang, Ziqiu Zeng, Huamin Wang, Chao Liu, Alan Yuille, Fan Shi, Changxi Zheng, Yunzhu Li, Chenfanfu Jiang, Peter Yichen Chen |
| [NaviAIS: A Scenario-Level Vessel Trajectory Prediction Dataset withVectorized Lane Priors and the NaviLane Forecasting Framework](https://arxiv.org/abs/2607.18887) | Robot Foundation / VLA | Yuan Gui, Hongchen Luo, Liqi Qu, Longyue Fu, Jiao Wang |
| [Koopman DCM: Unstable Eigenfunctions as Data-driven Representations for Legged Balancing](https://arxiv.org/abs/2607.18760) | World Model | Stéphane Caron |
| [DWM: Separating World Effects from Actions in Latent World Models](https://arxiv.org/abs/2607.18715) | World Model | Yi-Ge Zhang, Tianqi Du, Qi Zhang, Yisen Wang |
| [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](https://arxiv.org/abs/2607.18709) | Robot Foundation / VLA | Ziqin Wang, Hao Li, Weijun Wang, Junhao Cai, Jia Zeng, Yilun Chen, Jiangmiao Pang, Si Liu |
| [Do AI-Native Biotechs Need Departments? Benchmarking Company World Models for AI-Driven Drug Development](https://arxiv.org/abs/2607.18696) | World Model | Yinan Wang |
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
