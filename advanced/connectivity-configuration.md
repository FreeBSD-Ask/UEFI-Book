# Connectivity Configuration（连接性配置）

本小节主要介绍英特尔无线网卡、蓝牙和 WWAN 模块（如 GPRS/3G/4G/5G 模块）的相关配置。

## CNVi CRF Present（显示是否存在 CNVi 模块）

本选项用于检测和显示系统中是否存在 CNVi 模块。

CNVi（Connectivity Integration，英特尔® 集成连接技术）是英特尔将 Wi-Fi 和 Bluetooth® 技术的关键元件转移到处理器上的解决方案。CRF（Companion RF，辅助射频模块）指无线网卡，现代无线网卡通常与蓝牙功能集成在同一模块中。

该解决方案由以下部分组成：

- CNVi：英特尔处理器的集成无线 IP 部分
- M.2 外形配套的 RF (CRF) 模块（2230 和 1216 焊接）。尽管这些无线网卡的物理规格为 M.2，但它们只能被特定的英特尔处理器所支持，AMD 处理器无法使用。

参见：英特尔公司. 什么是英特尔® 集成连接 (CNVi) 和配套 RF (CRF) 模块？[EB/OL]. (2022-10-21)[2026-03-26]. <https://www.intel.cn/content/www/cn/zh/support/articles/000026155/wireless.html>. 该文档解释了 CNVi 技术架构及其配套模块的工作原理。

## CNVi Configuration（CNVi 配置）

### CNVi Mode（CNVi 模式）

选项：

Auto Detection（自动检测）
Disable Integrated（禁用集成）

说明：

Auto Detection（自动检测）表示如果发现独立方案，将默认启用该方案，否则启用集成方案（CNVi）。
Disable Integrated（禁用集成）则会禁用集成方案。

注意：当 CNVi 存在时，用于比特率配置的 GPIO 引脚会被占用。

### MfUart1 type（带外通信的 UART 类型）

选项：

- ISH Uart0：ISH UART0（集成传感器中心的 UART0）
- SerialIO Uart2：SerialIO UART2（串行输入输出控制器的 UART2）
- Uart over external pads：通过外部引脚的 UART
- Not connected：未连接

说明：

这是一个测试选项，用于配置 Wi-Fi 辅助带外通信所使用的 UART 类型。

### Wi-Fi Core（无线核心）

选项：

Disable（禁用）
Enable（启用）

说明：

此选项用于启用或禁用 CNVi 中的 Wi-Fi 功能。

### BT Core（蓝牙核心）

选项：

Disable（禁用）
Enable（启用）

说明：

BT（Bluetooth，蓝牙）。此选项用于启用或禁用 CNVi 中的蓝牙功能。

### BT Audio Offload（蓝牙音频卸载/A2DP）

选项：

Disable（禁用）

Enable（启用）

说明：

BT Audio Offload（A2DP），英特尔蓝牙音频卸载技术，参见英特尔公司. 示范影片：以 Intel® Bluetooth® 音频卸除省电（A2DP）（MP4）[EB/OL]. (2022-10-27)[2026-03-26]. <https://www.intel.cn/content/www/cn/zh/content-details/751466/demo-video-power-saving-with-intel-bluetooth-audio-offload-a2dp-mp4.html>. 展示蓝牙音频卸载技术的省电效果。硬件卸载的音频处理允许在计算机的主 CPU 之外执行主要音频处理任务，即将蓝牙传输音频的解码放到 DSP 进行处理，可降低处理器的负载并省电。参见微软公司. Hardware-Offloaded 音频处理[EB/OL]. (2025-07-18)[2026-03-26]. <https://learn.microsoft.com/zh-cn/windows-hardware/drivers/audio/hardware-offloaded-audio-processing>. 介绍硬件卸载音频处理的技术原理与实现。

该功能可将来自蓝牙设备的 HFP 格式音频输入传送至音频 DSP，并通过 A2DP 格式以高能效方式将音频输出至蓝牙设备。

此功能仅支持特定 Intel® AX 系列无线网卡。

### BT RF-Kill Delay Time（蓝牙射频关闭延迟时间）

其具体作用尚不明确。

## RFI Mitigation（射频干扰缓解）

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 DDR 射频干扰抑制功能，用于控制内存模块的抗射频干扰功能。

该射频干扰缓解功能可能会导致 DDR 运行速度暂时降低。

## CoExistence Manager（共存管理）

选项：

Disable（禁用）

Enable（启用）

说明：

共存管理器可缓解英特尔 WWAN（无线广域网，如蜂窝网络 2G/3G/4G/5G）与英特尔 WLAN（Wi-Fi/蓝牙）之间的无线电共存问题。

## Preboot BLE（预启动蓝牙）

选项：

Disable（禁用）

Enable（启用）

说明：

此选项用于启用预启动蓝牙功能。

其具体作用尚不明确。

## Discrete Bluetooth Interface（独立蓝牙接口）

选项：

Disable（禁用）

USB

说明：

要选择蓝牙接口，必须启用 SerialIo UART0。

## BT Tile Mode（蓝牙 Tile 模式）

选项：

Disable（禁用）

Enable（启用）

说明：

Tile 是由 Tile 公司开发的一款小型蓝牙跟踪器，可用于查找丢失的物品。

启用后，可通过智能手机上的 Tile 应用定位计算机。

## Advanced settings（高级设置）

选项：

Disable（禁用）

Enable（启用）

说明：

配置无线设备的 ACPI 对象。

## WWAN Configuration（WWAN 配置）

## WWAN Device（WWAN 设备）

选择 M.2 WWAN 设备选项以启用 4G 7360/7560（英特尔）或 5G M80（联发科）调制解调器。

### Firmware Flash Device（固件闪存设备）

选项：

Disable（禁用）

Enable（启用）

说明：

控制 WWAN 固件闪存设备开关。启用后，WWAN 模块的固件存储区域将以闪存设备的形式暴露给操作系统，允许通过操作系统下的工具对 WWAN 模块进行固件更新。禁用则隐藏该设备，防止意外修改 WWAN 固件。

### Wireless CNV Config Device（无线 CNV 配置设备）

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 WCCD（Wireless CNV Config Device）ACPI 设备节点。WCCD 是 CNVi 无线模块在 ACPI 表中的配置设备节点，操作系统通过该节点识别和配置集成的 CNVi 无线模块（Wi-Fi/蓝牙）。禁用此项后，操作系统将无法通过 ACPI 枚举 CNVi 无线设备。

### WWAN Reset Workaround（WWAN 重置变通方案）

选项：

Disable（禁用）

Enable（启用）

说明：

启用此变通方案将使 BIOS 在执行 WWAN 设备加电序列之前，拉高 `FULL_CARD_POWER_OFF#`、`PERST#` 和 `RESET#` WWAN 信号，禁用此选项则不会对其施加任何影响。

该变通方案用于解决某些 WWAN 模块在上电后无法正常初始化的问题。通过在加电前先拉高复位信号，可确保 WWAN 模块从确定的复位状态开始启动，避免因上一次异常断电导致的初始化失败。仅在遇到 WWAN 模块无法被系统识别时启用。

### WA - WWAN OEM SVID（WWAN 模块所使用的 OEM 子厂商 ID）

显示 WWAN 模块所使用的 OEM 子厂商 ID。

### WA - WWAN SVID Detect Timeout（检测 WWAN OEM 子厂商信息的超时时间）

用于检测 WWAN OEM 子厂商 ID（SVID）的超时数值（以毫秒为单位）。请注意，这只是针对 OEM 的变通方案。
