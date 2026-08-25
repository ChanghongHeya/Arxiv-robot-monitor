# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-08-25 02:15 UTC
- Relevant papers: 17

| Title | Type | Authors |
|---|---|---|
| [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486) | Robot Foundation / VLA | Yiren Lu, Xin Ye, Jiaming Liu, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman |
| [Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models](https://arxiv.org/abs/2608.23478) | Robot Foundation / VLA | Sangoh Lee, Sangwoo Mo, Wook-Shin Han |
| [Reward-Free Continual Adaptation for Resilient Space Robots](https://arxiv.org/abs/2608.23452) | World Model | Andrej Orsula, Miguel Olivares-Mendez, Carol Martinez |
| [ROS2SmolVLA: Enabling Small Vision-Language-Action Models for Integration into Industrial-Grade Lightweight Robots](https://arxiv.org/abs/2608.23320) | Robot Foundation / VLA | Nils Mandischer, Noah Böckmann, Ludwig Holl, Lars Mikelsons |
| [Think Only When Needed: Prompt-Authority Control for Selective Slow-Path Intervention in Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23224) | Robot Foundation / VLA | Zhiruo Zhou, Zelin Li, Xiwen Chen, Jiazhuo Li, Chenwei Wang, Huiming Chen, Xiaojun Zhu |
| [Guided Riemannian Optimization (GuRO): Bridging Model Predictive Control and Decision Transformers](https://arxiv.org/abs/2608.23204) | World Model | Hossein Abdi, Satya Prakash Dash, Mingfei Sun |
| [EchoWM: Open and Enterable Omnimodal World Models](https://arxiv.org/abs/2608.23189) | World Model | Songchun Zhang, Yaowei Li, Junhao Zhuang, Weiyang Jin, Haoyu Wang, Xin Lu, Yilang Sun, Shiyi Zhang, Haoran Li, Xiaoxiao Ma, Yuming Li, Yijun Liu, Yaofeng Su, Yanwen Ma, Haoyu Wu, Zihan Su, Yue Ma, Lvmin Zhang, Haoyang Huang, Zeyue Xue, Anyi Rao, Nan Duan |
| [Pointing-VLA: Typed Spatial Grounding Interfaces for Vision-Language-Action Manipulation](https://arxiv.org/abs/2608.23138) | Robot Foundation / VLA | Xiwen Chen, Zelin Li, Zhiruo Zhou, Huiming Chen, Chenwei Wang, Xiaojun Zhu |
| [InstructMove: A Text-Indispensable Benchmark for Instruction-Following Manipulation](https://arxiv.org/abs/2608.22990) | Robot Foundation / VLA | Mengao Zhao, Ziang Li, Chaodong Huang, Mengchen Ma, Haoyi Jiang, Yiwei Jin, Xinjie Wang, Yun Du, Xuewu Lin, Taojun Ding, Hongyu Xie, Jackson Jiang, Chunlei Yu, Kaihua Zhang, Lichao Huang, Liu Liu, Tianwei Lin, Zhizhong Su |
| [UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models](https://arxiv.org/abs/2608.22869) | Robot Foundation / VLA | Lars Osterberg, Maggie Wang, Mac Schwager |
| [LpWM: A Case for Sparse Representations in World Models](https://arxiv.org/abs/2608.22764) | World Model | Yilun Kuang, Yash Dagade, Quentin Le Lidec, Lucas Maes, Randall Balestriero, Yann LeCun |
| [Where World Models Break: Natural-Input Failure Discovery](https://arxiv.org/abs/2608.22421) | World Model | Zhanpeng Shi, Zi Liang, Rong Feng, Shiqin Tang, Xuyang Chen, Hongzong Li |
| [Robust Bimanual Vision-Language-Action Models via Embarrassingly Simple Modality Masking](https://arxiv.org/abs/2608.22419) | Robot Foundation / VLA | Dongzhou Cheng, Ziang Li, Yixiao Zhou, Haojuan Li, Jinghao Zhang, Lei Lei, Minjing Dong, Jie Gui, Jiaqi Wang |
| [LD4WAM: Learning Latent Dynamics from Human Videos for World Action Models](https://arxiv.org/abs/2608.22403) | Robot Foundation / VLA | Zhenhao Shen, Jiaqi Liang, Jasper Lu, Feng Jiang, Yuran Wang, Chuanbo Wei, Jiayi Liu, Jianchun Yang, Qize Yu, Jiadi You, Ce Hao, Guanqi He, Chen Xie, Ruihai Wu |
| [Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning](https://arxiv.org/abs/2608.22294) | World Model | Juntao Cheng, Jingkai Wang, Yijun Shen, Xiansheng Chen, Zhiwei Yu |
| [DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model](https://arxiv.org/abs/2608.22278) | World Model | Jie Yin, Xingyu Lai |
| [On the Capability Separation Between World-Model Policy Learning and Imitated World-Action Models](https://arxiv.org/abs/2608.22197) | World Model | Yang Yu |
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
