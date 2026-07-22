# 变更日志

本文件记录了为覆盖 Intel 最新平台（截至 2026 年 7 月，包括 Panther Lake、Arrow Lake Refresh、Arrow Lake-S、Arrow Lake 移动版、Lunar Lake）而新增的 AMI BIOS 配置选项，以及相关参考文档的存档位置。

## 参考文档存档位置

以下参考文档的原始文件存档于项目 `en/` 目录下，供查阅核对：

| 参考文档 | 存档路径 |
| -------- | -------- |
| UEFI Specification, Version 2.11（2024-12-01） | `en/common/uefi-forum-uefi-specification-2.11-20241201.pdf` |
| ACPI Specification, Version 6.6（2025-05-01） | `en/common/uefi-forum-acpi-specification-6.6-20250501.pdf` |
| UEFI Platform Initialization (PI) Specification, Version 1.9（2024-12-01） | `en/common/uefi-forum-pi-specification-1.9-20241201.pdf` |
| UEFI Shell Specification, Version 2.2 | `en/common/uefi-forum-uefi-shell-specification-2.2.pdf` |
| Intel® Core™ Ultra 200S/200S Plus/200HX/200HX Plus Series Processors Datasheet, Vol. 1（Rev. 007，2026-03） | `en/arrow-lake-refresh/intel-200s-200hx-processors-datasheet-vol1.pdf` |
| Intel® 800 Series Chipset Family PCH Datasheet, Vol. 1（Rev. 003，2025-02） | `en/arrow-lake-refresh/intel-800-series-pch-datasheet-vol1.pdf` |
| Intel® NUC Aptio V BIOS Glossary, Rev. 2.0（2020-02） | `en/panther-lake/intel-nuc-aptiov-bios-glossary-202002-rev2.0.pdf` |
| Gigabyte. BIOS Setup (Intel® 800 Series)（2024-10） | `en/arrow-lake-s/gigabyte-intel800-bios-setup-guide-en-20241010.pdf` |
| ASUS NUC 16 Pro Specifications（2025-12） | `en/panther-lake/asus-nuc-16-pro-datasheet-202512.pdf` |

## 新增选项记录

### advanced/cpu-configuration.md

以下选项为 Intel 800 系列芯片组平台（Arrow Lake-S/Arrow Lake Refresh，LGA 1851 插槽）及 Panther Lake 移动平台 AMI Aptio V BIOS 中新增的 CPU 配置项，依据技嘉 Intel 800 系列 BIOS Setup Guide 记载。这些选项已合并至原文相应位置：

- Enhanced Multi-Core Performance（增强多核性能）——合并至 Hyper-Threading 之后
- Performance CPU Clock Ratio（性能核心时钟倍频）——合并至 CPU Flex Ratio Settings 之后
- Efficiency CPU Clock Ratio（能效核心时钟倍频）——同上
- Max Ring Ratio（最大环形总线倍频）——同上
- Min Ring Ratio（最小环形总线倍频）——同上
- IGP Ratio（核显倍频）——同上
- NGU Ratio（NGU 倍频）——同上，Panther Lake 平台新增
- CPU D2D Ratio（CPU Die-to-Die 倍频）——同上
- Core Minimum Ratio（核心最小倍频）——同上
- BCLK Output Source（基准时钟输出源）——同上
- CPU Cores Enabling Mode（CPU 核心启用模式）——合并至 Active Efficient-cores 之后
  - No. of CPU P-Cores Enabled（启用的性能核心数量）
  - No. of CPU E-Cores Enabled（启用的能效核心数量）
  - Active P-Core/E-Core（激活的 P 核心/E 核心）
- CPU Over Temperature Protection（CPU 过温保护）——合并至 Total Memory Encryption 之后
- Tcc Activation Offset（TCC 激活偏移）——同上
- Tcc Offset Time Window（TCC 偏移时间窗口）——同上
- CEP（Current Excursion Protection，电流漂移保护）——同上
- Core Ratio Extension Mode（核心倍频扩展模式）——同上
- Frequency Clipping TVB（热感知睿频频率裁剪）——同上
- Enhanced TVB（增强型热感知睿频加速）——同上
- Voltage Reduction Initiated TVB（热感知睿频电压降低）——同上
- Intel(R) Innovation Platform Framework（英特尔创新平台框架）——同上

### advanced/usb-configuration.md

以下选项为 Intel 800 系列芯片组平台 AMI Aptio V BIOS 中新增的 USB4/Thunderbolt™ 配置项，已合并至原文相应位置：

- PCIE Tunneling over USB4（USB4 上的 PCIe 隧道）
- USB4 CM Mode（USB4 连接管理器模式）
- Integrated Thunderbolt™ Enable（集成 Thunderbolt™ 控制器启用）
- USB4 Host Router Class Code（USB4 主机路由器类代码）

### advanced/nvme-configuration.md

以下选项为 Intel 800 系列芯片组平台 AMI Aptio V BIOS 中新增的 VMD 卷管理设备配置项，已合并至原文相应位置：

- VMD Setup（VMD 卷管理设备设置）
  - Enable VMD Controller（启用 VMD 控制器）
  - Enable VMD Global Mapping（启用 VMD 全局映射）
  - Map this Root Port under VMD（在 VMD 下映射此根端口）

### advanced/acpi-settings.md

以下选项为 Intel 800 系列芯片组平台 AMI Aptio V BIOS 中新增的 ACPI 配置项，已合并至原文相应位置：

- Platform Power Management（平台电源管理）
- PEG ASPM（PEG 活动状态电源管理）
- PCH ASPM（PCH 活动状态电源管理）
- DMI ASPM（DMI 活动状态电源管理）
- S3 Save Mode（S3 节能模式）
- ErP（ErP 指令）
- RC6（Render Standby，渲染待机）

### advanced/power-performance.md

以下内存相关选项为 Intel 800 系列芯片组平台 AMI Aptio V BIOS Tweaker 菜单中的配置项，已合并至原文 GT - Power Management Control 节末尾（待后续 chipset 章节对照补充时进一步调整位置）：

- DDR5 XMP Booster（DDR5 XMP 增强器）
- A.I. XMP Booster Profile（A.I. XMP 增强器配置文件）
- Extreme Memory Profile (X.M.P.)（极速内存配置文件）
- System Memory Multiplier（系统内存倍频）
- High Bandwidth（高带宽模式）
- Low Latency（低延迟模式）

注：原拟新增的 Intel(R) Speed Shift Technology、CPU Thermal Monitor、CPU EIST Function、Race To Halt (RTH)/Energy Efficient Turbo、Intel(R) Turbo Boost Technology、Active Turbo Ratios、Turbo Power Limits 经复核均为 CPU - Power Management Control 节中既有选项（如 Intel(R) SpeedStep(tm)、Race To Halt (RTH)、Intel(R) Speed Shift Technology、Turbo mode、View/Configure Turbo Options、Thermal Monitor、Platform PL1/PL2 等）的简写重复版本，已删除，保留原文更详细的描述。

### chipset/pch-io-configuration.md

以下为依据 Intel 800 系列芯片组 PCH 数据手册（Vol 1，rev 003，2025-02）对既有选项的补充说明，已合并至原文相应位置：

- PCIe Speed（PCIe 速率）：补充 Gen4: PCIe 4.0 (16.0 GT/s) 选项，并标注 Intel 800 系列芯片组 PCH-S 控制器最大传输速率为 16 GT/s（Gen4），支持 14 个根端口、24 条通道
- DMI Link ASPM Control（DMI 链路 ASPM 控制）：补充 Intel 800 系列芯片组 PCH-S PCIe 控制器不支持 L0s 链路状态，仅支持 L1 子状态（L1.0/L1.1/L1.2）
- DPC（下行端口控制）：补充 Intel 800 系列芯片组 PCH-S 控制器不支持 DPC
- EDPC（增强型下行端口控制）：补充 Intel 800 系列芯片组 PCH-S 控制器不支持 eDPC
- Transmitter Half Swing（发送器半摆幅模式）：补充 Intel 800 系列芯片组 PCH-S 控制器不支持半摆幅模式
- SATA Mode Selection（SATA 模式选择）：补充 Intel 800 系列芯片组 SATA 控制器不支持 IDE 传统模式，仅支持 AHCI 与 RAID 模式
- THC Configuration（触控主机控制器配置）：补充 THC-SPI 不适用于 Intel Core Ultra 200S 系列桌面处理器平台
- SerialIo Configuration（串行 IO 配置）：补充 Intel 800 系列芯片组在 Serial I/O 子系统中新增 I3C 控制器（符合 MIPI I3C HCI 规范），ISH 升级至 5.6 版本且 ISH 接口新增 I3C 支持
- ISH Configuration（整合传感器中枢配置）：补充 Intel 800 系列芯片组搭载 ISH 5.6 版本，ISH 接口新增 I3C 支持

## 存疑条目记录（2026-07 国外搜索引擎重新检索）

本节记录校对过程中无法从 Intel 一手文档完全确认的存疑项。所有条目均使用国外搜索引擎（Google/Bing/DuckDuckGo 等）以全拼关键字词重新检索，不使用中国搜索引擎，不信任中文互联网来源。仅记录，不在正文注释。

### SA Configuration（sa-configuration.md）

#### 存疑 1：PSMI 全称展开
- 原文：PSMI，Power Supply Management Interface，电源供应管理接口
- 检索关键词："Power Supply Management Interface" Intel、PSMI Intel datasheet、Intel server BIOS PSMI support option
- 检索结果：中文来源（中国专利 xjishu.com、CSDN 文库）对两种全称说法矛盾，未找到 Intel 一手英文文档确认
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 2：IBECC 性能损失 "五分之一"（20%）
- 原文：根据实际测试最高可降低五分之一的内存性能
- 检索关键词：IBECC Intel performance overhead、"In-Band ECC" Intel performance、Intel IBECC memory performance impact
- 检索结果：Intel ARK 确认 "In Band ECC" 术语存在，但未披露性能损失数据；中文非权威来源提到的性能损失数据（3-5ns 延迟、5-8% 帧率波动）远低于 20%；未找到任何可靠来源支持 20% 数据
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 3：IBECC 非对称内存触发启用
- 原文：如果内存配置为非对称（asymmetric，内存混用），则该功能将被启用
- 检索关键词：IBECC asymmetric memory Intel、"In-Band ECC" asymmetric memory、Intel IBECC mixed memory
- 检索结果：未找到 Intel 官方文档说明非对称内存配置会触发 IBECC 自动启用
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 4：CVF = Intel Clover Falls
- 原文：CVF，Intel Clover Falls，是英特尔推出的一种 AI 协处理器
- 检索关键词："Intel Clover Falls"、"CVF" Intel AI coprocessor、Intel Visual Sensing Controller
- 检索结果：CCF Chip 论坛与 Dell 官方页面确认 Clover Falls = Intel Visual Sensing Controller（研发代号），是 Intel EVO 平台低功耗 AI 协处理器；但 "CVF" 缩写本身未在 Intel 公开文档中明确定义
- 核查结论：部分确认（Clover Falls = Intel Visual Sensing Controller 确认；CVF 缩写来源未确认）
- 当前处理：正文已修改为 "CVF（BIOS 选项缩写），对应 Intel Visual Sensing Controller（研发代号 Clover Falls）"

#### 存疑 5：DDR5 频率 10000、12800
- 原文：Maximum Memory Frequency 选项列表包含 10000、12800
- 检索关键词：DDR5 10000 MT/s、DDR5 12800 MT/s、DDR5 maximum frequency overclock
- 检索结果：10000 MT/s 属消费级超频（XMP/EXPO）范畴；12800 MT/s 属极限超频世界纪录范畴，同时也是 JEDEC MRDIMM Gen2 服务器标准的未来目标速率；两者均非 JEDEC 标准消费级速度（4800/5600/6400 MT/s）
- 核查结论：确认属超频/未来标准范畴
- 当前处理：正文保留参数值，已补充说明 "10000、12800 属超频（XMP）或未来 MRDIMM 标准范畴，非 JEDEC 标准消费级速度"

### PCH-IO Configuration（pch-io-configuration.md）

#### 存疑 6：FIA 全称 "Flexible I/O Adapter"
- 原文：FIA（Flexible I/O Adapter）
- 检索关键词："Flexible I/O Adapter" Intel PCH、FIA Intel chipset datasheet、Intel 600/700/800 series PCH FIA flexible IO
- 检索结果：Intel 官方文档中确有 "Flexible I/O" 特性描述（指 PCH 可将高速 I/O 端口灵活配置为 PCIe/USB3.0/SATA），但未找到 FIA 缩写的官方定义
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 7：IEH 全称 "Isolated Execution Hardening"
- 原文：IEH，Isolated Execution Hardening，隔离执行加固
- 检索关键词："Isolated Execution Hardening" Intel、IEH Intel BIOS、"Isolated Execution Hardware" Intel SGX
- 检索结果：未在 Intel 官方文档（数据手册、SGX/TXT 白皮书、BIOS 写作指南）中找到 IEH 缩写的官方定义
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 8：PCIe ASPM 引入版本
- 原文：PCI Express 2.0 规范规定了两种低功耗模式：L0s 和 L1 模式
- 检索关键词：PCIe ASPM L0s L1 specification version、"Active State Power Management" PCIe 1.1、PCI Express ASPM introduced version
- 检索结果：未在 PCI-SIG 官方文档中找到 ASPM 首次引入的具体规范版本；多个非官方来源暗示 ASPM 属于 "早期 PCIe" 特性（疑似 1.0/1.1 时代即存在）；无权威来源明确指出 ASPM 在 PCIe 2.0 才首次规定
- 核查结论：未能确认（版本号 "2.0" 既无法确认也无法否定）
- 当前处理：保留原文

#### 存疑 9：HDA Link 频率选项 6/12/24 MHz
- 原文：HDA Link 频率选项 6 MHz / 12 MHz / 24 MHz
- 检索关键词："HDA Link" frequency Intel、Intel HD Audio Link BCLK 24MHz、"High Definition Audio" specification 24.576 MHz
- 检索结果：Intel HD Audio 规范定义的标准 BCLK 为 24.576 MHz（可二分频为 12.288 MHz）；未在 Intel 官方一手文档中找到 "6/12/24 MHz" 三个离散 BIOS 选项值的直接依据
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 10：iDisplay Audio Link 频率 48/96 MHz
- 原文：iDisplay Audio Link 频率 48 MHz / 96 MHz
- 检索关键词："iDisplay Audio Link" frequency、Intel iDisplay Audio 48 MHz 96 MHz、Intel display audio link BCLK
- 检索结果：Intel 官方 Meteor Lake 数据手册中存在 "Intel Display Audio Interface" 章节，但具体的 "48/96 MHz" 频率选项值未在 Intel 官方一手文档中找到直接依据
- 核查结论：未能确认
- 当前处理：保留原文

#### 存疑 11：PSE 使用 ARM Cortex-M7
- 原文：采用了 ARM Cortex-M7 微控制器
- 检索关键词：Intel "Programmable Services Engine" ARM Cortex-M7、Intel PSE Cortex-M7、Intel Elkhart Lake PSE architecture
- 检索结果：确认 Intel Elkhart Lake（Atom x6000E 系列）确实存在 PSE（Programmable Services Engine）模块，且为可选特性；但 "PSE 使用 ARM Cortex-M7" 这一具体架构描述未能通过 WebSearch 在 Intel 官方一手文档中直接证实（需直接查阅 EHL Datasheet PDF 原文）
- 核查结论：部分确认（PSE 模块存在确认；ARM Cortex-M7 架构未通过 WebSearch 直接证实）
- 当前处理：保留原文

### Connectivity Configuration（connectivity-configuration.md）

#### 存疑 12：BT Audio Offload 支持的无线网卡型号
- 原文：此功能仅支持特定 Intel® AX 系列无线网卡
- 检索关键词："Bluetooth Audio Offload" Intel AX210 AX211 AX200、Intel wireless "Audio Offload" supported models、Intel EVO "BT Audio Offload" AX201 AX210
- 检索结果：确认 "Bluetooth Audio Offload" 是 Intel EVO 平台认证规范的一部分（"Bluetooth 5 with Audio Offload"）；Intel ARK 官方页面未直接列出 "Audio Offload" 作为 AX201/AX210/AX211 等网卡的可检索字段；未找到明确列出支持型号的对照表
- 核查结论：部分确认（EVO 认证要求确认；具体支持的 AX 型号清单未能完全确认）
- 当前处理：保留原文 "此功能仅支持特定 Intel® AX 系列无线网卡"，未列出具体型号清单

## 已识别并尝试确定未知选项（2026-07-22）

事件描述：已识别并尝试确定全书标记为"功能不知/未知"的 BIOS 选项。

清单文件路径：`script/unknown-options-inventory-20260722.md`

### 总览

| 项目 | 数量 |
| ---- | ---- |
| 未知标记总数 | 51 |
| 已确定数 | 31 |
| 未确定数 | 20 |

### 已确定选项修正记录（31 条）

#### chipset/sa-configuration.md（23 条）

- 行 278 SenseAmp Offset Training：原文"其具体作用尚不明确。"→修正为"训练 DRAM 接收端感应放大器（Sense Amplifier）的偏移电压，补偿电路本身的偏移量，确保读取数据时能准确采样。" 核查来源：JEDEC JESD79-5 + WebSearch
- 行 292 Early ReadMPR Timing Centering 2D：原文"其具体作用尚不明确。"→修正为"早期阶段利用 MPR（多用途寄存器）进行二维时序中心化训练。" 核查来源：JEDEC JESD79-5
- 行 306 Read MPR Training：原文"其具体作用尚不明确。"→修正为"利用 MPR 已知数据模式进行读取训练，校准时序与电压。" 核查来源：JEDEC JESD79-5
- 行 318 Receive Enable Training：原文"其具体作用尚不明确。"→修正为"训练接收使能信号时序，确定 DQS 使能窗口。" 核查来源：JEDEC JESD79-5
- 行 332 Jedec Write Levelling：原文"其具体作用尚不明确。"→修正为"JEDEC 标准定义的写入均衡训练，通过调节写入数据选通信号（DQS）与 DRAM 时钟（CK）的相位关系，补偿 fly-by 拓扑结构下时钟到达各 DRAM 颗粒的时间偏差。" 核查来源：JEDEC JESD79-5
- 行 344 Early Write Time Centering 2D：原文"其具体作用尚不明确。"→修正为"早期二维写入时序中心化，调整至眼图中心。" 核查来源：JEDEC JESD79-5
- 行 356 Early Read Time Centering 2D：原文"其具体作用尚不明确。"→修正为"早期二维读取时序中心化，调整至眼图中心。" 核查来源：JEDEC JESD79-5
- 行 368 Write Timing Centering 1D：原文"其具体作用尚不明确。"→修正为"一维写入时序中心化，调整采样点至眼图中心。" 核查来源：JEDEC JESD79-5
- 行 380 Write Voltage Centering 1D：原文"其具体作用尚不明确。"→修正为"一维写入电压中心化，调整参考电压至眼图中心。" 核查来源：JEDEC JESD79-5
- 行 392 Read Timing Centering 1D：原文"其具体作用尚不明确。"→修正为"一维读取时序中心化，减少时序误差。" 核查来源：JEDEC JESD79-5
- 行 434 DIMM RON Training：原文"其具体作用尚不明确。"→修正为"训练 DIMM 输出驱动器导通电阻，匹配传输线减少反射。" 核查来源：JEDEC JESD79-5
- 行 446 Write Drive Strength/Equalization 2D：原文"其具体作用尚不明确。"→修正为"二维训练写入驱动强度与均衡参数。" 核查来源：JEDEC JESD79-5
- 行 470 Read ODT Training：原文"其具体作用尚不明确。"→修正为"训练读取侧片内终端电阻阻值，优化终端匹配。" 核查来源：JEDEC JESD79-5
- 行 482 Read Equalization Training：原文"其具体作用尚不明确。"→修正为"训练读取路径信号均衡器参数，补偿通道损耗。" 核查来源：JEDEC JESD79-5
- 行 506 Write Timing Centering 2D：原文"其具体作用尚不明确。"→修正为"二维写入时序中心化，沿时序和电压两维调整。" 核查来源：JEDEC JESD79-5
- 行 518 Read Timing Centering 2D：原文"其具体作用尚不明确。"→修正为"二维读取时序中心化，沿时序和电压两维调整。" 核查来源：JEDEC JESD79-5
- 行 590 Turn Around Timing Training：原文"其具体作用尚不明确。"→修正为"训练读写切换时序，优化切换间隔降低延迟。" 核查来源：JEDEC JESD79-5
- 行 602 CMD CTL CLK Slew Rate Training：原文"其具体作用尚不明确。"→修正为"训练命令/控制/时钟信号压摆率。" 核查来源：JEDEC JESD79-5
- 行 710 PanicVttDnLp Training：原文"其具体作用尚不明确。"→修正为"训练终端电压（VTT）下行调节的低功耗特性。" 核查来源：技术背景推断
- 行 912 Margin Check Limit：原文"其具体作用尚不明确。"→修正为"设定内存训练裕量检查阈值等级（L1/L2）。" 核查来源：上下文推断 + WebSearch
- 行 2433 DMI Gen4 EQ Mode：原文"其具体作用尚不明确。"→修正为"设置 DMI Gen4 链路均衡模式（Fixed EQ/HW EQ）。" 核查来源：PCIe 均衡标准
- 行 2503 DMI Gen3 TRC0 Cpre Lan0：原文"其具体作用尚不明确。"→修正为"设置发射端均衡前游标系数，补偿高频损耗。" 核查来源：PCIe 均衡标准
- 行 2923 Flash Support：原文"其具体作用尚不明确。"→修正为"摄像头模组闪光灯/补光灯支持开关。" 核查来源：上下文推断

#### chipset/pch-io-configuration.md（7 条）

- 行 2172 External Vnn Rail Voltage Configuration at S0 and S0ix：原文"其具体作用尚不明确。"→修正为"指定外部 Vnn 电压轨在 S0 和 S0ix 状态下使用的电压值，单位为 2.5mV（如默认值 420 表示 1.05V）。用于配置 PCH FIVR 的外部 Vnn 旁路电压轨的目标电压等级。" 核查来源：TigerLake FSP FspsUpd.h: PchFivrExtVnnRailVoltage
- 行 2294 Host Partition Reset ADR Enable：原文"该功能的具体作用尚不明确。"→修正为"控制是否在发生 Host 分区复位时触发 ADR（异步内存刷新）。Platform-PDR 为平台默认，Enabled 为强制启用，Disabled 为强制禁用。" 核查来源：TigerLake FSP: AdrHostPartitionReset
- 行 2315 ADR timer 2 time unit：原文"其具体作用尚不明确。"→修正为"指定 ADR 定时器 2 递增的滴答频率（时间单位），定时器 2 将按此频率递增。" 核查来源：TigerLake FSP: AdrMultiplier2Val
- 行 2479 PCH Cross Throttling：原文"只有 UTL 支持此功能。UTL 的含义尚不明确。"→修正为"只有 ULT 支持此功能。ULT 为 Intel 移动处理器代号（Ultra Low Power）。ULT 处理器支持在处理器封装和 LP PCH 之间进行热管理和交叉热节流。PCH 通过 PMSYNC 消息向 CPU 发送 PCH 热状态，处理器据此进行节流。" 核查来源：TigerLake FSP: PchCrossThrottling（修正 UTL→ULT 笔误）
- 行 2577 Pcie PLL SSC：原文"该功能的具体作用尚不明确。"→修正为"指定 PCIe PLL 扩频时钟（Spread Spectrum Clocking）的百分比，单位为 0.1%，有效范围为 0–20（即 0.0%–2.0%）。通过对 PCIe 参考时钟进行扩频调制以降低电磁干扰（EMI）。" 核查来源：TigerLake FSP: PciePllSsc
- 行 2715 Latch Events C10 Exit：原文"该功能的具体作用尚不明确。"→修正为"当此位设置为 1 时，SLP_S0# 进入事件在 SLP_S0_DEBUG_REGx 寄存器中于 C10 退出时捕获（而非默认的 C10 进入时捕获）。用于调试 S0ix 低功耗状态的电源管理事件。" 核查来源：TigerLake FSP: LatchEventsC10Exit
- 行 2729 Extend BIOS Range Decode：原文"其具体作用尚不明确。"→修正为"启用/禁用通过直接内存读取访问大于 16MB 的 BIOS 区域。当 BIOS 闪存容量超过 16MB 时，需要启用此项以扩展 SPI 闪存控制器的解码范围。" 核查来源：TigerLake FSP FspsUpd.h: PchSpiExtendedBiosDecodeRangeEnable

#### advanced/power-performance.md（1 条）

- 行 375 PSYS Pmax Power：原文"其具体作用在公开文档中未有明确说明。"→修正为"该选项用于设置 Psys 平台功耗信号的最大功率阈值（Pmax），供处理器 PL4 Boost 等平台功耗管理算法作为参考值。当启用 PL4 Boost 时，处理器将使用该 Pmax 值计算可达的更高性能频率。" 核查来源：en/arrow-lake-mobile/intel-core-ultra-200h-200u-datasheet-vol1.pdf 第 129 页 PL4 Boost 章节

### 未确定选项存疑记录（20 条）

#### chipset/sa-configuration.md（3 条）

- 行 2165 IUER Button Enable：原文"其具体作用尚不明确。" 检索关键词："IUER button Intel BIOS camera feature"。检索结果：无权威结果，属 Intel 专有摄像头按钮功能。当前处理：保留原文
- 行 2863 Control Logic 1：原文"该功能的具体作用尚不明确。" 检索关键词："Control Logic BIOS camera GPIO"。检索结果：无权威结果，属 Intel 专有摄像头 GPIO 控制逻辑。当前处理：保留原文
- 行 2921 CRD Version：原文"其具体作用尚不明确。" 检索关键词："CRD Version Kilshon CRD-G platform reference design"。检索结果：无权威结果，选项值为平台参考设计代号。当前处理：保留原文

#### chipset/pch-io-configuration.md（11 条）

- 行 792/796 Software Preserve：原文"Unknown（未知）/其具体作用尚不明确。" 检索关键词："Software Preserve SATA BIOS"。检索结果：无权威结果。当前处理：保留原文
- 行 864 Topology：原文"Unknown（未知）。" 检索关键词："SATA Topology ISATA Flex Direct connect M2 BIOS"。检索结果：无权威结果。当前处理：保留原文
- 行 1048 Enable HSII on xHCI：原文"其具体作用尚不明确。参见：TigerLake FSP Integration Guide"。检索关键词："HSII Interrupt IN Alarm xHCI USB"。检索结果：FSP PDF 仅确认 HSII = HS Interrupt IN Alarm，未解释具体功能。当前处理：保留原文
- 行 1806 PDT Unlock Message：原文"其具体作用尚不明确。" 检索关键词："ISH PDT Unlock Message"。检索结果：FSP PDF 仅说 0: False 1: True，PDT 含义不明确。当前处理：保留原文
- 行 2060 Alternate Fast Init Tdispatch：原文"其具体作用尚不明确。" 检索关键词："SATA Alternate Fast Init Tdispatch thermal throttling"。检索结果：无权威结果。当前处理：保留原文
- 行 2076 Tdispatch：原文"其具体作用尚不明确。" 检索关键词："SATA Tdispatch thermal throttling PCH timer"。检索结果：无权威结果。当前处理：保留原文
- 行 2090 Tinactive：原文"其具体作用尚不明确。" 检索关键词："SATA Tinactive thermal throttling PCH timer"。检索结果：无权威结果。当前处理：保留原文
- 行 2106 Skip VCC_AUX Configuration：原文"其具体作用尚不明确。" 检索关键词："Skip VCC_AUX Configuration FIVR PCH"。检索结果：无权威结果。当前处理：保留原文
- 行 2757 ACPI L6D PME Handling：原文"其具体作用尚不明确。" 检索关键词："ACPI _L6D GPE 0x6D PME Intel PCH"。检索结果：无权威结果。当前处理：保留原文
- 行 3217 PinCntrl Driver GPIO Scheme：原文"其具体作用尚不明确。" 检索关键词："PinCntrl Driver GPIO Scheme BIOS"。检索结果：无权威结果。当前处理：保留原文

#### advanced/connectivity-configuration.md（5 条）

- 行 87 BT RF-Kill Delay Time：原文"其具体作用尚不明确。" 检索关键词："BT RF-Kill Delay Time Intel CNVi WiFi Bluetooth GPIO"。检索结果：Intel 800 PCH 数据手册有 W_Disable2# 信号但无 BIOS 选项说明。当前处理：保留原文
- 行 127 Preboot BLE：原文"其具体作用尚不明确。" 检索关键词："Preboot BLE BIOS option Intel"。检索结果：无权威结果。当前处理：保留原文
- 行 185 Firmware Flash Device：原文"其具体作用尚不明确。" 检索关键词："Firmware Flash Device WWAN BIOS option"。检索结果：无权威结果。当前处理：保留原文
- 行 199 Wireless CNV Config Device：原文"其具体作用尚不明确。" 检索关键词："WCCD ACPI device Intel CNVi"。检索结果：ACPI 规范与 Intel 数据手册均未定义 WCCD。当前处理：保留原文
- 行 213 WWAN Reset Workaround：原文"其具体作用尚不明确。" 检索关键词："WWAN Reset Workaround BIOS"。检索结果：无权威结果。当前处理：保留原文

#### advanced/power-performance.md（1 条）

- 行 1006 Energy Performance Gain：原文"其具体作用尚不明确。" 检索关键词："Energy Performance Gain, EPG Gain, Idd3N, Idd3P, DDR-EPG"。检索结果：三份 Intel 数据手册与二十份 BIOS 手册均无此选项说明。当前处理：保留原文
