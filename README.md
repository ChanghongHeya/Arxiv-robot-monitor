# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-10-03 05:58 UTC
- Relevant papers: 15

| Title | Type | Authors |
|---|---|---|
| [World Observer: Joint Actor-Observer Generation for Persistent World Modeling](https://arxiv.org/abs/2610.02162) | World Model | Hyunwook Choi, Dahyun Chung, Hyunsung Kim, Siyoon Jin, Jinhyeok Choi, Junyoung Seo, Seungryong Kim |
| [DuoMind: Enabling Distributed Multi-Robot Coordination with Semantic Communication](https://arxiv.org/abs/2610.02161) | Robot Foundation / VLA | Hanchu Zhou, Dechen Gao, Hang Wang, Brendan Lynch, Boqi Zhao, Qiyao Ma, Raman Goyal, Junshan Zhang |
| [UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054) | Robot Foundation / VLA | Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li |
| [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939) | Robot Foundation / VLA | Ruiyang Si, Jianxin Bi, Shunyu Yang, Rui Ni, Wenbo Huang, Qiang Wang, Shulong Jiang, Duomin Wang, Xiuyu Li, Haiwen Feng, Zhen Dong, Daquan Zhou |
| [ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing](https://arxiv.org/abs/2610.01856) | Robot Foundation / VLA | Zhugang Liu, Kaichuang Zhang, Jinman Zhang, Pu Sun, Martha Asare, Jose Hernandez, Maxim Ermolinsky, Efren Saenz, Qi Lu, Jinghao Yang |
| [Continuous Conditioning of VLAs with Augmenting EMG and Visual Task Descriptors](https://arxiv.org/abs/2610.01794) | Robot Foundation / VLA | Edward W. Staley, Connor O. Pyles, Rahul Hingorani, Frank Camargo, Griffin Milsap, Jared Markowitz, Matthew S. Fifer, Michael Wolmetz |
| [World Motion Models: Flexible Sequence Modeling of SE(3) Trajectories](https://arxiv.org/abs/2610.01742) | World Model | Jiahui Lei, Qianqian Wang, Trevor Darrell, Angjoo Kanazawa |
| [ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection](https://arxiv.org/abs/2610.01741) | Robot Foundation / VLA | Yijie Zhu, Rui Shao, Jie He, Wei Li, Bo Zhao, Yelin Wang, Xiaochen Yuan, Tao Tan, Miao Zhang, Xiaojiang Peng, Zitong Yu |
| [Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614) | World Model | Xindi Yang, Baolu Li, Liam Lee, Zhenfei Yin, Songxin Zhang, Zhuoyang Song, Xu Jia, Jianfei Cai, Tien-Tsin Wong, Bingyi Jing, Mengyue Yang |
| [ReCo: Response-Consistent Locomotion with Policy-Aware MPC for Legged Manipulation](https://arxiv.org/abs/2610.01612) | World Model | Kuankuan Sima, Yichao Gao, Chenxi Gu, Kefan Zhao, Lin Zhao |
| [Completion Aware Guidance for World Action Models](https://arxiv.org/abs/2610.01559) | World Model | Seungyeon Kim, Junhoo Lee, Baekseung Kim, Minkyu Kim, Nojun Kwak |
| [Is Success All You Need? Investigating the Impact of Input Perturbations on VLA Behaviour in Tabletop Manipulation Tasks](https://arxiv.org/abs/2610.01351) | Robot Foundation / VLA | Sophie Higham, Riccardo Andrea Izzo, Matteo Matteucci, Alessandro Suglia |
| [Cross-entropy optimization with prioritized constraints](https://arxiv.org/abs/2610.01319) | World Model | Francisco Roldan Sanchez, Pau de las Heras Molins, David Fridovich-Keil, Georgios Bakirtzis |
| [Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning](https://arxiv.org/abs/2610.01224) | World Model | Takumi Hara, Kanata Suzuki |
| [PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162) | World Model | Isaiah Milkey, Som Sagar, Aditya Taparia, Xinyuan Liu, Jiqing Wen, Ransalu Senanayake |
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
