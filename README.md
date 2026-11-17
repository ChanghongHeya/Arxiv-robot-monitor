# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-11-17 08:45 UTC
- Relevant papers: 20

| Title | Type | Authors |
|---|---|---|
| [ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://arxiv.org/abs/2611.21607) | Robot Foundation / VLA | Ruixi Yu, Dairu Liu, Xuchuan Chen, Zekun Qi, Zekai Li, Zhuo Cao, Luyang Niu, Yingsheng Zhang, Sikai Liang, Ke Fan, He Wang, Li Yi |
| [Lazy-MOSAIC: Accelerating Skill-Centric Manipulation Planning with Learned Skill-Effect World Models](https://arxiv.org/abs/2611.21517) | World Model | Itamar Mishani, Mukund Krishnakumar, Oren Salzman, Maxim Likhachev |
| [Data-Driven Predictive Control for Autonomous Vehicle Racing under Varying Friction](https://arxiv.org/abs/2611.21378) | World Model | Julius Beerwerth, Julius Tischbein, Bassam Alrifaee |
| [BoBDeLaN: Bounded-Bandwidth Context Adaptation for Deep Lagrangian Robot Control](https://arxiv.org/abs/2611.21209) | World Model | Lucas Schulze, Sucheth Shenoy, Jan Peters, Oleg Arenz |
| [MetricHand: Geometry-Aware Flow Matching for 4D Hand Reconstruction in Metric World Space](https://arxiv.org/abs/2611.21060) | Robot Foundation / VLA | Yibo Bai, Likui Zhang, Jinglei Zhang, Zhengbin Pang, Xingshen Song, Xiaoqing Yin, Jinsheng Deng |
| [POKE: Probe Offline, Keep Efficiently for Vision-Language-Action Models](https://arxiv.org/abs/2611.21033) | Robot Foundation / VLA | Jaehyuk Lee, Yeajin Lee, Suhyun Bae, Donghun Lee |
| [FAVR: Flow-Aware Visual Residual Alignment for Vision-Language-Action Policies](https://arxiv.org/abs/2611.20971) | Robot Foundation / VLA | Qixuan Wu, Xiaole Yang, Yuguang Yang, Canyu Chen, Linlin Yang, Haixia Pan, Guodong Guo, Baochang Zhang |
| [Competent Autonomous Driving Through Fine Tuning Vision Language Action Models with Symbolic Traffic Rules](https://arxiv.org/abs/2611.20648) | Robot Foundation / VLA | Barkin Dagda, Vinal Asodia, Iman Sharifi, Peng Wei, Saber Fallah |
| [Instructions Before Actions: Prospective and Retrospective Language Supervision for Driving Vision-Language-Action Data](https://arxiv.org/abs/2611.20631) | Robot Foundation / VLA | Angel Martinez-Sanchez, Ross Greer |
| [JEPTERA: A Platform Agnostic JEPA-Assisted Model Predictive Planner for Urban UAV Navigation](https://arxiv.org/abs/2611.20593) | World Model | Gibran Fathoni Belva, Mansur Arief, Ahmad Alfan Alfian Irfan |
| [Lift, See, Act: Hierarchical Robot Policy Pretraining with 3D Foundation Models](https://arxiv.org/abs/2611.20481) | Robot Foundation / VLA | Yiyuan Ge, Changxing Ding, Ziyu Hao, Zijie Zheng, Xiangmin Xu |
| [ReRead: Wrong Predictions, Useful Representations - Correcting Frozen Robot Policies by Re-reading Their Own Representations](https://arxiv.org/abs/2611.20465) | Robot Foundation / VLA | Xu Su, Shunlong Xiao, Qintao Yi, Mingkuan Zhao, Xinmiao Yu, Yizhe Li, Zihan Wang, Bokui Chen |
| [Stochastic Self-Distillation for Flow-Based Vision-Language-Action Models](https://arxiv.org/abs/2611.20460) | Robot Foundation / VLA | Jingru Guo, Alessandra Russo, Joey Bose, Christos Ziakas |
| [XMimic and XSoma: Learning Humanoid Motion Tracking and Locomotion in Under a Minute](https://arxiv.org/abs/2611.20452) | World Model | Nico Bohlinger, Jan Peters |
| [NF-VLA: A Normalizing-Flow Baseline for Vision-Language-Action Learning](https://arxiv.org/abs/2611.20314) | Robot Foundation / VLA | Ruichen Deng, Qinyu Zhao, Yong-Hyun Park, Mutian Tong, Liang Zheng, Jiatao Gu |
| [Right Goal, Wrong Body: Re-grounding Frozen VLAs under Actuation Shift](https://arxiv.org/abs/2611.20244) | Robot Foundation / VLA | Umer Siddique, Peilang Li, Yongcan Cao |
| [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](https://arxiv.org/abs/2611.20107) | World Model | Yansong Qu, Zilin Huang, Zihao Sheng, Sikai Chen, Samuel Labi |
| [ReactBench-AD: Do Driving VLAs and World-Action Models React to Imminent Hazards in Their Path?](https://arxiv.org/abs/2611.20011) | Robot Foundation / VLA | Nikos Theodoridis, Reenu Mohandas, Sushil Sharma, Ciarán Hogan, Ganesh Sistu, Anthony Scanlan, Tim Brophy, Ciarán Eising |
| [PlanDiv: Test-Time Scaling with Latent Plans for Vision-Language-Action Models](https://arxiv.org/abs/2611.20010) | Robot Foundation / VLA | Hanbo Zhang, Lianlei Shan, Liuhaichen Yang, Zezhi Tang |
| [Value and Policy Calibration from Execution Feedback for Socially Compatible Driving](https://arxiv.org/abs/2611.19969) | World Model | Sen Shen, Ning Liu, Xiangrui Kong, Yingwei Li, Dongkun Han |
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
