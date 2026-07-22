# CLAUDE.md

## 项目概述

本项目是一本基于 AMI BIOS 的 UEFI/BIOS 注解 GitBook 电子书，提供全注全译，帮助读者理解系统启动相关设置。项目遵循 BSD 2-Clause 许可证，作者为 ykla <yklaxds@gmail.com>。

## 目录结构

```
UEFI-Book/
├── README.md                          # 项目首页
├── SUMMARY.md                         # GitBook 目录（首行必须为 # Table of contents）
├── mu-lu.md                           # 自动生成的目录（由 mulu.yml 从 SUMMARY.md 同步）
├── CONTRIBUTING.md                    # 贡献指南
├── CLAUDE.md                          # 本文件
├── LICENSE                            # BSD 2-Clause 许可证
├── .autocorrectrc                     # AutoCorrect 配置
├── .markdownlint.json                 # markdown-lint2 配置
├── .gitbook/assets/                   # GitBook 图片资源
├── .github/workflows/                 # CI/CD 工作流
│   ├── sync-headers.yml               # 标题同步（SUMMARY.md → 文件首行 H1）
│   ├── mulu.yml                       # 目录同步（SUMMARY.md → mu-lu.md）
│   └── create-pdf.yml                 # PDF/EPUB 生成（每周日 UTC 15:30）
├── uefi-bios/                         # UEFI/BIOS 概述与警告（7 个子文件）
├── main/                              # Main 主菜单（6 个子文件）
├── advanced/                          # Advanced 高级（22 个子文件）
├── chipset/                           # Chipset 芯片组（2 个子文件）
├── security/                          # Security 安全（5 个子文件）
├── boot/                              # Boot 启动（21 个子文件）
├── save-exit-bao-cun-yu-tui-chu.md    # Save & Exit 保存与退出（无 H2，不拆分）
└── script/                            # 临时脚本目录（不需要清理）
```

每章顶级目录内同时包含父页面文件（保留 H1 + 简介 + 菜单截图）和拆分后的子文件（每个 H2 一个独立文件）。

## GitBook 规范

### SUMMARY.md 约束

- 首行 `# Table of contents` 绝对不允许变更，否则 GitBook 无法识别
- 目录结构与文件放置位置必须一致：`* [标题](路径)` 中的路径必须与实际文件位置匹配
- 子条目使用 2 空格缩进
- 格式：`* [标题](目录/文件名.md)`，子条目为 `  * [标题](目录/子文件名.md)`

### 工作流机制

- **sync-headers.yml**：自动从 SUMMARY.md 同步章节标题到 Markdown 文件首行 H1。修改文件一级标题必须仅修改 SUMMARY.md 中的标题，否则会被覆盖
- **mulu.yml**：当 SUMMARY.md 变更时，自动生成 mu-lu.md（将首行 `# Table of contents` 替换为 `# 目录`）
- **create-pdf.yml**：每周日 UTC 15:30 自动生成 PDF 和 EPUB，使用 gitbook-pdf-export 工具遍历 SUMMARY.md 结构

### 标题同步规则

每个 Markdown 文件首行必须为 `# <标题>`，且与 SUMMARY.md 中对应条目的方括号标题完全一致。这是 sync-headers.yml 工作的前提。

## 格式规则

### 标点符号

- 全书正文标点符号统一使用全角（包括“”、括号、冒号等）
- 禁止使用「」『』符号，一律替换为“”或‘’
- 双引号使用“”或‘’，不使用半角 "" 或 ''
- 避免中文标点（尤其是“”）一侧或两侧新增空格

### 路径与 IP

- 全书正文中的路径（带 \\）和 IP 地址使用**加粗**，不使用行间代码
- 转义字符 \\ 相关的元素使用行间代码包裹，不使用转义字符

### 命令与选项

- 选项、可调选项、命令、可调参数等使用行间代码包裹
- 不带选项或参数的裸命令不使用行间代码格式，继续裸着不加任何包裹
- 手册页引用使用 **命令(N)** 加粗格式（如 **vt(4)**），不得使用反引号或点号格式

### 中英文排版

- 中英文之间有空格
- 代码块中的英语注释翻译为中文
- fstab 不翻译
- pkgbase 不翻译
- “package” / “packages” 翻译为“软件包”（代码块和命令输出中的 package 保留英文）
- GSoC 翻译为“编程之夏”

### 段落与结构

- 一段内容必须在一行内，不同段落必须换行
- 中文标题前后多余空格需清理
- 避免滥用“已”字（如“XX 已新增”应改为“新增 XX”）
- 避免滥用“一个 xx”这种翻译
- 避免不地道的汉语语法（病句、后置于、倒装句等欧化汉语现象）
- 修正“xx yy”类倒置结构（如“xx 可调参数”应改为“可调参数 xx”）
- 书名、作品名、商标、动漫名词需用标点标注清楚，写完整准确

### 其他

- 文件名加粗，不篡改
- 不要篡改软件版本号
- 不要篡改用户名
- 中文复数用单数 Port
- 删除、改写纯粹的骂人句子或字词时，直接删除脏字修饰语，不用替换词

## 事实核查方法论

### 核心原则

- 必须通过多个一手来源交叉确认
- 不信任中文互联网来源（博客、论坛、百度百科等）
- 不篡改任何既有参数值（选项名称、数值范围、寄存器地址、默认值等），仅允许格式调整和拼写修正
- 校对过程须留痕，记录核查来源

### 优先来源

1. Intel 数据手册（Intel Datasheet）
2. UEFI 规范（UEFI Specification）
3. JEDEC 标准
4. PCI-SIG 规范
5. USB-IF 规范
6. AMI 文档
7. ACPI 规范
8. 厂商官方文档（如 Intel、AMI 官方技术文档）

### 工作流程

1. 逐行逐句子遍历内容检查逻辑一致性
2. 联网复核后修改
3. 对于不存在的实际访问查询需联网复查三次后修改
4. 不得以任何方式搜索、批量、绕过逐句子审查
5. 修改时禁止机械修改，禁止批量，需逐个修改
6. 修改前后需复核
7. 禁止参考 FreeBSD Handbook

## 自动清理工具

### 工具配置

- **AutoCorrect**：配置文件 `.autocorrectrc`
  - 规则：space-word:1, space-punctuation:1, fullwidth:1, no-space-fullwidth:1, no-space-fullwidth-quote:1
  - codeblock: 0（不格式化代码块）
- **md-padding@latest**：中英文间距处理
- **markdown-lint2**：配置文件 `.markdownlint.json`
  - 关键规则：MD001, MD003, MD009, MD024 (siblings_only:true), MD041, MD049 (asterisk), MD050 (asterisk), MD060 (compact, aligned_delimiter)

### 使用流程

1. 禁止批量接受或默认接受工具输出
2. 必须逐个结合上下文综合复核每条建议
3. 修改前复核一次（确认建议合理）
4. 修改后复核一次（确认未引入新问题）
5. 全部文件清理完成后，进行一次总复核
6. 特别注意避免中文标点（尤其是“”）一侧或两侧新增空格

### 注意事项

- AutoCorrect 的 `no-space-fullwidth: 1` 和 `no-space-fullwidth-quote: 1` 规则确保全角标点附近无空格
- 如工具在中文标点一侧或两侧新增空格，拒绝此类修改
- 不得使用软件工具批量替代逐个复核，必须逐个手动逐行修改

## 构建流程

### 本地预览

使用 GitBook 进行本地预览。

### CI/CD

- **push 时**：sync-headers.yml 同步标题，mulu.yml 更新 mu-lu.md
- **每周日 UTC 15:30**：create-pdf.yml 生成 PDF 和 EPUB，发布到 GitHub Releases
- **PR 提交时**：系统自动生成预览网站

## 文件编码规范

- 所有文件使用 UTF-8 编码，禁止使用 BOM 标记
- 换行符统一使用 LF
