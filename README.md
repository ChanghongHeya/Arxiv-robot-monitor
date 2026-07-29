# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-07-29 04:08 UTC
- Relevant papers: 19

| Title | Type | Authors |
|---|---|---|
| [DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models](https://arxiv.org/abs/2607.25918) | World Model | Haoyuan Ji, Lingxiang Fan, Shang Su, Yinqiao Lu, Mengkai Shi, Jun Gao, Shuo Feng |
| [SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2607.25912) | Robot Foundation / VLA | Zonghe Liu, Shanyuan Jie, Xiaoquan Sun, Chen Cao, Zetian Xu, Zongsheng Liu, Jiayu Chen |
| [HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone](https://arxiv.org/abs/2607.25895) | Robot Foundation / VLA | Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang, Haoran Jia, Huan Du, Zicheng Zeng, Jun Ma, Guiyu Qin, Di Zhang, Xiaofei Li |
| [Shared Voxel-Map-Based Cooperative Indoor UAV Guidance with a Multi-Agent Soft Actor-Critic Controller](https://arxiv.org/abs/2607.25728) | World Model | Thomas Hickling, Dylan Wynne, Yu Su, Nabil Aouf |
| [A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models](https://arxiv.org/abs/2607.25516) | Robot Foundation / VLA | Haoyu Zhang, Yuwei Wu, Jin Chen, Gao Zhi, Zhenxin Diao, Mingyang Gao, Kun Wu, Yongchun Liu, Fan Li |
| [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/abs/2607.25487) | Robot Foundation / VLA | Minhyeok Lee, Chiyoung Kim, Chanhoe Gu, Seongrok Kim, Sanghyuk Roy Choi, Donghwan Hwang, Donghun Ryu, Seokhyun Kim |
| [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337) | World Model | Jiaxin Bai, Jiaxuan Xiong |
| [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/abs/2607.25236) | World Model | Jiaxin Bai, Jiaxuan Xiong |
| [Data Pyramid for Embodied Manipulation](https://arxiv.org/abs/2607.24744) | Robot Foundation / VLA | Yifan Ye, Yankai Fu, Yaoxu Lv, Bohan Hou, Jun Cen, Lingdong Kong, Duo Zheng, Tianxing Chen, Jiaming Liu, Ziang Cao, Yunfan Lou, Wei Chow, Xian Sun, Yingshuo Wang, Kuangzhi Ge, Xiaowei Chi, Xidong Zhang, Zhibo Pang, Yiwu Zhong, Sirui Han, Zhihe Lu, Weihao Yuan, Qifeng Chen, Michael Yu Wang, Yao Mu, Ziwei Liu, Jianfei Yang, Ping Luo, Shanghang Zhang |
| [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720) | World Model | Tianyi Men, Zhuoran Jin, Kang Liu, Jun Zhao |
| [τ: Learning Touch-Augmented Vision-Language-Action Models from Future Visual Supervision](https://arxiv.org/abs/2607.24485) | Robot Foundation / VLA | Ning Cheng, Jinan Xu, Wanlin Li, Yangzhi Chen, Jing Gao, Yiqun Wang, Kelan Peng, Wenjuan Han |
| [ArmnetBench v0.1: Parallel Real-World Evaluation of Manipulation Policies on a Low-Cost Arm Farm](https://arxiv.org/abs/2607.24481) | Robot Foundation / VLA | Praveen Selvaraj, Lorenzo Uttini, Ville Kuosmanen |
| [Model Predictive Planner for UAV Navigation in Non-Convex Air Corridors](https://arxiv.org/abs/2607.24369) | World Model | Henrique Silva, Marcelo A. Santos, Guilherme V. Raffo |
| [FeelWorld: Visuo-Tactile World Model for Hierarchical Contact Prediction and Planning](https://arxiv.org/abs/2607.24267) | World Model | Wenxuan Ma, Chaofan Zhang, Chao Xue, Yinghao Cai, Guocai Yao, Shaowei Cui, Shuo Wang |
| [DeVA: Decoupled Video-Action Model with physical guidance for robot policy learning](https://arxiv.org/abs/2607.24159) | Robot Foundation / VLA | Mengqi Zhang, Sahil Khose, Simar Kareer, Yuchen Song, Unnat Jain, Judy Hoffman |
| [A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference](https://arxiv.org/abs/2607.24148) | Robot Foundation / VLA | Zhuoran Song, Haozhe Jiang, Chunyu Qi, Minnan Pei, Gang Li, Xiaoyao Liang, Haibing Guan |
| [Scaling GUI Agents with Visual State Transitions](https://arxiv.org/abs/2607.24112) | World Model | Xiangyan Liu, Kaixin Li, Haonan Wang, Biao Wu, Meng Fang, Longxu Dou, Chao Du, Michael Qizhe Shieh, Tianyu Pang |
| [Moving-Horizon Estimation and Nonlinear Model Predictive Control of Cable-Driven Soft Manipulators](https://arxiv.org/abs/2607.24029) | World Model | Lingxiao Xun, Haihong Li, Gang Zheng |
| [FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking](https://arxiv.org/abs/2607.24008) | Robot Foundation / VLA | Hai Jiang, Yixian Zou, Binbin Liang, Boqian Liu, Fanman Meng, Shuaicheng Liu |
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
