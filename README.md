# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-01 05:58 UTC
- Relevant papers: 17

| Title | Type | Authors |
|---|---|---|
| [SUN: Persistent Programs For Language-Grounded Control-to-Learning-to-Real Policies](https://arxiv.org/abs/2608.31167) | World Model | Weiqi Wang, Zhi Li, Yudong Lei, David Martinez, Xiaofeng Gao, Yuxin Jiang, Chenfanfu Jiang, Yingnian Wu, Demetri Terzopoulos, Ran Gong |
| [CAER: Causal Action Effect Reweighting for World Model Training](https://arxiv.org/abs/2608.30897) | World Model | Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li |
| [Temporal Forcing: 4D Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2608.30643) | Robot Foundation / VLA | Xingyu Ding, Yuzhong Zhao, Chunhai Zhao, Yinghuan Shi, Chaoyang Zhao, Yifan Zhang |
| [Behavior-Skill: A Fine-Grained Benchmark for Evaluating Vision-Language-Action Policies in Long-Horizon Tasks](https://arxiv.org/abs/2608.30536) | Robot Foundation / VLA | Chunyun Ma, Lun Luo, Xingjian Luo, Xiexing Feng, Hang Zhang, Wei Liu, Feng Qiao, Yaonan Wang, Huimin Lu, Xieyuanli Chen |
| [PAVE: Predictive Alignment and Value-Guided Evolution for World-Action Policies](https://arxiv.org/abs/2608.30378) | Robot Foundation / VLA | Botong Zhao, Fang Yu, Tim, Senhua Zhu, Xinyuan Chen, Yue Lu |
| [CometVLA: Co-Training on an Embodied Data Pyramid towards Physical Understanding](https://arxiv.org/abs/2608.30289) | Robot Foundation / VLA | Hanwen Wan, Dafeng Chi, Linbo Zhai, Tianao Shen, Yuzheng Zhuang, Tianle Zhang, Peidong Liu, Liang Lin, Xiaoqiang Ji |
| [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](https://arxiv.org/abs/2608.30237) | Robot Foundation / VLA | Hongzhe Bi, Zihao Zhou, Yihang Tang, Jingrui Pang, Shuhe Huang, Haitian Liu, Runqing Wang, Shuai Huang, Yichen Wang, Yiming Cheng, Ruowen Zhao, Zhenghua Li, Hengkai Tan, Xiaolong Liu, Jinhui Wan, Jiabao Liu, Min Zhao, Fan Bao, Jun Zhu |
| [Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving](https://arxiv.org/abs/2608.30144) | Robot Foundation / VLA | Tongfei Guo, Lili Su |
| [Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving](https://arxiv.org/abs/2608.30122) | Robot Foundation / VLA | Tian Zhang, Zhuo Huang, Hongrui Ye, Yu Wu, Zengmao Wang, Kaixuan Zhou |
| [How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account](https://arxiv.org/abs/2608.30067) | World Model | Ruize Xu, Xiao Yu, Yujin Tang, Chenming Shang, Nikhil Singh |
| [The Intervention Gap in Latent World Models](https://arxiv.org/abs/2608.29998) | World Model | Donna Vakalis |
| [Training-Free Action Correction for VLA Model Failures via Language Feedback](https://arxiv.org/abs/2608.29967) | Robot Foundation / VLA | Owen Kwon, Pablo Ortega-Kral, Arthur Bucker, Jean Oh |
| [AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies](https://arxiv.org/abs/2608.29937) | Robot Foundation / VLA | Yafei Zhang, Nan Wu |
| [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910) | World Model | Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li |
| [Self-Aware Active Learning Enables Continual Improvement in Autonomous Driving](https://arxiv.org/abs/2608.29772) | World Model | Dong Hu, Chao Huang, Carman K. M. Lee, Dimitrios Kanoulas |
| [SmoothRL: Online Reinforcement Learning During Asynchronous Execution](https://arxiv.org/abs/2608.29768) | Robot Foundation / VLA | Guang Gao, Yuxuan Nong, Baifu Huang, Jianan Wang |
| [DriftingVLA: Native One-Step Vision-Language-Action Generation via Per-Dimension Temporal Drifting](https://arxiv.org/abs/2608.29749) | Robot Foundation / VLA | Yuxuan Gao, Shiqi Zhang, Yedong Shen, Yifan Duan, Wenhao Yu, Xin Zhang, Siyuan Cao, Jiajun Deng, Yanyong Zhang |
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
