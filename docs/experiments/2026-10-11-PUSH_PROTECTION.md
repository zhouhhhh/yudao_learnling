# 上游 SQL 样例触发推送保护

- 日期：2026-10-11
- 状态：进行中（工作区修复已验证，提交历史与远端推送待处理）
- 学习仓库原提交：f096217a9d6f8f9f51014f32ef325ee323bdb00e，当前只有一个提交。

## 现象与原因

引用聊天“排查 Git 推送失败”的日志为 GH013 / Push cannot contain secrets，指向上游 SQL 的对象存储与短信渠道初始化数据。.gitignore 不能判断文件内容是否含密钥，也不会清除已经提交的内容。之前仅检查忽略规则，遗漏了样例 SQL 凭据检查。

## 修改

保留初始化脚本，仅将 9 种数据库脚本中 36 条相关 INSERT 的 accessKey/accessSecret 或短信 api_key/api_secret 换成 REPLACE_WITH_YOUR_ACCESS_KEY_ID 与 REPLACE_WITH_YOUR_ACCESS_KEY_SECRET。未确认原值真伪，不按误报放行。真实云存储与短信功能需要使用自己的私有配置，这些占位符不能用于实际调用。

新增 scripts/check_secrets.py，检查常见 AKID/LTAI/AKLT 格式，不输出密钥值。补齐根 .gitignore 的 backups/、dumps/ 与凭据文件规则，继续保留初始化 SQL。

## 验证与局限

- python scripts/check_secrets.py：工作区中已跟踪文件未发现目标格式。
- python scripts/check_secrets.py --history：仍在原提交的 9 个 SQL 文件中发现目标格式，符合尚未替换提交的状态。
- git diff --check：通过；9 个 SQL 文件各只修改 4 行。
- git check-ignore：备份、导出、local/ 与凭据文件被忽略。

尚未导入数据库，不宣称 SQL 运行验证通过。此脚本是针对本次云 Access Key 格式的补充检查，不能覆盖 GitHub 的全部密钥类型。

## 后续操作

当前只有首次提交，且日志显示该推送被拒绝。工作区改动确认后，在根目录执行：

```powershell
git add .
git commit --amend --no-edit
python scripts/check_secrets.py --history
```

只新增提交无法移除旧提交内容。再次推送前须确保历史检查通过；远端成功与否以实际结果为准。本次未改写提交或推送。
