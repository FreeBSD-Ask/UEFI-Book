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
