# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-11 05:34 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [UniMPA: A Unified Memory-Prediction-Action Model via Action-Grounded Transition Modeling](https://arxiv.org/abs/2609.11875) | Robot Foundation / VLA | Wei Li, Rui Shao, Jie He, Lingsen Zhang, Ziwei Liu, Liqiang Nie |
| [ActSafeGuard: Differentiable and Training-Aligned Constraint Enforcement for Flow-Matching Policies](https://arxiv.org/abs/2609.11697) | Robot Foundation / VLA | Jianming Ma, Rongjun Jin, Xiaxi Si, Yang Zhang, Yiheng Li, Yue Gao |
| [Memory as Plans: World-Action Modeling with Memory-Grounded Planning](https://arxiv.org/abs/2609.11561) | Robot Foundation / VLA | Sizhe Zhao, Haozhe Xie, Weiyu Zhao, Chenchu Zhang, Huan Wang, Chenyang Wang, Qinglin Liu, Shengping Zhang |
| [CAP: Continuously Adaptive Perception-Blind Humanoid Locomotion via Learned Denoising](https://arxiv.org/abs/2609.11553) | World Model | Hongjin Chen, Zijun Xu, Shihao Ma, Yi Zhao, Xilai Liu, Ke Ma, Wei Zhang, Chunyang Xie, Pengfei Li, Jieru Zhao, Wenchao Ding |
| [FARM: Reading Failure Signals from the Internal Predictive States of a Frozen Robotic World Model](https://arxiv.org/abs/2609.11445) | Robot Foundation / VLA | Haoran Pei, Mingrui Luo, Senbao Wang, Haoran Lv, Jie Guo, Sheng Zhong, Ruixi Ci |
| [Your Model Already Knows Don't Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2609.11310) | Robot Foundation / VLA | Gautam Rajendrakumar Gare, Siyi Li, Hewei Wang, Cesar Daniel Hernandez, Wei Zhao, Wolfgang M. Pauli, John Galeotti, Deva Ramanan |
| [IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2609.10915) | Robot Foundation / VLA | Kian Hosseinkhani, Qinhe Peng, George Shramko, Mehran Aghabozorgi, Jianing Qian, Tristan Engst, Alireza Moazeni, Dinesh Jayaraman, Ke Li |
| [HuRo: Robotizing Human Videos for Scalable VLA Pretraining](https://arxiv.org/abs/2609.10706) | Robot Foundation / VLA | Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim |
| [Programmable World Model](https://arxiv.org/abs/2609.10540) | World Model | Zheng-Hui Huang, Guixu Lin, Jiacheng Lin, Yi-Chuan Huang, Ruihan Yu, Muyao Niu, Siqi Yang, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang, Zhixiang Wang |
| [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](https://arxiv.org/abs/2609.10506) | World Model | Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard |
| [Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization](https://arxiv.org/abs/2609.10464) | World Model | Andy Zeyi Liu, Haoran Sun, Lucas Baker, Randall Balestriero, John Sous |
| [Frequency-Conditioned Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2609.10405) | Robot Foundation / VLA | Haochen Niu, Shengye Dong, Hao Liu, Peiwen Lin, Wang Chuang |
| [FolDeX: A Physical-World Benchmark for Long-Horizon Robotic Manipulation of Deformable Objects](https://arxiv.org/abs/2609.10243) | Robot Foundation / VLA | Chenhuan Liu, Yi Xu, Feng Wu, Hanyang Wang, Wenxiao Kuai, Weihao Ding, Shan Wang, Yang Liu, Shuyong Gao, Wenqiang Zhang |
| [RoboDrop: Curating VLA Post-Training Data via Local Gradient Compatibility](https://arxiv.org/abs/2609.10021) | Robot Foundation / VLA | Runze Xu, Yuanfan Xu, Cuijie Xu, Shuang Dai, Yining Li, Yu Wang, Jincheng Yu |
| [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](https://arxiv.org/abs/2609.09941) | Robot Foundation / VLA | Zengjue Chen, Peidong Liu, Jiawei Li, Qi Wang |
| [Time-Frequency Geometric Cross-Attention for Chunked Vision-Language-Action Models](https://arxiv.org/abs/2609.09925) | Robot Foundation / VLA | Shengye Dong, Haochen Niu, Hao Liu, Peiwen Lin, Chuang Wang, Shanmin Pang |
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
