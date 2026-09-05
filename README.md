# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-09-05 05:12 UTC
- Relevant papers: 14

| Title | Type | Authors |
|---|---|---|
| [GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation](https://arxiv.org/abs/2609.04193) | Robot Foundation / VLA | Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao |
| [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070) | Robot Foundation / VLA | Ruoyu Yao, Yusen Xie, Qingzhao Liu, Pei Liu, Zewei Yang, Yipeng Zhu, Xiaolong Wang, Jun Ma |
| [Toward Unified Robot Learning: Bridging Representation, Vision-Language-Action, and World Models](https://arxiv.org/abs/2609.03927) | Robot Foundation / VLA | Shaunak A. Mehta, Ananya Hazarika, Haochen Zhang, Fan Yang, Ryo Moriyama, Wenkai Li, Yash Patel, Kanata Suzuki |
| [A hybrid pipeline for dynamic ontology-based semantic mapping](https://arxiv.org/abs/2609.03891) | World Model | Konstantinos Dimitropoulos, Ioannis Hatzilygeroudis |
| [FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation](https://arxiv.org/abs/2609.03889) | Robot Foundation / VLA | Yutian Zhang, Siyuan Ma, Liwen Yang, Yang Li, Ce Hao, Haozhen Chi, Dong We, Qiaojun Yu, Dibo Hou |
| [Semantic Bayesian World Models](https://arxiv.org/abs/2609.03834) | World Model | Tommaso Soru |
| [Rethinking World Models for Safety-Critical Embodied Systems](https://arxiv.org/abs/2609.03774) | World Model | Kailang Ma, Heye Huang, Inhi Kim, Kitae Jang |
| [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715) | Robot Foundation / VLA | Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa |
| [Predictive Zonotope Reduction: Precise Runtime Monitoring under Uncertainty](https://arxiv.org/abs/2609.03699) | World Model | Vladimir Krsmanovic, Florian Kohn, Bernd Finkbeiner, Milan Simovic |
| [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](https://arxiv.org/abs/2609.03681) | Robot Foundation / VLA | Chenhao Zhang, Hanyu Zhao, Hang Cheng, Tengfei Pan, Long Zeng |
| [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602) | Robot Foundation / VLA | Jinyang Wang, Shiwei Li, Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yihang Zhao, Liu Liu, Yongjia Zhao, Jinlong Chen, Huirui Xu, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao, Minghao Yang |
| [Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections](https://arxiv.org/abs/2609.03591) | Robot Foundation / VLA | Jiafeng Xu, Qi Li, Yan Shen, Yiyu Ren, Travis Davies, Shaowen He, Ze Wang, Yifan Yang, Ran Cheng, Hao Dong |
| [Drive-HWM: Hierarchical World Models for Dynamic-Latent Guided Autonomous Driving](https://arxiv.org/abs/2609.03572) | Robot Foundation / VLA | Zhaoxin Fan, Tianbao Zhang, Wenjun Wu, Xiaofeng Wang, Yeying Jin, Jian Zhao, Zheng Zhu, Shuicheng Yan |
| [Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning](https://arxiv.org/abs/2609.03565) | World Model | Muyuan Liu, Yue Huang, Zheng Liang, Xiang Gao |
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
