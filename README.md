# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-05-21 05:06 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs](https://arxiv.org/abs/2605.21446) | Robot Foundation / VLA | Abhinaw Priyadershi, Jelena Frtunikj |
| [PointACT: Vision-Language-Action Models with Multi-Scale Point-Action Interaction](https://arxiv.org/abs/2605.21414) | Robot Foundation / VLA | Shizhe Chen, Paul Pacaud, Cordelia Schmid |
| [A Terrain-Adaptive epsilon-Constraint MPC for Uneven Terrain Kinodynamic Planning](https://arxiv.org/abs/2605.21188) | World Model | Otobong Jerome, Geesara Kalathunga, Tiago Nascimento |
| [Distill to Think, Foresee to Act: Cognitive-Physical Reinforcement Learning for Autonomous Driving](https://arxiv.org/abs/2605.21139) | World Model | Yang Wu, Qiang Meng, Zhaojiang Liu, Youquan Liu, Jian Yang, Jin Xie |
| [Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation](https://arxiv.org/abs/2605.20811) | World Model | Jingyang He, Guangrun Li, Jieyu Zhang, Chengkai Hou, Zhengping Che, Shanghang Zhang |
| [VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models](https://arxiv.org/abs/2605.20774) | Robot Foundation / VLA | Alex S. Huang, Jiahui Zhang, Shiqing Tang, Yu Xiang |
| [GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation](https://arxiv.org/abs/2605.20752) | Robot Foundation / VLA | Zijian Zhang, Yuqing Jiang, Qian Cheng, Si Liu, Ding Zhao, Ping Luo, Weitao Zhou, Haibao Yu |
| [VBT-MPC: Vision-Based Tactile MPC for Contour Following](https://arxiv.org/abs/2605.20392) | World Model | Edison Velasco-Sanchez, Luis F. Recalde, Guanrui Li, Pablo Gil |
| [Beyond Binary Success: A Diagnostic Meta-Evaluation Framework for Fine-Grained Manipulation](https://arxiv.org/abs/2605.19986) | Robot Foundation / VLA | He-Yang Xu, Pengyuan Zhang, Zongyuan Ge, Xiaoshuai Hao, Serge Belongie, Xin Geng, Yuxin Peng, Xiu-Shen Wei |
| [World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks](https://arxiv.org/abs/2605.19957) | World Model | Zuyao Lin, Jianhui Zhang, Peidong Jia, Xiaoguang Zhao, Shanghang Zhang, Xingyu Chen |
| [RoHIL: Robust Human-in-the-Loop Robotic Reinforcement Learning Against Illumination Variations](https://arxiv.org/abs/2605.19924) | World Model | Shuoqin Zhang, Yixin Xiong, Xiru Gao, Kai Liu, Ke Wang, Xichuan Zhou, Zhe Hu |
| [RoVLA: Multi-Consistency Constraints for Robust Vision-Language-Action Models](https://arxiv.org/abs/2605.19678) | Robot Foundation / VLA | Jingzhou Luo, Yifan Wen, Yongjie Bai, Xinshuai Song, Yang Liu, Liang Lin |
| [HEAT: Heterogeneous End-to-End Autonomous Driving via Trajectory-Guided World Models](https://arxiv.org/abs/2605.19631) | World Model | Hoonhee Cho, Giwon Lee, Jae-Young Kang, Hyemin Yang, Heejun Park, Kuk-Jin Yoon |
| [FlyMirage: A Fully Automated Generation Pipeline for Diverse and Scalable UAV Flight Data via Generative World Model](https://arxiv.org/abs/2605.19600) | World Model | Jinhan Li, Xijie Huang, Zhaoqi Wang, Yijin Wang, Weiqi Ge, Qiyi He, Mo Zhu, Fei Gao, Yuze Wu, Xin Zhou |
| [PAPO-VLA: Planning-Aware Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2605.19580) | Robot Foundation / VLA | Peizheng Guo, Jingyao Wang, Changwen Zheng, Wenwen Qiang |
| [SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving](https://arxiv.org/abs/2605.19524) | Robot Foundation / VLA | Kefei Tian, Yuansheng Lian, Kai Yang, Xiangdong Chen, Shen Li |
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
