# Yudao Cloud 长期学习项目

通过真实业务请求理解大型服务如何组织，以及中间件为什么存在、如何接入、失效时会发生什么。

## 当前状态

2026-10-11：已获取 master-jdk17 后端源码，并确定 JDK 17 + Spring Boot 3.5、MySQL、Vue3 Element Plus。源码与文档由外层学习仓库统一管理，运行环境尚未验证，未启动服务。

学习方向来自前期讨论：以 **Yudao Cloud** 为主线，先完成登录与用户查询，再研究服务调用、缓存、异步处理和故障恢复。节奏按成果推进，不预设必须在几周内完成。

## 从这里开始

1. 查看 [学习路线](docs/ROADMAP.md)，明确第一阶段验收成果。
2. 查看 [环境记录](docs/ENVIRONMENT.md) 的源码基线，再核验工具与组件版本。
3. 获取源码后，按该版本官方说明建立最小运行环境，记录实际命令。
4. 跑通一次登录与用户查询，用 [请求追踪模板](docs/templates/REQUEST_TRACE.md) 记录完整链路。
5. 每次学习结束更新 [进度](docs/PROGRESS.md) 和 [交接](docs/HANDOFF.md)。

## 文档导航

| 文档 | 用途 |
|---|---|
| [AGENTS.md](AGENTS.md) | 后续 AI 协作、教学、修改和验证约定 |
| [ROADMAP](docs/ROADMAP.md) | 按成果划分的阶段与验收条件 |
| [ENVIRONMENT](docs/ENVIRONMENT.md) | 版本、依赖、启动与恢复记录 |
| [ARCHITECTURE](docs/ARCHITECTURE.md) | 源码地图与请求链路调查方法 |
| [EXPERIMENTS](docs/EXPERIMENTS.md) | 中间件实验清单和完成标准 |
| [PROGRESS](docs/PROGRESS.md) | 当前阶段、成果与问题 |
| [HANDOFF](docs/HANDOFF.md) | 下一次学习的最短上下文 |
| [RESOURCES](docs/RESOURCES.md) | 官方来源与版本核验规则 |
| [笔记模板](docs/templates/NOTE.md) | 概念、源码证据与理解记录 |
| [实验模板](docs/templates/EXPERIMENT.md) | 可复现实验及恢复记录 |
| [决策模板](docs/templates/DECISION.md) | 长期技术选择及重新评估条件 |

## 目录约定

```text
upstream/                  框架源码，纳入外层仓库
exercises/                 个人练习与独立演示
docs/notes/                源码与概念笔记
docs/experiments/          实验结果（含脱敏证据）
docs/decisions/            版本、组件等选择记录
docs/templates/            可复制模板
```

在根目录统一提交源码、文档和练习。upstream/ 按普通目录收录，保留上游 LICENSE 和原有 .gitignore；内层 Git 元数据备份在忽略的 local/yudao-cloud-git-backup/。根 .gitignore 排除依赖、构建产物、日志和本机私有配置；保留上游配置样例与锁文件。后续真实凭据放在被忽略的私有配置中，不直接写入上游样例。
