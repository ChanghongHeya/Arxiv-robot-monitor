# HCH arXiv Monitor

<!-- AUTO_RESULTS_START -->
## Latest Results

- Window: last 2 day(s)
- Updated at: 2026-11-21 07:56 UTC
- Relevant papers: 14

| Title | Type | Authors |
|---|---|---|
| [PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.26596) | Robot Foundation / VLA | Kai Lu, Chenyang Ma, Ioannis Havoutis |
| [PhyDEX: A Benchmark for Physical Reasoning in Vision-Language-Action Models via Dynamic Extrinsic Dexterity](https://arxiv.org/abs/2611.26565) | Robot Foundation / VLA | Hao Vo, Taisei Hanyu, Yuki Ikebe, Pham Tri Quang, Sreevenkata Anjani Tishita Godavarthi, Nghi D. Q. Bui, Daniel Sonntag, Chase Rainwater, Duy Minh Ho Nguyen, Anh Nguyen, Ngan Le |
| [Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation](https://arxiv.org/abs/2611.26444) | Robot Foundation / VLA | Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, Ziyi Xiong, Yang Li, Zhengwei Xie, Zhimin Wang, Zhen Liu, Jiazhen Huang, Yuzheng Zhang, Yuche Liu, Hongyi Yang, Chen Tang, Shixiang Tang, Hakan Aktas, Adam Wu, Duo Wu, Kangye Ji, Shuzhao Xie, Huanan Liu, Weijue Bu, Chenxin Li, Xinyuan Wang, Tianyi Bai, Yinan Mao, Jiawei Wang, Minglei Li, Heng Yu, Ehsan Adeli, Minchen Li, Yong-Lu Li, Cengiz Öztireli, Huazhe Xu, Chao Yu, Jing Zhang, Shanghang Zhang, Weitao Zhou, Wenwu Zhu, Cheng Chi, Jingyan Jiang, Zhi Wang |
| [Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models](https://arxiv.org/abs/2611.26438) | Robot Foundation / VLA | Zixuan Liu, Hashem Haghbayan, Zizhan Zheng, Siavash Khajavi |
| [Awaken-HI: Scaling Humanoid Intelligence with Whole-Body Human Experience](https://arxiv.org/abs/2611.26420) | Robot Foundation / VLA | EngineAI |
| [TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action](https://arxiv.org/abs/2611.26405) | Robot Foundation / VLA | Weile Li, Yunfan Lou, Muqing Shi, Zihao Zhang, Zhenbiao Huang, Boxian Yao, Xiyu Zhu, Zhibo Pang |
| [FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving](https://arxiv.org/abs/2611.26242) | Robot Foundation / VLA | Changtao Zhao, Yingxue Guan, Li Wang, Shijie Zhao, Yuhang Zhang, Shengkai Zhang, Qing Wang, Ziying Song |
| [Teaching Vision-Language-Action Models to Stop Safely](https://arxiv.org/abs/2611.26239) | Robot Foundation / VLA | Zheyuan Liu, Chuhan Wang, Jinduo Guo, Yue Huang, Xiangchi Yuan, Ningshan Ma, Meng Jiang |
| [SpecWM: Turning Verification into Refinement for Streaming World Models](https://arxiv.org/abs/2611.26211) | World Model | Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma |
| [One View, One Action: Spatially Generalizable VLAs through Observation-Aligned Experts and Cross Graph Consistency](https://arxiv.org/abs/2611.26161) | Robot Foundation / VLA | Jinxi Liu, Ruifeng Zhai, Hao Liu, Guangrun Wang |
| [Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models](https://arxiv.org/abs/2611.25980) | World Model | John Won, Yonghoon Dong, Jinwoo Shin |
| [Point Dynamics as Proxy for Robotic World Models](https://arxiv.org/abs/2611.25946) | World Model | Dong An, Tianyu Liu, Haoran Ding, Wen Yang, Anqing Duan, Zhengzhong Liu, Eric P. Xing, Guangyi Liu |
| [Fast-JEPA: Advancing the Success-Latency Frontier for Latent World Models](https://arxiv.org/abs/2611.25927) | World Model | Yao Zhang, Bin Yu, Shijie Lian, Haishan Liu, Changti Wu, Yu Wu, Kai Chen |
| [DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies](https://arxiv.org/abs/2611.25695) | Robot Foundation / VLA | Jun Xia, Shangwen Wang, Jun Ma, Ruichao Ren, Zhouyang Jia, Xin Zhao, Huijun Liu, Jie Yu |
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
