# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-08-21 02:20 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111) | Robot Foundation / VLA | Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li, Yunjian Li, Lishengsa Yue, Zhiyong Cui, Chengzhong Xu, Zhenning Li |
| [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](https://arxiv.org/abs/2608.19964) | Robot Foundation / VLA | Bhavya Gupta, Onat Gungor, Tajana Rosing |
| [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891) | Robot Foundation / VLA | Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch, Markus Wulfmeier, Abbas Abdolmaleki, Martin Riedmiller |
| [An Irreducible Quantum Advantage in Aligning World Models with Reality](https://arxiv.org/abs/2608.19779) | World Model | Josep Lumbreras, Hailan Ma, Jayne Thompson, Mile Gu |
| [World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms](https://arxiv.org/abs/2608.19661) | Robot Foundation / VLA | Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot |
| [OrthoSkillVLA: Continual Skill Learning via Gradient-Informed Skill Subspace Adaptation](https://arxiv.org/abs/2608.19589) | Robot Foundation / VLA | Jiaqi Wang, Zhou Fang, Qiongfeng Shi, Yi Zhou |
| [Fine-Tuning VLAs with Self-Demonstrated Generative Control for Multi-Task Manipulation](https://arxiv.org/abs/2608.19490) | Robot Foundation / VLA | Prachi Garg, Steve Xing, Prahit Yaugand, Saurabh Gupta, Derek Hoiem |
| [Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control](https://arxiv.org/abs/2608.19443) | World Model | Chaoyi Pan, Zeji Yi, John Zhang, Zachary Manchester, Guannan Qu, Guanya Shi |
| [Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control](https://arxiv.org/abs/2608.19375) | World Model | Harry Zhang, Dan Negrut |
| [DA-WAM: Decision-Aligned Future Latents for Driving World Models](https://arxiv.org/abs/2608.19085) | World Model | Ruiguo Zhong, Benshan Ma, Xiaolong Chen, Lang Zhang, Mingyue Feng, Yaonong Wang, Pei Liu, Jun Ma |
| [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](https://arxiv.org/abs/2608.19066) | Robot Foundation / VLA | Yechan Park, HyunJin Kim |
| [Decision-Metric Alignment in Latent World Models: Diagnostics and Action-Conditioned Objectives for MPC Planning](https://arxiv.org/abs/2608.18746) | World Model | Jiawei Wang, Ke Rui, Yushen Zuo, Yichun Feng, Minglei Li |
| [Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI](https://arxiv.org/abs/2608.18671) | Robot Foundation / VLA | Mohammad Zamani, Fatemeh Ziaeetabar |
| [Reinforced Planning with Latent World Models](https://arxiv.org/abs/2608.18669) | World Model | Armin Sommer, Jannik Schilling |
| [Progressive Experience Fusion for Multi-Task World Model Control in Endovascular Navigation](https://arxiv.org/abs/2608.18647) | World Model | Harry Robertshaw, Maxence Boels, Nikola Fischer, Sebastien Ourselin, Christos Bergeles, Alejandro Granados, Thomas C Booth |
| [Real-Time Control-Constrained DDP for Underactuated Balancing of Legged Robots](https://arxiv.org/abs/2608.18552) | World Model | SeongWon Nam, Hyunyong Lee, Hansol Kang, Jiman Park, Yeongwoo Son, Bumsu Yi, Jaeyoung Oh, Hyouk Ryeol Choi |
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
