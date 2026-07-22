# Embedded Controller（嵌入式控制器）

## Embedded Controller information（嵌入式控制器信息）

显示嵌入式控制器相关信息。

## Power Fail Resume Type（断电恢复类型）

选项：

Always ON

Always OFF

Last State

说明：

指定在电源故障（G3 状态，完全断电）后重新加电时系统应进入的状态。

如果是无电池运行模式（Batteryless Operation），芯片组在电源故障后总是自动开机（即 Always ON）：因此，若选择“Always OFF”恢复类型，或选择“Last State”且上一次状态为关机，系统将自动开机后立即关闭。

## No CMOS Battery Handling（无 CMOS 电池处理逻辑）

选项：

Enabled（启用）

Disabled（禁用）

说明：

在没有 CMOS 电池的系统中（例如服务器或嵌入式设备），芯片组通常会在断电后自动上电：

因此，如果将恢复类型设置为“Always OFF”，或者设置为“Last State”且上一次状态为关机，那么系统将自动开机后立即关闭。

## LID_BTN# Configuration（LID_BTN# 信号配置）

选项：

Force Open（强制开启）

Force Closed（强制关闭）

Normal Polarity（正常极性）

Inverted Polarity（反转极性）

说明：

LID_BTN# 是笔记本等设备上的“盖子开关”信号（LID Button），通常用于感知盖子是否关闭。

配置 LID_BTN# 信号为始终开启或关闭（无论引脚电平如何），或者配置引脚的极性：高电平 = 打开（正常），低电平 = 打开（反转）。

## LID_BTN# Wake Configuration（LID_BTN# 唤醒配置）

选项：

No Wake（不唤醒）

Only From S3（仅从 S3 唤醒）

Wake From S3/S4/S5（从 S3/S4/S5 唤醒）

说明：

控制屏盖打开时是否自动唤醒系统。

配置 LID_BTN# 信号的唤醒功能（当前未强制设置为“开启”或“关闭”时）。根据引脚配置，当屏幕盖处于开启状态时，它可以使系统从睡眠状态唤醒。

## OUT 80 serial redirection port（BIOS OUT 80 串口重定向端口）

选项：

None（无）

1

2

1+2

说明：

在 BIOS 中，`OUT 80h` 通常指的是将数据写入 I/O 端口 0x80，这是一个用于调试的标准端口。通过向该端口写入特定的值，系统可以在启动过程中输出调试信息，帮助开发人员定位问题。

用于调试。选择将 OUT 80（POST 代码）重定向到指定的 EC UART（串口）。

## Hardware Monitor（硬件监控）

显示监控的硬件参数和设置。

## Reset Causes Handling（重置原因处理）

用于指定系统在重启时如何响应不同的重置原因。该功能主要用于嵌入式系统或服务器中，以便在系统重启时进行适当的诊断或日志记录。

### Reset Button Pressed（重置按钮被按下）

选项：

Happened（发生）：按下了重置按钮

Not Happened（未发生）：重置按钮没被按下

说明：

系统是否检测到机箱上的硬件重置按钮被按下。

### Clear from log（日志清除）

选项：

Enabled（启用）

Disabled（禁用）

说明：

清除 BIOS 中的系统事件日志。

重启后生效。

### WDT Timeout Expired（看门狗定时器超时触发）

选项：

Happened（发生）：看门狗定时器超时了

Not Happened（未发生）：看门狗定时器未超时

### Power Failure（电源故障）

选项：

Happened（发生）：电源故障了

Not Happened（未发生）：电源未故障

### EC Soft Reset（嵌入式控制器软重置）

说明：

Happened（发生）：嵌入式控制器软重置过

Not Happened（未发生）：嵌入式控制器未执行过软重置

## Super IO Configuration（超级 I/O 配置）

参见：CSDN 博主 u011397314. BIOS 实战之 Super IO-Smart Fan[EB/OL]. (2024-01-15)[2024-01-15]. <https://blog.csdn.net/u011397314/article/details/111147528>。

用于管理主板上的传统 I/O 接口，如串口（COM）、并口（LPT）、PS/2 键盘/鼠标、红外接口（IR）以及环境控制器（EC）等。这些接口通常由 Super I/O 芯片控制，负责处理低速 I/O 设备的通信。

### Serial Port x（串口 x）

#### Address（地址）

选项：

0x3F8 / 0x3E8 / 0x2F8 / 0x2F0 / 0x2E8 / 0x2E0 / 0x2A8 / 0x2A0 / 0x288 / 0x280

说明：

串口 I/O 基线地址，用于指定串口通信的 I/O 地址。

#### IRQ（来自设备的中断请求）

选项：

3 / 4 / 5 / 6 / 7 / 10 / 11 / 14 / 15

说明：

串口 I/O IRQ（Interrupt Request，来自设备的中断请求），定义串口通信中断请求的硬件资源。

参见：Linux 内核开发社区. 什么是 IRQ？[EB/OL]. [2026-03-26]. <https://www.kernel.org/doc/html/v6.9/translations/zh_CN/core-api/irq/concepts.html>。

## External FAN/PWM Settings（外部风扇/PWM 设置）

当 SMARC（Smart Mobility ARChitecture，智能移动架构）相关配置中的 PWM/风扇管理启用时可见。

参见：什么值得买值友 9415279329. PWM 信号占空比，如何影响散热风扇速度？[EB/OL]. [2026-03-26]. <https://post.smzdm.com/p/a5p056o3/>。

### FAN_PWMOUT device type(FAN_PWMOUT 设备类型)

选项：

3-WIRE FAN（3 线风扇）

4-WIRE FAN（4 线风扇）

Generic PWM（通用 PWM）

说明：

风扇 PWM（脉宽调制）输出接口类型，用于指定风扇类型。

### Automatic Temperature FAN Control（风扇自动温度控制）

选项：

Enabled（启用）

Disabled（禁用）

说明：

热反馈风扇控制是一种基于温度传感器反馈来动态调节风扇转速的控制机制。

### FAN PWM Frequency（风扇 PWM 频率）

选项范围：

1-60000

说明：

设置 FAN_PWMOUT 信号的频率。典型值为 100（用于三线风扇）/ 20000（用于四线风扇）。

### FAN Duty Cycle (%)（风扇占空比）

选项范围：

1-100

说明：

脉冲信号（PWM）高电平的时间占整个周期的比例，来控制风扇的转速。

设置 FAN_PWMOUT 信号的占空比。当占空比增加时，风扇接收到的有效电流增加，转速也随之提升；反之，占空比减少时，风扇转速会降低。简言之，占空比越大，风扇转速越高。

## Watchdog Configuration（看门狗配置）

选项：

Enabled（启用）

Disabled（禁用）

说明：

看门狗定时器机制配置。

## GPIO Configurations（GPIO 配置）

GPIO，General Purpose Input/Output（通用输入输出），通常用于嵌入式设备。

### GPIOx (GPIO x)

#### Configuration（配置）

选项：

Input（输入模式）

Output Low（输出低电平）：输出固定的物理低电平（通常是 0 V）。

Output High（输出高电平）：输出固定的物理高电平（通常是 Vcc）。

Output Last（保持上次输出状态）：与上次启动时的状态保持一致，不做更改。

说明：

将引脚配置为输入或带固定初始值的输出。

## MAC address(es) visualization（MAC 地址显示）

显示系统的 MAC 地址。

## SMARC Related Configuration（SMARC 相关配置）

用于将 GPIO 分配给不同的功能。

### HD Audio Reset（HDA 重置）

选项：

Enabled（启用）

Disabled（禁用）

说明：

当该引脚配置为音频模式时，音频控制器和 Codec 会正常工作；但如果将其配置为通用 GPIO 用途，则音频功能将无法启用。

启用此选项后，GPIO4 将被用作高清音频复位信号。GPIO4 → HDA_RST#（高清音频复位引脚）。

### PWM/FAN Management（PWM/风扇管理）

选项：

Enabled（启用）

Disabled（禁用）

说明：

启用此选项后，GPIO5 将被用作 PWM / 风扇输出信号。GPIO5 → PWM_OUT（脉宽调制输出）。

### Tachometer（转速计）

选项：

Enabled（启用）

Disabled（禁用）

说明：

启用此选项后，GPIO6 将被用作转速计输入。GPIO6 → TACHIN。

## USB Port Enabling（USB 端口使能）

选项：

Enabled（启用）

Disabled（禁用）

说明：

禁用/启用载板上每个 USB 端口的 VBUS 电源（USB 供电线 +5 V）
