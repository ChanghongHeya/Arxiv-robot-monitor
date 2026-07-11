# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-07-11 04:08 UTC
- Relevant papers: 6

| Title | Type | Authors |
|---|---|---|
| [FabriVLA: A Lightweight Vision-Language-Action Model for Precise Multi-Task Manipulation](https://arxiv.org/abs/2607.08575) | Robot Foundation / VLA | Shiyuan Yang, Borong Zhang, Jizheng Zhang, Zhijia Tao, Junfei Guo, Donglai Ran, Xu Bian, Qingbiao Li |
| [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448) | Robot Foundation / VLA | Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, Zhengru Fang, Yi Nie, Changxu Wei, Yu Wang, Wenbo Ding, Chao Yu |
| [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375) | Robot Foundation / VLA | Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song |
| [Write-Protected Discrete Bottlenecks for Language-Grounded World Models: A Structural Limitation and Sufficient Fix](https://arxiv.org/abs/2607.08312) | World Model | Jiayi Fang |
| [TFP: Temporally Conditioned Memory-Fusion Policies for Visuomotor Learning](https://arxiv.org/abs/2607.08283) | Robot Foundation / VLA | Yushen Liang, Yue Peng, Baosheng Jin, Tianluo Zhang, Xinyu Zhang, Shuyi Zhou, Zhuoran Chen, Xinqi Liu, Shenji Wan |
| [LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action](https://arxiv.org/abs/2607.08182) | Robot Foundation / VLA | Qi Lyu, Baicheng Liu, Xudong Wang, Jiahua Dong, Lianqing Liu, Zhi Han |
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
