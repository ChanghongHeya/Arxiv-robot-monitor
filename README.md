# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-03 05:25 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) | World Model | Kelvin Li, Dhruv Pendharkar, Anish Pahilajani, Chuyi Shang, Leon Oks, Leonid Karlinsky, Rogerio Feris, Trevor Darrell, Roei Herzig |
| [Do Better Imagined Rollouts Mean Better Robot Control? A Controlled Study of World-Model Evaluation Under Feedback](https://arxiv.org/abs/2609.02811) | World Model | Dharini Raghavan, Amritpal Singh |
| [From Proxy Learning to Driving Decisions: A Transfer-Based Framework for Evaluating Future-Aware Autonomous Driving Planners](https://arxiv.org/abs/2609.02688) | World Model | Yikai Wu |
| [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2609.02653) | Robot Foundation / VLA | Mingyu Mei, Haojie Xu, Shihao Jin, Zibo Dai, Qihao Cheng, Zhengrui Lv, Hongjie Fang, Shirun Tang, Guang Chen, Xinyue Zhao, Huiliang Shen, Zaixing He |
| [Latent Cluster Analysis for Vision-Language-Action Models](https://arxiv.org/abs/2609.02634) | Robot Foundation / VLA | Theodor Wulff, Sergio Lanza, Tamara Bila, Angelo Cangelosi, Stefan Wermter, Igor Farkas |
| [ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation](https://arxiv.org/abs/2609.02546) | Robot Foundation / VLA | Mi Yan, Wenhao Zhang, Zhiqi Zhang, Yu Peng, Tangxinyu Wang, Lingfei Zhai, Jiayi Su, Shengliang Deng, Lin Peng, Yaowei Liu, Yuxing Chen, Zhiyuan Wei, Jilong Wang, Jiayi Chen, Jiangran Lyu, Zhizheng Zhang, He Wang |
| [World-Model-Augmented Visual Locomotion for Humanoids on Foothold-Constrained Terrain](https://arxiv.org/abs/2609.02542) | World Model | Yuxi Liu, Lijun Han, Ziming Wang, Ao Zhang, Cong Yang, Wei Sui |
| [Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531) | Robot Foundation / VLA | Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid |
| [Towards Zero-Shot Transfer Across Embodiments For Driving VLAs](https://arxiv.org/abs/2609.02341) | Robot Foundation / VLA | Caio Azevedo, Stefano Sabatini, Sascha Hornauer, Fabien Moutarde |
| [Modeling What Changes: Sparse, Residual World Models for Object-Centric Manipulation](https://arxiv.org/abs/2609.02046) | World Model | Param Thakkar, Parsika Paresh Shah, Manisha Sushant Gote |
| [Facet-0: A Robotic Foundation Model for Contact-Rich Precise Manipulation](https://arxiv.org/abs/2609.01596) | Robot Foundation / VLA | Haoyuan Deng, Haichao Liu, Wenkai Guo, Yuan Ling, Zaijia Yang, Yuanjiang Xue, Haosheng Sun, Liangzi Wang, Ziwei Wang |
| [Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching](https://arxiv.org/abs/2609.01404) | Robot Foundation / VLA | Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon, Dohoon Ryu, Daehee Kim, Myungseo Song, Jihyuk Byun, Seunggyu Chang, Taeho Kil, Jiseob Kim, Bado Lee, Geewook Kim |
| [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | Robot Foundation / VLA | Wei Wang, Wenqiao Zhang, Yutong Lin, Yuqian Yuan, Tianwei Lin, Jinhao Mao, Zhenxuan Fan, Mingjian Gao, Yang Dai, Wentong Li, Zheqi Lv, Zheng Dong, Yingjie Niu, Jiaqi Zhu, Jun Xiao, Chao Li, Yueting Zhuang |
| [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://arxiv.org/abs/2609.01215) | Robot Foundation / VLA | Riyaaz Shaik, Chandru Venkataraman |
| [ProxPI: Proximal Prior Injection for Sampling-Based MPC under Learned-Prior Mismatch](https://arxiv.org/abs/2609.00941) | World Model | Euncheol Im, Myotaeg Lim, Yisoo Lee |
| [Knowing When to Stop: Adaptive Action Chunking via Internal Cross-Attention Dynamics in VLAs](https://arxiv.org/abs/2609.00908) | Robot Foundation / VLA | Runze Xu, Xiaolong Shan, Shuang Dai, Yu Wang, Jincheng Yu |
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
