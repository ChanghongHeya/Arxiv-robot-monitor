# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-09 05:40 UTC
- Relevant papers: 18

| Title | Type | Authors |
|---|---|---|
| [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158) | Robot Foundation / VLA | Anqi Li, Yuxin Chen, Zhaobo Li, Zhuo Cao, Junli Ren, Masayoshi Tomizuka, Dhruv Shah |
| [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://arxiv.org/abs/2609.09155) | World Model | Yuncong Yang, Zhengtao Han, Furkan Ozyurt, Zeyuan Yang, Han Yang, Junyi Cao, Haoyu Zhen, Yilun Du, Chuang Gan |
| [Proxy Policy Steering](https://arxiv.org/abs/2609.09148) | Robot Foundation / VLA | Chuanruo Ning, Tianrui Wang, Wei-Chiu Ma, Kuan Fang |
| [DeCAL: Towards Physically-Grounded Dexterous Vision-Language-Action Models via Contact-Aware Latent Co-Imagination](https://arxiv.org/abs/2609.09119) | Robot Foundation / VLA | Yankai Fu, Ning Chen, Junkai Zhao, Heng Zhang, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang |
| [Online, Reachability-Aware, Sampling-Based Motion Planning](https://arxiv.org/abs/2609.09073) | World Model | Brendan Gould, Zhiyuan Zhang, Panagiotis Tsiotras, Samuel Coogan |
| [Model Predictive Control of Tensegrity Robots via Contact-Aware Graph Neural Dynamics Model](https://arxiv.org/abs/2609.08958) | World Model | Nelson Chen, Patrick Meng, Charles Tang, Angelina Degay, Zachary Brei, Rebecca Kramer-Bottiglio, Kostas E. Bekris, Mridul Aanjaneya |
| [VeriScene: Reconstructing Crime Scenes from Legal Evidence via World-Model Agent](https://arxiv.org/abs/2609.08342) | World Model | Kevin Chuanpu Fu, Yongsen Zheng, Zee Kin Yeong, Kwok-Yan Lam |
| [CALIPER: Clean Scenes Cannot Rank Physical Inference in Pretrained Visual Representations](https://arxiv.org/abs/2609.08250) | World Model | Aman Mehta, Riya Baviskar |
| [WorldAgen: Unified State-Action Prediction with Test-Time World Model Training](https://arxiv.org/abs/2609.08162) | Robot Foundation / VLA | Chi Wan, Kangrui Wang, Yuan Si, Pingyue Zhang, Manling Li |
| [mjorbit: A Simulation Framework for Space Robotics](https://arxiv.org/abs/2609.08010) | World Model | John Z. Zhang, Joris Verhagen, Fausto Vega, Patrick McKeen, Zachary Manchester |
| [ComVLA: Communication-Aware Split Inference for VLA Models in 6G-Connected Robotics](https://arxiv.org/abs/2609.07838) | Robot Foundation / VLA | Boliang Liu, Wint Yi Poe, Jingyun Di, Riccardo Trivisonno, Giuseppe Caire |
| [ICI-VLA: In-Context Imitation with Spatiotemporally Aligned Demonstrations for Vision-Language-Action Models](https://arxiv.org/abs/2609.07581) | Robot Foundation / VLA | Songhua Yang, Ziyu Liu, Xuetao Li, Ruqi Xiao, Kangxin Zhu, Miao Li |
| [Anti-Gravity Walking by a Flying Humanoid Robot via Thrust-Rate Input Whole-Body Model Predictive Control](https://arxiv.org/abs/2609.07544) | World Model | Kazuki Sugihara, Kei Okada |
| [PhysReal: Learning Real-World Deformable Object Physics via Hybrid Constitutive Modeling](https://arxiv.org/abs/2609.07532) | World Model | Yinan Deng, Jianqiao Song, Yisi Zhang, Yuhan Wang, Jiahui Wang, Yufeng Yue |
| [Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy](https://arxiv.org/abs/2609.07470) | Robot Foundation / VLA | Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos |
| [PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout](https://arxiv.org/abs/2609.07328) | World Model | Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv |
| [World Models Under Asynchronous Sensor Observations](https://arxiv.org/abs/2609.07299) | World Model | Akash Anand, Abhay Anand, Yash Vishe |
| [Beyond Task Success: Stage-Wise Reliability of World Model Planning under Sensing Degradation](https://arxiv.org/abs/2609.07126) | World Model | Geonmyeong Lee, Byoung-Tak Zhang |
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
