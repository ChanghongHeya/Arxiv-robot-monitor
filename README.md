# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-19 05:26 UTC
- Relevant papers: 15

| Title | Type | Authors |
|---|---|---|
| [GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies](https://arxiv.org/abs/2609.20776) | Robot Foundation / VLA | Xin Chen, Sen Chen, Yujuan Ding, Jian Liu, Guoqing Wang, Wei Ye, Heng Tao Shen, Yi Bin |
| [MoWAM: Explicit Future Motion Prediction for Efficient World Action Models](https://arxiv.org/abs/2609.20709) | World Model | Jiayu Wang, Bin Zhu, Yue Yu, Jingjing Chen |
| [HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface](https://arxiv.org/abs/2609.20659) | Robot Foundation / VLA | Zimu Han, Yiming Zeng, Jiyao Zhang, Zihao Zhao, Yuanfei Wang, Yixiang Jin, Shiqi Li, Shuangben Chen, Wei Huang, Ruodai Li, Hui Shen, Hao Dong |
| [DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation](https://arxiv.org/abs/2609.20649) | World Model | Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu |
| [SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation](https://arxiv.org/abs/2609.20648) | Robot Foundation / VLA | Kaivalya Agrawal, Md Ashiqur Rahman, Raymond A. Yeh, Zachary Kingston |
| [TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces](https://arxiv.org/abs/2609.20646) | Robot Foundation / VLA | Jiaxuan Zhang, Ruizhe Liu, Yu Zhang, Yanchao Yang |
| [Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control](https://arxiv.org/abs/2609.20575) | World Model | Yilang Liu, Haoxiang You, Qian Wang, Daniel Rakita, Ian Abraham |
| [DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion](https://arxiv.org/abs/2609.20035) | World Model | Run Wang, Alapati Tuerxun, Shuo Liu, Wei Xiao, Ján Drgoňa, Yilin Mo, Liang Wu |
| [Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034) | World Model | Xin Zhou, Cong Miao |
| [Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation](https://arxiv.org/abs/2609.19976) | Robot Foundation / VLA | Harsha Guda, Adrià Colomé, Carme Torras |
| [Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models](https://arxiv.org/abs/2609.19923) | Robot Foundation / VLA | Haolong Li, Guner Dilsad Er, Michael Muehlebach, Joerg Stueckler |
| [Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning](https://arxiv.org/abs/2609.19878) | Robot Foundation / VLA | Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Yian Ma, Lianhui Qin |
| [Feeling Terrain Before Crossing: World Models for Off-Road Navigation](https://arxiv.org/abs/2609.19863) | World Model | E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo |
| [Improving Cross-embodiment Transfer in Latent Action Models with Action-Similarity Supervision](https://arxiv.org/abs/2609.19846) | Robot Foundation / VLA | Maxime Alvarez, Renzo Caballero, Tatsuya Matsushima, Yusuke Iwasawa, Yutaka Matsuo |
| [AI Smart Glasses for Wearable Intelligence: From Egocentric Sensing to Agentic Personalization](https://arxiv.org/abs/2609.19793) | Robot Foundation / VLA | Xu Yuan, Yi Wang, Zhuohang Jiang, Haohao Qu, Yujuan Ding, Shanru Lin, Guoliang Xing, Hongxia Yang, Jiannong Cao, Qing Li, Wenqi Fan |
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
