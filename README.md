# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-10-29 06:41 UTC
- Relevant papers: 16

| Title | Type | Authors |
|---|---|---|
| [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666) | Robot Foundation / VLA | Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang |
| [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588) | World Model | Rodrigo Gonzalez Laiz, Steffen Schneider |
| [World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer](https://arxiv.org/abs/2610.37518) | Robot Foundation / VLA | Guoning Wu, Zijian Cai, Yuhang Zhang, Ying Liu, Yongbin Zheng |
| [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) | Robot Foundation / VLA | Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu |
| [VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning](https://arxiv.org/abs/2610.37378) | Robot Foundation / VLA | Bojun Zou, Wenhao Yu, Jiaohao Li, Jiaxuan Lin, Guanting Ye, Haohan Geng, Weihao Yu, Yanyong Zhang, Jianmin Ji |
| [Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer](https://arxiv.org/abs/2610.37330) | Robot Foundation / VLA | Hanwen Ren, Meng Zheng, Wenzhe Cui, Benjamin Planche, Zhongpai Gao, Anwesa Choudhuri, Terrence Chen, Ziyan Wu |
| [Vision-Language-Action or World-Action? Just Action Models](https://arxiv.org/abs/2610.37219) | Robot Foundation / VLA | Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki |
| [Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution](https://arxiv.org/abs/2610.37215) | Robot Foundation / VLA | Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, Trong-Bao Ho, Thien-Loc Ha, Tan Q. Nguyen, Tuan Dam, Vu N. Duong, Daniel Sonntag, Ngan Le, Khoa D. Doan, Jan Peters, An Thai Le, Duy M. H. Nguyen, Vien Anh Ngo |
| [GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091) | Robot Foundation / VLA | Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao |
| [Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037) | Robot Foundation / VLA | Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang, Weiran Huang |
| [Vision-Language Agents Can Learn in Their Own Latent Worlds](https://arxiv.org/abs/2610.36925) | World Model | Haoxi Li, Sikai Bai, Jianfei Ma, Qinglin Hou, Xiaocheng Lu, Tao Han, Jie Zhang, Song Guo |
| [When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate](https://arxiv.org/abs/2610.36852) | Robot Foundation / VLA | Marc Ziegler, Batu Özen, Sami Mentes, Thomas Waschulzik, Alois Knoll |
| [TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823) | Robot Foundation / VLA | Jeremy A. Collins, Seungjae Lee, Rachanon Wachakorn, Krishnan Srinivasan, Animesh Garg, Vitor Campagnolo Guizilini, Paarth Shah |
| [RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791) | World Model | Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li |
| [Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition](https://arxiv.org/abs/2610.36765) | Robot Foundation / VLA | Lifan Zheng, Guotao Chen, Zhenyang Li, Shujie Cui, Qiang Huang, Fan Liu |
| [Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution](https://arxiv.org/abs/2610.36761) | Robot Foundation / VLA | Zihan Zhang, Zeyu Wu, Xin Zhang, Mingyu Luo, Haohui Que, Tong Zhu |
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
