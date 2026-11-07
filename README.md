# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-11-07 06:46 UTC
- Relevant papers: 13

| Title | Type | Authors |
|---|---|---|
| [OopsieRecover: Learning Transferable VLA Corrections from Semantic Interventions](https://arxiv.org/abs/2611.08462) | Robot Foundation / VLA | Arpit Bahety, Skand Peri, Sriniket Ambatipudi, Chen Xu, Haruki Nishimura, Masha Itkina, Roberto Martín-Martín |
| [Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing](https://arxiv.org/abs/2611.08425) | Robot Foundation / VLA | Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva, Olin Goudey, Neel P. Bhatt, Matthias Scheutz, Ufuk Topcu |
| [T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust VLA Models](https://arxiv.org/abs/2611.08413) | Robot Foundation / VLA | Mohammed Hassan, Zhenyang Chen, Zheng Wang, Zhixin Zhu, Tianlong Chen, Yingyan, Lin, Chaojian Li |
| [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://arxiv.org/abs/2611.08373) | Robot Foundation / VLA | Fuhao Li, Wenxuan Song, Qizhou Huang, Ziyang Zhou, Jingbo Wang, Junwu E, Pengwei Wang, Yan Wang, Shunbo Zhou, Haoang Li |
| [GPWM: Modeling the World as 3D Particle Motion](https://arxiv.org/abs/2611.08338) | World Model | Robert Ren, Matthew Bronars, He Zhu, Yikai Tang, Jianing Zhang, Sergey Zakharov, Pavel Tokmakov, Katerina Fragkiadaki |
| [La-JEPA: Compact Robot Policies with Latent World Modeling](https://arxiv.org/abs/2611.08156) | Robot Foundation / VLA | Mateo Clémente, George Z. Xue, Amin Abyaneh, Liheng Ma, Rui Heng Yang, Tongtong Cao, Zhanguang Zhang, Yingxue Zhang |
| [FreeOcc: Decoupling Ego-Motion for Efficient 4D Occupancy Forecasting via Continuous Flow Matching](https://arxiv.org/abs/2611.08128) | World Model | Zeping Zhang, Zhuoya Zhao, Samy Metari, Robert Laganière |
| [WAM-Sim0.1: World Anchored Memory Meets Online RL for Consistent and Realistic Driving Simulation](https://arxiv.org/abs/2611.07939) | World Model | Jiahao Cui, Jiaye Li, Wenhao Zhang, Yaoyi Li, Shan Luan, Quanhui Tang, Jianhua Han, Lin Cheng, Hang Xu, Siyu Zhu |
| [GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912) | World Model | Xiyan Su, Finn Rasmus Schäfer, Hojun Lim, Frank Diermeyer, Johannes Betz, Markus Lienkamp |
| [PVDepth: Panoramic Video Depth Estimation via Geometry-Aware Spatiotemporal Adaptation](https://arxiv.org/abs/2611.07873) | World Model | Chuanxin Song, Peixi Peng |
| [Learning Robotic World Models with Semantic and Visual Feedback](https://arxiv.org/abs/2611.07850) | Robot Foundation / VLA | Hao Wu, Yuqi Li, Yizhou Zhao, Kun Wang, Xiao Luo, Yu Cheng, Bo An, Yingli Tian, Laszlo A. Jeni, Ming-Hsuan Yang |
| [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730) | World Model | Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim, Hanyoung Jang, HyeongYeop Kang |
| [AffectiveVLA: Safe and Intent-Aware VLA Control for Human-Humanoid Social Interaction](https://arxiv.org/abs/2611.07712) | Robot Foundation / VLA | Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina, Yara Mahmoud, Iana Zhura, Miguel Altamirano Cabrera, Dzmitry Tsetserukou |
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
