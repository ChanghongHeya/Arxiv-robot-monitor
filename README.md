# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-04-29 04:27 UTC
- Relevant papers: 9

| Title | Type | Authors |
|---|---|---|
| [Variational Neural Belief Parameterizations for Robust Dexterous Grasping under Multimodal Uncertainty](https://arxiv.org/abs/2604.25897) | Robot Foundation / VLA | Clinton Enwerem, Shreya Kalyanaraman, John S. Baras, Calin Belta |
| [ProDrive: Proactive Planning for Autonomous Driving via Ego-Environment Co-Evolution](https://arxiv.org/abs/2604.25329) | World Model | Chuyao Fu, Shengzhe Gan, Zhuoli Ouyang, Yuhan Rui, Xiaowei Chi, Sirui Han, Jiankun Wang, Hong Zhang |
| [Libra-VLA: Achieving Learning Equilibrium via Asynchronous Coarse-to-Fine Dual-System](https://arxiv.org/abs/2604.24921) | Robot Foundation / VLA | Yifei Wei, Linqing Zhong, Yi Liu, Yuxiang Lu, Xindong He, Maoqing Yao, Guanghui Ren |
| [Exploiting Differential Flatness for Efficient Learning-based Model Predictive Control of Constrained Multi-Input Control Affine Systems](https://arxiv.org/abs/2604.24706) | World Model | Tobias A. Farger, Adam W. Hall, Angela P. Schoellig |
| [Learning Human-Intention Priors from Large-Scale Human Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2604.24681) | Robot Foundation / VLA | Yifan Xie, YuAn Wang, Guangyu Chen, Jinkun Liu, Yu Sun, Wenbo Ding |
| [CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/abs/2604.24622) | Robot Foundation / VLA | Fan Du, Feng Yan, Jianxiong Wu, Xinrun Xu, Weiye Zhang, Weinong Wang, Yu Guo, Bin Qian, Zhihai He, Fei Wang, Heng Yang |
| [Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://arxiv.org/abs/2604.24447) | Robot Foundation / VLA | Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li, Jinyu Gu |
| [$M^2$-VLA: Boosting Vision-Language Models for Generalizable Manipulation via Layer Mixture and Meta-Skills](https://arxiv.org/abs/2604.24182) | Robot Foundation / VLA | Siyao Xiao, Yuhong Zhang, Zhifang Liu, Zihan Gao, Jingye Zhang, Sinwai Choo, Dake Zhong, Mengzhe Wang, Xiao Lin, Xianfeng Zhou, Jia Jia, Haoqian Wang |
| [AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation](https://arxiv.org/abs/2604.24086) | Robot Foundation / VLA | Kai Yang, Zedong Chu, Yingnan Guo, Zhengbo Wang, Shichao Xie, Yanfen Shen, Xiaolong Wu, Xing Li, Mu Xu |
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
