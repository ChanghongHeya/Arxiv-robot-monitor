# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-11-13 07:32 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models](https://arxiv.org/abs/2611.17110) | Robot Foundation / VLA | Jiachun Jin, Zetong Zhou, Haonan Wang, Xiao Yang, Jun Zhu, Zhijie Deng |
| [STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models](https://arxiv.org/abs/2611.16589) | Robot Foundation / VLA | Zhuo Han, Yeqiang Wang, Xinran Wang, Hongwei Han, Yi Xiong, Zunian Wan, Jianbo Mao, Huan Peng, Yongcheng Liu, Wei Shan, Maoqing Yao |
| [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2611.16579) | World Model | Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv |
| [PhysCapBench: A Cross-Domain Benchmark for Physically Grounded Video Captioning](https://arxiv.org/abs/2611.16424) | World Model | Haofeng Wang, Pengcheng Wen, Ruiqi Li, Yuhao Zhang, Tiange Zhang, Boren Zheng, Xuanyi Liu, Siyu Tao, Danni Yu, Gan Lin, Haocheng Tang, Tianzizhe Guo, Mingyuan Su, Boyuan Chen, Zhongyuan Wang |
| [BlinkMimic: Training a Humanoid Motion Tracker in Minutes on a Single GPU](https://arxiv.org/abs/2611.16422) | World Model | Fuyi Chen |
| [I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History](https://arxiv.org/abs/2611.16419) | Robot Foundation / VLA | Xiangyi Jia, Kaixian Qu, Shengzhi Wang, Chenyu Yang, Robert Katzschmann, Marco Hutter |
| [What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation](https://arxiv.org/abs/2611.16246) | Robot Foundation / VLA | Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu, Bokui Chen, Houde Liu |
| [MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes](https://arxiv.org/abs/2611.15937) | Robot Foundation / VLA | Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli |
| [What World Model Does Active Object Search Need? A Study under Imperfect Detection](https://arxiv.org/abs/2611.15689) | World Model | Kyeongryeol Go |
| [Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction](https://arxiv.org/abs/2611.15651) | Robot Foundation / VLA | Miao Pan, Kaixiang Yao, Xiaohe Zhou, Xu Wang, Qinfeng Li, Wenqi Zhang, Xuhong Zhang |
| [What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation](https://arxiv.org/abs/2611.15491) | Robot Foundation / VLA | Zhuoyue Li, Zhendong Han, Pankhuri Vanjani, Wenting Li, Rudolf Lioutikov |
| [ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490) | Robot Foundation / VLA | Zibin Dong, Yicheng Liu, Shiduo Zhang, Tianyuan Yuan, Baijun Ye, Jinqiu Wang, Hang Zhao |
| [Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning](https://arxiv.org/abs/2611.15381) | Robot Foundation / VLA | Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer, Yung-Hui Li, Donglin Chen, Shang-Ching Liu, Jianwei Zhang |
| [Bind-WAM: Binding-Uncertainty-Guided Selective Future Imagination in World Action Models](https://arxiv.org/abs/2611.15368) | World Model | Chenhao Qiu, Shuyi Chen, Songen Gu, Shufeng Nan, Tianyu Wang, Siyu Lin, Yifan Li, Bingwen Zhu, Yanwei Fu |
| [CARE-Drive: Coupled Alternating Refinement for Ego-trajectories](https://arxiv.org/abs/2611.15360) | Robot Foundation / VLA | Xiao Ma, Yijun Chen, Zhiquan Hu, Jicheng Zhao, Yuming Li, Chuang Dai |
| [AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention](https://arxiv.org/abs/2611.15215) | World Model | Haoyi Zhang, Qi Zhang, Yunfan Ren, Yi Bin, Lei Zhu, Heng Tao Shen |
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
