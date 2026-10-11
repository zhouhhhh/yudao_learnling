# 001 初始学习技术栈评估

- 日期：2026-10-11
- 决策状态：被替代，用户最终选择见 [002 采用技术栈](002-ADOPTED_STACK.md)。下文保留初次评估依据，不作为当前配置。
- 验证状态：进行中。已阅读远程官方资料，未获取源码、编译或启动。

## 背景与建议

目标是学习大型服务和中间件，同时学习 PostgreSQL。建议主线采用 JDK 21 + master-jdk17（Boot 3.5 系列）+ PostgreSQL + Vue3 Element Plus；JDK 25 + master-jdk25（Boot 4 系列）在基础闭环完成后作为升级对照实验。该建议是学习成本判断，不是两个分支运行稳定性的实测结论。

17、21、25 都属于 LTS 版本；JDK 25 并非短期版本。选择 21 是为了保留较新的 Java 学习入口，同时减少 Boot 大版本适配与 PostgreSQL 适配一起引入的变量。master-jdk17 根 POM 网页快照的 java.version 是 17；使用 JDK 21 构建不等于项目自动使用 Java 21 语法或开启虚拟线程。首先保持上游编译目标。

## 来源与证据边界

- [17 分支根 POM](https://github.com/YunaiV/yudao-cloud/blob/master-jdk17/pom.xml)：网页显示 java.version=17、Boot=3.5.15。
- [25 分支根 POM](https://github.com/YunaiV/yudao-cloud/blob/master-jdk25/pom.xml)：网页显示 java.version=25、Boot=4.1.0。
- [25 分支 BOM](https://github.com/YunaiV/yudao-cloud/blob/master-jdk25/yudao-dependencies/pom.xml)：网页显示 Boot=4.1.1，与根 POM 快照不同。不同网页抓取时间可能造成差异，也可能是源码配置差异；必须获取同一 commit 后核验，不能直接判断构建失败。
- [Boot 4 迁移指南](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide)：用于调查模块化、Jackson 和第三方组件适配变化。
- [Java 支持路线](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)：17、21、25 的 LTS 定位；具体发行版支持另行确认。

这些小版本只代表本次远程网页观察，不作为固定源码基线或依赖可下载的证明。完整 SHA 待拉取后记录。

## PostgreSQL

[官方启动说明](https://cloud.iocoder.cn/quick-start/)明确允许 PostgreSQL，同时提醒非 MySQL SQL 脚本可能滞后。[MyBatis starter POM](https://github.com/YunaiV/yudao-cloud/blob/master-jdk17/yudao-framework/yudao-spring-boot-starter-mybatis/pom.xml)声明 PostgreSQL JDBC 驱动为 optional；获取源码后按该 commit 检查运行服务是否真正包含驱动，按官方方式调整。

首次验收应检查：实际 PostgreSQL SQL 脚本位置与完整性、连接 URL/驱动、主键生成或序列、分页与自定义 SQL、布尔及时间字段、初始化权限/租户数据。先验证 system 与 infra 的必要功能，不推断所有业务模块均兼容。此次未成功读取 PostgreSQL SQL 文件，路径与内容仍待本地核验。

业务数据库选择 PostgreSQL 不代表 Nacos、XXL-Job 等组件内部存储自动使用 PostgreSQL。开发期优先按所选版本官方单机说明运行 Nacos，其内部存储需求独立核验。

## 前端

用户指定：https://gitee.com/yudaocode/yudao-ui-admin-vue3 。本次 Gitee 页面未能读取，改查 repository 字段指向该 Gitee 仓库的 [GitHub package.json](https://github.com/yudaocode/yudao-ui-admin-vue3/blob/master/package.json)。网页 engines 为 Node >=20.19.0、pnpm >=8.6.0；实际版本以用户获取的 commit、锁文件与构建工具要求为准，不据此保证两个托管平台内容完全同步。

[.env.dev](https://github.com/yudaocode/yudao-ui-admin-vue3/blob/master/.env.dev)指向远程演示后端；[.env.local](https://github.com/yudaocode/yudao-ui-admin-vue3/blob/master/.env.local)默认本地地址。拉取后检查启动脚本实际加载的 mode，并将 API 地址匹配实际 Cloud 网关，不能仅凭前端页面打开认定本地系统跑通。

## 其余选择与重新评估

基础阶段继续使用框架配套的 Redis、Nacos 与 Gateway，版本依当前源码确认。仍需选择安装方式、实际启动模块；队列、调度、追踪等到相关阶段再选，不一次安装全部。

如果用户更希望研究最新框架、愿意处理兼容性，或固定 SHA 的 25 分支通过最小构建与 PostgreSQL 闭环，则可直接选择 25 主线。学习基线建立后不持续自动追最新提交。
