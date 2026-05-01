# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-05-01 04:45 UTC
- Relevant papers: 15

| Title | Type | Authors |
|---|---|---|
| [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/abs/2604.28196) | World Model | Xin Zhou, Dingkang Liang, Xiwu Chen, Feiyang Tan, Dingyuan Zhang, Hengshuang Zhao, Xiang Bai |
| [LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models](https://arxiv.org/abs/2604.28192) | Robot Foundation / VLA | Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng |
| [RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects](https://arxiv.org/abs/2604.28161) | World Model | Tim Missal, Lucas Domingues, Berk Guler, Simon Manschitz, Jan Peters, Paula Dornhofer Paro Costa |
| [A Pattern Language for Resilient Visual Agents](https://arxiv.org/abs/2604.28001) | Robot Foundation / VLA | Habtom Kahsay Gidey, Alexander Lenz, Alois Knoll |
| [Flying by Inference: Active Inference World Models for Adaptive UAV Swarms](https://arxiv.org/abs/2604.27935) | World Model | Kaleem Arshid, Ali Krayani, Lucio Marcenaro, David Martin Gomez, Carlo Regazzoni |
| [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792) | Robot Foundation / VLA | MotuBrain Team, Chendong Xiang, Fan Bao, Haitian Liu, Hengkai Tan, Hongzhe Bi, James Li, Jiabao Liu, Jingrui Pang, Kiro Jing, Louis Liu, Mengchen Cai, Rongxu Cui, Ruowen Zhao, Runqing Wang, Shuhe Huang, Yao Feng, Yinze Rong, Zeyuan Wang, Jun Zhu |
| [Can Tabular Foundation Models Guide Exploration in Robot Policy Learning?](https://arxiv.org/abs/2604.27667) | Robot Foundation / VLA | Buqing Ou, Frederike Dümbgen |
| [PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations](https://arxiv.org/abs/2604.27472) | Robot Foundation / VLA | Yang Zhang, Jiangyuan Zhao, Chenyou Fan, Fangzheng Yan, Tian Li, Haitong Tang, Sen Fu, Xuan'er Wu, Qizhen Weng, Weinan Zhang, Xiu Li, Chi Zhang, Chenjia Bai, Xuelong Li |
| [RAY-TOLD: Ray-Based Latent Dynamics for Dense Dynamic Obstacle Avoidance with TDMPC](https://arxiv.org/abs/2604.27450) | World Model | Seungho Han, Seokju Lee, Jeonguk Kang |
| [LA-Pose: Latent Action Pretraining Meets Pose Estimation](https://arxiv.org/abs/2604.27448) | World Model | Zhengqing Wang, Saurabh Nair, Prajwal Chidananda, Pujith Kachana, Samuel Li, Matthew Brown, Yasutaka Furukawa |
| [Judge, Then Drive: A Critic-Centric Vision Language Action Framework for Autonomous Driving](https://arxiv.org/abs/2604.27366) | Robot Foundation / VLA | Lijin Yang, Jianing Huang, Zhongzhan Huang, Shu Liu, Hao Yang |
| [STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation](https://arxiv.org/abs/2604.26848) | Robot Foundation / VLA | Yuxuan Tian, Yurun Jin, Bin Yu, Yukun Shi, Hao Wu, Chi Harold Liu, Kai Chen, Cong Huang |
| [Walk With Me: Long-Horizon Social Navigation for Human-Centric Outdoor Assistance](https://arxiv.org/abs/2604.26839) | Robot Foundation / VLA | Lingfeng Zhang, Xiaoshuai Hao, Xizhou Bu, Yingbo Tang, Hongsheng Li, Jinghui Lu, Xiu-shen Wei, Jiayi Ma, Yu Liu, Jing Zhang, Hangjun Ye, Xiaojun Liang, Long Chen, Wenbo Ding |
| [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694) | World Model | Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu |
| [AGEL-Comp: A Neuro-Symbolic Framework for Compositional Generalization in Interactive Agents](https://arxiv.org/abs/2604.26522) | World Model | Mahnoor Shahid, Hannes Rothe |
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
