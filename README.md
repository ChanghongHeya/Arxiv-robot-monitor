# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-08-11 03:01 UTC
- Relevant papers: 20

| Title | Type | Authors |
|---|---|---|
| [Energy-Structured Latent World Models with Neural Time Fields for Physically Constistent Open-World Motion Planning](https://arxiv.org/abs/2608.09876) | Robot Foundation / VLA | Yapeng Liu, Yuanzhao Zhai, Bo Ding, Huaimin Wang, Lin Wang |
| [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853) | Robot Foundation / VLA | Dongchi Huang, Hongyin Zhang, Bohan Hou, Siteng Huang, Zhian Su, Hang Guo, Tong Lu, Zhaofeng Xu, Jiahao Tang, Jianfei Yang, Donglin Wang, Peixi Peng, Mingxiu Chen, Deli Zhao, Xin Li |
| [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) | Robot Foundation / VLA | Jingkai Wang, Zihan Tang, Gu Zhang, Mingyu Cao, Jiapeng Chen, Jingjiao Zhao, Xiansheng Chen, Pengwei Wang, Lemao Liu, Dejing Dou |
| [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) | Robot Foundation / VLA | Qu Tang, Benhui Zhuang, Bo Yuan, Xue Yu, Longteng Guo, Junlan Feng |
| [Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models](https://arxiv.org/abs/2608.09696) | World Model | Kevin Murphy |
| [Nonlinear Model Predictive Control of a Robotic Soft Esophagus](https://arxiv.org/abs/2608.09602) | World Model | Dipankar Bhattacharya, Ryman Hashem, Leo K. Cheng, Weiliang Xu |
| [verdi: retrieval is not transfer for continual world model optimization](https://arxiv.org/abs/2608.09537) | World Model | Junyu Wu, Shiqin Nie, Youyi Kou, Baohua Yin, Guocai Yao, Qingyu Chen, Jingheng Ma, Shiji Zhou, Hongyong Song, Mingchen Zhuge, Sen Cui, Changshui Zhang |
| [RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](https://arxiv.org/abs/2608.09467) | Robot Foundation / VLA | Boxiong Wang, Hui Kang, Geng Sun, Jiahui Li, Chao Yu, Daxin Tian |
| [VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction](https://arxiv.org/abs/2608.09448) | Robot Foundation / VLA | Hongjin Ji, Guoyang Xia, Luoyang Sun, Fangxiang Feng, Lei Ren |
| [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](https://arxiv.org/abs/2608.09410) | Robot Foundation / VLA | Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu |
| [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](https://arxiv.org/abs/2608.09381) | Robot Foundation / VLA | Yihan Lin, Jiawei He, Shifeng Bao, Chen Zhao, Yang Li, Xiaobo Wang, Yan Wang, Cheng Chi, Jing Zhang |
| [WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation](https://arxiv.org/abs/2608.09298) | World Model | Peterson Co, Sicheng Hu, Chunxuan Jiao, Hongyang Cheng, Yulin Luo, Yijie Xu, Sixiang Chen, Zhongxia Zhao, Zihao Wang, DaFeng Chi, Peidong Liu, YuTong Chen, Henghua Liu, Zhihao Yuan, Huizhu Jia, Yuzheng Zhuang, Tianle Zhang, Liang Lin, Huajie Tan, Shanghang Zhang |
| [Trajectory Divergence Horizon Decision for Reliable Dual-Arm Surgical Subtask Manipulation](https://arxiv.org/abs/2608.09125) | Robot Foundation / VLA | Mingwu Su, Guankun Wang, Jinsong Lin, Rulin Zhou, Ziyi Hao, Zhiwei Fang, Huxin Gao, Jiewen Lai, Jiazheng Wang, Fan Zhang, Hongliang Ren |
| [Latent World Models with Monotone Planning Costs for Image-Goal Navigation](https://arxiv.org/abs/2608.09073) | World Model | Amirhosein Chahe, Siwei Cai, Lifeng Zhou |
| [From Recovery to Drop-off: How Action Post-training Reduces a VLM's Late-Layer Depth Decodability](https://arxiv.org/abs/2608.08904) | Robot Foundation / VLA | Alexander Hackett, Arnaud Denis-Remillard, Axel Cassou |
| [Preview-Based Relative-Motion Control of an Insertion Tool for Neural-Thread Placement in Pulsating Tissue](https://arxiv.org/abs/2608.08860) | World Model | Yongyan Cao |
| [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](https://arxiv.org/abs/2608.08749) | Robot Foundation / VLA | Zhongxi Chen, Shenqi Zong |
| [WA-SpecDec: World-Aware Speculative Decoding for Vision-Language-Action Models](https://arxiv.org/abs/2608.08725) | Robot Foundation / VLA | Zikang Wen, Yuning Zhang, Dong Yuan |
| [Population-Scalable Multi-Agent World Modeling](https://arxiv.org/abs/2608.08600) | World Model | Renjie Zhao, Yuxiang Wu, Mingyu Zhang, Jiaxin Li, Sisi Li, Yimin Sheng, Tianxi Tan, Zhenkai Zhang, Jianyi Zhu, Yong-Lu Li |
| [Vid2WAM: Distilling Video Diffusion Priors into World Action Models](https://arxiv.org/abs/2608.08558) | Robot Foundation / VLA | Chenhao Qiu, Ruixiang Wang, Runyi Zhao, Sixu Lin, Songen Gu, Shufeng Nan, Guiliang Liu, Kui Jia, Yanwei Fu, Simo Wu |
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
