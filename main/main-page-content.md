# 主页面内容

主页面内容区域展示了系统的核心硬件信息和基本配置选项，用户可在此区域查看 BIOS 版本、处理器信息、内存信息等关键参数。

## BIOS Information（BIOS 信息）

BIOS 信息子页面用于展示 BIOS 固件的详细属性，包括厂商、版本、兼容性等关键参数，帮助用户了解当前系统的固件版本和兼容性信息。

- BIOS Vendor（BIOS 厂商）: American Megatrends（安迈科技）
- Core Version（核心版本）: 5.27
- Compliancy（兼容性）: UEFI 2.8; PI 1.7
- Project Version（项目版本）: X4-V004
- Build Date and Time（构建日期和时间）: 03/05/2025 21:22:06（2025 年 03 月 05 日 21:22:06）
- M/B Name（主板名称）: RADXA X4
- Access Level（访问级别）: Administrator（管理员）

## Processor Information（处理器信息）

处理器信息子页面展示了中央处理器的详细规格，包括名称、类型、频率、步进等关键参数。这些信息由 BIOS 通过 CPUID 指令从处理器内部寄存器读取，用于系统识别和配置处理器相关功能。

- Name（名称）: AlderLake ULX - BIOS 报告的平台标识（Intel 官方代号为 Alder Lake-N）
- Type（类型）: Intel(R) N100 - 处理器型号
- Speed（频率）: 800 MHz - 当前运行频率（可能为节能状态下的低频）
- ID（编号）: 0xB06E0 - 处理器标识符
- Stepping（步进）: A0 - 处理器修订版本

步进（Stepping）是处理器制造过程中的版本标识，当制造工艺改进或功能修复时，会创建新的步进代码。Intel 处理器步进通常由“一位字母 + 一位数字”组成，字母越靠后、数字越大，通常表示步进版本越高，处理器相对较新。根据 [英特尔® 处理器 N100](https://www.intel.cn/content/www/cn/zh/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/ordering.html) 的官方资料，其当前步进为“N0”（一般消费者获得的均为该步进）。但该图 BIOS 显示该 N100 处理器的步进为“A0”，这通常表明其为工程样片。

参考文献：

- 英特尔公司. 英特尔® 处理器步进意味着什么？[EB/OL]. [2024-01-15]. <https://www.intel.cn/content/www/cn/zh/support/articles/000057218/processors.html>. 解释处理器步进版本的含义及其与硬件修订的关系。
- 联想. CPU“步进”介绍[EB/OL]. [2024-01-15]. <https://iknow.lenovo.com.cn/detail/320528>. 通俗介绍 CPU 步进概念及不同步进版本间的差异。
- 英特尔公司. 英特尔® 处理器 N100 规格与订购信息[EB/OL]. [2026-04-17]. <https://www.intel.cn/content/www/cn/zh/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html>. （确认步进 N0、4 核 4 线程、6 MB 缓存、800 MHz 基础频率）。

## Memory Information（内存信息）

内存信息子页面展示了系统内存的配置情况，包括版本、总容量、运行频率等参数。

- Memory RC Version（内存 RC 版本）: 0.0.4.73
- Total Memory（总内存）: 16384 MB
- Memory Frequency（内存频率）: 4800 MHz

## Language and Time（语言与时间）

语言与时间子页面用于配置系统的语言偏好、日期和时间设置。这些设置存储在 CMOS/NVRAM 中，由实时时钟（RTC）芯片维持。系统日期和时间是操作系统时间的基础，许多应用程序和系统服务依赖准确的时间信息。

- System Language（系统语言）: [English]（[英语]）- 控制 BIOS 界面显示语言
- System Date（系统日期）: [Sat 07/19/2025]（[2025 年 07 月 19 日 星期六]）- 系统当前日期
- System Time（系统时间）: [04:49:48] - 系统当前时间
