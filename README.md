# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-04-07 03:47 UTC
- Relevant papers: 10

| Title | Type | Authors |
|---|---|---|
| [E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes](https://arxiv.org/abs/2604.04834) | Robot Foundation / VLA | Jiajun Zhai, Hao Shi, Shangwei Guo, Kailun Yang, Kaiwei Wang |
| [ROSClaw: A Hierarchical Semantic-Physical Framework for Heterogeneous Multi-Agent Collaboration](https://arxiv.org/abs/2604.04664) | Robot Foundation / VLA | Rongfeng Zhao, Xuanhao Zhang, Zhaochen Guo, Xiang Shao, Zhongpan Zhu, Bin He, Jie Chen |
| [Veo-Act: How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?](https://arxiv.org/abs/2604.04502) | Robot Foundation / VLA | Zhongru Zhang, Chenghan Yang, Qingzhou Lu, Yanjiang Guo, Jianke Zhang, Yucheng Hu, Jianyu Chen |
| [FORMULA: FORmation MPC with neUral barrier Learning for safety Assurance](https://arxiv.org/abs/2604.04409) | World Model | Qintong Xie, Weishu Zhan, Peter Chin |
| [RK-MPC: Residual Koopman Model Predictive Control for Quadruped Locomotion in Offroad Environments](https://arxiv.org/abs/2604.04221) | World Model | Sriram S. K. S. Narayanan, Umesh Vaidya |
| [DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198) | World Model | Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng |
| [Adaptive Action Chunking at Inference-time for Vision-Language-Action Models](https://arxiv.org/abs/2604.04161) | Robot Foundation / VLA | Yuanchang Liang, Xiaobo Wang, Kai Wang, Shuo Wang, Xiaojiang Peng, Haoyu Chen, David Kim Huat Chua, Prahlad Vadakkepat |
| [Adapting Neural Robot Dynamics on the Fly for Predictive Control](https://arxiv.org/abs/2604.04039) | World Model | Abdullah Altawaitan, Nikolay Atanasov |
| [Dynamic Whole-Body Dancing with Humanoid Robots -- A Model-Based Control Approach](https://arxiv.org/abs/2604.03999) | World Model | Shibowen Zhang, Jiayang Wu, Guannan Liu, Helin Zhu, Junjie Liu, Zhehan Li, Junhong Guo, Xiaokun Leng, Hangxin Liu, Jingwen Zhang, Jikai Wang, Zonghai Chen, Zhicheng He, Jiayi Wang, Yao Su |
| [VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models](https://arxiv.org/abs/2604.03956) | Robot Foundation / VLA | Ravi Ranjan, Agoritsa Polyzou |
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
