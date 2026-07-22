# 贡献指南与开放任务

### 如何新建章节

自行操作时参见操作实例 Commit 6023cc8[EB/OL]. [2026-03-26]. <https://github.com/FreeBSD-Ask/FreeBSD-Ask/commit/6023cc8d58f3a1b9849ff11fa63bf3980177c370> 和下方 `SUMMARY.md` 结构说明。

若有困难可发邮件联系 ykla 协助操作。

#### `SUMMARY.md` 目录结构

```md
# Table of contents

* [FreeBSD 从入门到跑路](README.md)
* [编辑日志](CHANGELOG.md)
* [贡献指南与开放任务](CONTRIBUTING.md)
* [目录](mu-lu.md)

## 前言

* [前言](qian-yan/qian-yan.md)
* [致读者](qian-yan/zhi-du-zhe.md)
* [致谢](qian-yan/zhi-xie.md)
* [绪论](qian-yan/xu-lun.md)

## 第 1 章 FreeBSD 初见

* [1.1 操作系统的历程：UNIX、BSD 和 Linux](di-1-zhang-zou-jin-freebsd/di-1.1-unix.md)
* [1.2 FreeBSD 导论](di-1-zhang-zou-jin-freebsd/di-1.2-dao-lun.md)
* [1.3 George Berkeley（乔治·贝克莱）与 BSD 命名的文化背景](di-1-zhang-zou-jin-freebsd/di-1.3-jie-freebsd-jian-shi.md)
* [1.4 加州大学伯克利分校和“Fiat Lux”（要有光）](di-1-zhang-zou-jin-freebsd/di-1.4-Fiat-Lux.md)

## 第 2 章 安装 FreeBSD

* [2.1 安装前的准备工作](di-2-zhang-an-zhuang-freebsd/di-2.1-install-pre.md)
* [2.2 使用 bsdinstall 开始安装](di-2-zhang-an-zhuang-freebsd/di-2.2-jie-start-install.md)
* [2.3 键盘布局和主机名](di-2-zhang-an-zhuang-freebsd/di-2.3-jie-use-bsdinstall.md)
* [2.4 选择安装组件](di-2-zhang-an-zhuang-freebsd/di-2.4-jie-select.md)
* [2.5 分配磁盘空间](di-2-zhang-an-zhuang-freebsd/di-2.5-jie-fen-pei-disk.md)
* [2.6 设置 root 密码](di-2-zhang-an-zhuang-freebsd/di-2.6-root-jie.md)
* [2.7 网络设置](di-2-zhang-an-zhuang-freebsd/di-2.7-jie-net.md)
* [2.8 时区、服务、安全、固件和账户](di-2-zhang-an-zhuang-freebsd/di-2.8-jie-more.md)
* [2.9 完成安装](di-2-zhang-an-zhuang-freebsd/di-2.9-end-jie.md)
* [2.10 故障排除](di-2-zhang-an-zhuang-freebsd/di-2.10-jie-eol.md)
* [2.11 将 U 盘启动盘恢复为普通 U 盘（基于 Windows）](di-2-zhang-an-zhuang-freebsd/di-2.11-jie-usb.md)

其他从略
```

可以看到，`SUMMARY.md` 在形式上就是普通的 Markdown 文档，并无特殊支持。

但有一些注意事项：

- 第一行 `# Table of contents` 绝对不允许变更，否则 GitBook 将无法识别，导致失去同步。
- 要求格式应为 `* [2.2 使用 bsdinstall 开始安装](di-2-zhang-an-zhuang-freebsd/di-2.2-jie-start-install.md)`，不允许出现 `* [2.2 使用 bsdinstall 开始安装](di-3-zhang-ni-hao/di-2.2-jie-start-install.md)` 这种情况，即目录结构与文件放置位置必须一致（不一致虽不会报错，但本项目要求保持一致）。
- 通过 `sync-headers.yml`，将自动同步 `SUMMARY.md` 中的章节标题到具体的 Markdown 文件中。因此若需修改 `di-2.2-jie-start-install.md` 的一级标题 `# 2.2 使用 bsdinstall 开始安装`，必须仅修改 `SUMMARY.md` 中的 `2.2 使用 bsdinstall 开始安装`，否则会被 `sync-headers.yml` 覆盖。当二者不一致时，若提交时未触发脚本构建，则 GitBook 将以 `SUMMARY.md` 中的目录为准。

### 预览页面

当您提交 PR 时，系统会自动生成一个预览网站。

实际上，所有提交都有对应的网站版本：

![GitHub PR 页面](.gitbook/assets/yu-lan1.png)

您可通过该链接获取当前 PR 的实际显示样式：

![GitHub PR 页面](.gitbook/assets/yu-lan2.png)

![GitBook 预览页面](.gitbook/assets/yu-lan3.png)

且每次 push 都会自动更新：

![GitBook 预览页面](.gitbook/assets/yu-lan4.png)
