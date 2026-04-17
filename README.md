# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-04-17 04:10 UTC
- Relevant papers: 11

| Title | Type | Authors |
|---|---|---|
| [Learning Ad Hoc Network Dynamics via Graph-Structured World Models](https://arxiv.org/abs/2604.14811) | World Model | Can Karacelebi, Yusuf Talha Sahin, Elif Surer, Ertan Onur |
| [World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems](https://arxiv.org/abs/2604.14732) | Robot Foundation / VLA | Runze Li, Hongyin Zhang, Junxi Jin, Qixin Zeng, Zifeng Zhuang, Yiqi Tang, Shangke Lyu, Donglin Wang |
| [Energy-based Regularization for Learning Residual Dynamics in Neural MPC for Omnidirectional Aerial Robots](https://arxiv.org/abs/2604.14678) | World Model | Johannes Kübel, Henrik Krauss, Jinjie Li, Moju Zhao |
| [HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268) | World Model | Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo |
| [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](https://arxiv.org/abs/2604.14125) | Robot Foundation / VLA | Tianshuo Yang, Guanyu Chen, Yutian Chen, Zhixuan Liang, Yitian Liu, Zanxin Chen, Chunpu Xu, Haotian Liang, Jiangmiao Pang, Yao Mu, Ping Luo |
| [[Emerging Ideas] Artificial Tripartite Intelligence: A Bio-Inspired, Sensor-First Architecture for Physical AI](https://arxiv.org/abs/2604.13959) | Robot Foundation / VLA | You Rim Choi, Subeom Park, Hyung-Sin Kim |
| [Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection](https://arxiv.org/abs/2604.13942) | Robot Foundation / VLA | Zhen Liu, Xinyu Ning, Zhe Hu, Xinxin Xie, Weize Li, Zhipeng Tang, Chongyu Wang, Zejun Yang, Hanlin Wang, Yitong Liu, Zhongzhu Pu |
| [Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning](https://arxiv.org/abs/2604.13891) | World Model | Saeed Rahmani, Gözde Körpe, Zhenlin, Xu, Bruno Brito, Simeon Craig Calvert, Bart van Arem |
| [Beyond State Consistency: Behavior Consistency in Text-Based World Models](https://arxiv.org/abs/2604.13824) | World Model | Youling Huang, Guanqiao Chen, Junchi Yao, Lu Wang, Fangkai Yang, Chao Du, ChenZhuo Zhao, Pu Zhao, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang |
| [Jump-Start Reinforcement Learning with Vision-Language-Action Regularization](https://arxiv.org/abs/2604.13733) | Robot Foundation / VLA | Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, Loris Roveda |
| [Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap](https://arxiv.org/abs/2604.13654) | Robot Foundation / VLA | Hanxuan Chen, Jie Zheng, Siqi Yang, Tianle Zeng, Siwei Feng, Songsheng Cheng, Ruilong Ren, Hanzhong Guo, Shuai Yuan, Xiangyue Wang, Kangli Wang, Ji Pei |
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
