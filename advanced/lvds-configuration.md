# LVDS Configuration（LVDS 配置）

LVDS，Low-Voltage Differential Signal（低压差分信号）。

一般笔记本屏幕使用 LVDS 接口和主板相连。所以这部分主要用于设置内置的显示器面板。

## LVDS interface（LVDS 接口）

选项：

Enabled（启用）

Disabled（禁用）

此选项决定了以下选项：

### Edid Mode（EDID 模式）

选项：

External（扩展）

Default（默认）

Custom（自定义）

说明：

EDID（Extended Display Identification Data，扩展显示标识数据）包含显示器的分辨率、厂商名称和序列号等信息。

选择用于内部平板显示屏的 EDID。根据所选设置，以下部分选项或全部选项可能会出现或隐藏。

### EDID（扩展显示标识数据）

选项：

640x480 / 800x480 / 800x600 / 1024x600 / 1024x768 / 1280x720 / 1280x800 / 1280x1024 / 1366x768 / 1400x900 / 1600x900 / 1680x1050 / 1920x1080

说明：

仅当 Edid Mode（EDID 模式）选择 Default 才会出现本项。

设置内置显示器的 EDID 分辨率。

### Color Mode（色彩模式）

选项：

VESA 24bpp（美国标准，VESA 标准的 24 位色深格式）

JEIDA 24bpp（日本标准，JEIDA 标准的 24 位色深格式）

18 bpp（18 位色深格式）

说明：

选择 LVDS 接口的色深。对于 24 位色深，还可以选择 LVDS 通道的色彩映射方式，即选择是否兼容 VESA 标准或 JEIDA 标准。

### Interface（接口）

选项：

Single Channel（单通道）

Dual Channel（双通道）

说明：

配置 LVDS 接口为单通道或双通道模式。

### DE Polarity（数据使能极性）

选项：

Active High（高电平有效）

Active Low（低电平有效）

说明：

用于判断“使能状态”对应的是信号的高电平还是低电平。

### V-Sync Polarity（垂直同步极性）

选项：

Negative（负极性）

Positive（正极性）

说明：

定义显示器垂直同步信号的电平触发方式。

### H-Sync Polarity（水平同步极性）

选项：

Negative（负极性）

Positive（正极性）

说明：

定义显示器水平同步信号的电平触发方式。

### LVDS Advanced Options（LVDS 高级选项）

#### Spreading Depth（扩频深度）

选项：

No Spreading（无扩频）

0.5%

1.0%

1.5%

2.0%

2.5%

说明：

设置 LVDS 时钟频率用于扩频的带宽百分比。用于减小电磁干扰。

#### Output Swing（输出摆幅）

选项：

150 mV / 200 mV / 250 mV / 300 mV / 350 mV / 400 mV / 450 mV

说明：

设置 LVDS（低压差分信号）接口的差分输出摆幅。

输出摆幅分为正向和负向摆幅，也就是 VP+、VP-。输出摆幅指的是信号从最低电压到最高电压之间的电压差，也就是输出信号的电压幅度范围。

用于改善传输质量与信号完整性，调节得当可提升图像或数据传输稳定性。

#### T3 Timing（T3 延迟）

参见：yuanqiangfei. LVDS 接口液晶屏点屏流程详解[EB/OL]. (2024-01-15)[2024-01-15]. <https://www.cnblogs.com/yuanqiangfei/p/11654412.html>. 下同。

选项范围：

0-255（以 50 毫秒为单位表示）

说明：

面板电源序列中最小 T3 时序限制。默认值为 10（即 500 毫秒）。

用于控制 LVDS 信号输出到背光开启之间的时间延迟。

#### T4 Timing（T4 延迟）

选项范围：

0-255（以 50 毫秒为单位表示）

说明：

T4 表示从停止发送 LVDS 数据到关闭背光之间的最小延迟时间。

面板电源序列中最小 T4 时序限制。默认值为 2（即 100 毫秒）。

#### T12 Timing（T12 延迟）

选项范围：

0-255（以 50 毫秒为单位表示）

说明：

从关闭面板电源（VDD）之后，到下一次重新开启电源（VDD）之前，必须等待的最小时间间隔。

面板电源序列中最小 T12 时序限制。默认值为 20（即 1 秒）。

#### T2 Delay（T2 延迟）

选项：

Enabled（启用）

Disabled（禁用）

说明：

LVDS T2 延迟（LVDS T2 Delay）是指从 T-CON（Timing Controller）芯片上电到 LVDS 数据输出之间的最小延迟时间。此设置用于确保 T-CON 芯片完成初始化并稳定输出数据，以避免显示异常，如花屏或闪烁。

启用后，T2 延迟增加 20 毫秒，误差范围为正负 50%。

#### T5 Delay（T5 延迟）

选项：

Enabled（启用）

Disabled（禁用）

说明：

从关闭背光电源到停止输出 LVDS 数据之间的延迟时间。

启用后，T5 延迟增加 20 毫秒，误差范围为正负 50%。

#### P/N Pairs Swapping（P/N 对交换）

选项：

Enabled（启用）

Disabled（禁用）

说明：

启用或禁用 LVDS 差分对的交换（正极 ↔ 负极）。

控制交换 LVDS 信号对的 P 和 N 引脚与否。

用于调整 LVDS 信号极性匹配。

#### Pairs Order Swapping（差分对顺序交换）

选项：

Enabled（启用）

Disabled（禁用）

说明：

控制指定的信号线对顺序。LVDS 通道差分对的顺序交换（例如 A 与 D 互换，B 与 CLK 互换，C 与 C 互换）。

#### Bus Swapping（总线交换）

选项：

Enabled（启用）

Disabled（禁用）

说明：

将 LVDS 信号线路中的奇数通道和偶数通道进行互换。总线交换（奇数总线与偶数总线互换）。

#### Firmware PLL（固件级锁相环）

选项：

0: +/- 1.56%

1: +/- 3.12%

2: +/- 6.25%

3: +/- 12.5%

4: +/- 25%

5: +/- 50%

6: +/- 100%

说明：

配置 LVDS 接口的时钟源和频率范围。

LVDS（低压差分信号）接口的时钟信号通常由锁相环（PLL，Phase-Locked Loop）生成。

Firmware PLL 指通过固件（BIOS）对 PLL 参数进行调节，以优化时钟频率和信号稳定性。
