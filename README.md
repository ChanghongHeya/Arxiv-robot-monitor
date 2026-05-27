# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-05-27 05:12 UTC
- Relevant papers: 13

| Title | Type | Authors |
|---|---|---|
| [Riding the Shifting Potential: When Reactive Control Suffices for Multi-Goal Behavior](https://arxiv.org/abs/2605.27314) | World Model | Vito Mengers, Oliver Brock |
| [FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies](https://arxiv.org/abs/2605.27284) | Robot Foundation / VLA | Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu |
| [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820) | Robot Foundation / VLA | Jiarun Zhu, Yijun Hong, Xiaoquan Sun, Zetian Xu, Mingqi Yuan, Zhiyong Wang, Wenjun Zeng, Jiayu Chen |
| [When Does LeJEPA Learn a World Model?](https://arxiv.org/abs/2605.26379) | World Model | David Klindt, Yann LeCun, Randall Balestriero |
| [Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization](https://arxiv.org/abs/2605.26282) | World Model | Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang, Hai Wang, Zhuo Sun, Che Liu |
| [AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models](https://arxiv.org/abs/2605.25901) | Robot Foundation / VLA | Cuong Huynh, Maxim Popov, Denis Gridusov, Sergey Kolyubin |
| [Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models](https://arxiv.org/abs/2605.25889) | Robot Foundation / VLA | Jianwei Tai |
| [WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation](https://arxiv.org/abs/2605.25874) | Robot Foundation / VLA | Kaining Ying, Hengrui Hu, Siyu Ren, Jiamu Li, Fengjiao Chen, Ziwen Wang, Xuezhi Cao, Xunliang Cai, Henghui Ding |
| [OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation](https://arxiv.org/abs/2605.25829) | Robot Foundation / VLA | Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan |
| [Rethinking VLM Representation for VLA Initialization](https://arxiv.org/abs/2605.25802) | Robot Foundation / VLA | Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An, Xinyu Wei, Jianbo Liu, Hongsheng Li |
| [Compliant Non-Prehensile Pushing Manipulation](https://arxiv.org/abs/2605.25672) | World Model | Francesco Cufino, Mario Selvaggio, Fabio Amadio, Fabio Ruggiero |
| [Back to Parsimonious Latents: Learning Task-Centric World Models from Visual Foundations](https://arxiv.org/abs/2605.25620) | World Model | Minghao Fu, Fan Feng, Nicklas Hansen, Biwei Huang |
| [EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models](https://arxiv.org/abs/2605.25477) | Robot Foundation / VLA | Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn |
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
