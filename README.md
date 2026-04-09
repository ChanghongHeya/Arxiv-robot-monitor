# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-04-09 03:44 UTC
- Relevant papers: 14

| Title | Type | Authors |
|---|---|---|
| [PhyEdit: Towards Real-World Object Manipulation via Physically-Grounded Image Editing](https://arxiv.org/abs/2604.07230) | World Model | Ruihang Xu, Dewei Zhou, Xiaolong Shen, Fan Ma, Yi Yang |
| [INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209) | World Model | InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao |
| [Towards Multi-Object Nonprehensile Transportation via Shared Teleoperation: A Framework Based on Virtual Object Model Predictive Control](https://arxiv.org/abs/2604.06932) | World Model | Xinyang Fan, Zhaoyang Chen, Shu Xin, Yi Ren, Zainan Jiang, Fenglei Ni, Hong Liu |
| [Telecom World Models: Unifying Digital Twins, Foundation Models, and Predictive Planning for 6G](https://arxiv.org/abs/2604.06882) | World Model | Hang Zou, Yuzhi Yang, Lina Bariah, Yu Tian, Yuhuan Lu, Bohao Wang, Anis Bara, Brahim Mefgouda, Hao Liu, Yiwei Tao, Sergy Petrov, Salma Cheour, Nassim Sehad, Sumudu Samarakoon, Chongwen Huang, Samson Lasaulce, Mehdi Bennis, Mérouane Debbah |
| [The Rhetoric of Machine Learning](https://arxiv.org/abs/2604.06754) | World Model | Robert C. Williamson |
| [Infrastructure First: Enabling Embodied AI for Science in the Global South](https://arxiv.org/abs/2604.06722) | Robot Foundation / VLA | Shaoshan Liu, Jie Tang, Marwa S. Hassan, Mohamed H. Sharkawy, Moustafa M. G. Fouda, Tiewei Shang, Zixin Wang |
| [Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339) | Robot Foundation / VLA | Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao |
| [Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168) | Robot Foundation / VLA | Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan |
| [Learning-Guided Force-Feedback Model Predictive Control with Obstacle Avoidance for Robotic Deburring](https://arxiv.org/abs/2604.06133) | World Model | Krzysztof Wojciechowski, Ege Gursoy, Arthur Haffemayer, Sebastien Kleff, Vincent Bonnet, Florent Lamiraux, Nicolas Mansard |
| [Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation](https://arxiv.org/abs/2604.05673) | Robot Foundation / VLA | Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma |
| [A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model](https://arxiv.org/abs/2604.05672) | Robot Foundation / VLA | Kaidong Zhang, Jian Zhang, Rongtao Xu, Yu Sun, Shuoshuo Xue, Youpeng Wen, Xiaoyu Guo, Minghao Guo, Weijia Liufu, Liu Zihou, Kangyi Ji, Yangsong Zhang, Jiarun Zhu, Jingzhi Liu, Zihang Li, Ruiyi Chen, Meng Cao, Jingming Zhang, Shen Zhao, Xiaojun Chang, Feng Zheng, Ivan Laptev, Xiaodan Liang |
| [SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation](https://arxiv.org/abs/2604.05656) | Robot Foundation / VLA | Wuyang Luan, Junhui Li, Weiguang Zhao, Wenjian Zhang, Tieru Wu, Rui Ma |
| [Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment](https://arxiv.org/abs/2604.05614) | Robot Foundation / VLA | Theodor Wulff, Federico Tavella, Rahul Singh Maharjan, Manith Adikari, Angelo Cangelosi |
| [Uncovering Linguistic Fragility in Vision-Language-Action Models via Diversity-Aware Red Teaming](https://arxiv.org/abs/2604.05595) | Robot Foundation / VLA | Baoshun Tong, Haoran He, Ling Pan, Yang Liu, Liang Lin |
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
