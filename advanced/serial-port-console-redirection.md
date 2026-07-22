# Serial Port Console Redirection（串口控制台重定向）

用于配置串口重定向相关选项。

## Console redirections（COMx 的控制台重定向）

选项：

Disable（禁用）

Enable（启用）

说明：

串口 x 控制台的重定向开关设置，将控制台信息重定向到指定的串口中。此选项决定了：

## Console Redirection Settings（COMx 的串口控制台重定向参数设置）

该设置指定主机和远程计算机（用户正在使用的计算机）之间如何交换数据。两台计算机应使用相同或兼容的设置。

### Console redirections EMS（COMx 的 Windows 紧急管理控制台重定向）

选项：

Disable（禁用）

Enable（启用）

说明：

EMS 控制台重定向开关。

紧急管理控制台是一种在 Windows 操作系统中将控制台输出重定向到串口的技术。

### Console Redirection Settings（COMx 的控制台重定向设置）

#### Terminal Type（终端类型）

选项：

VT100：ASCII 字符集

VT100+：扩展的 VT100，用于支持颜色显示、功能键等。

VT-UTF8：使用 UTF-8 编码映射 Unicode 字符到 1 个或多个字节。

ANSI：扩展 ASCII 字符集。

说明：

通过此选项可选择仿真类型，BIOS 仿真类型必须与终端程序中选择的模式相匹配。

#### Bits per second（每秒传输比特数/波特率）

选项：

9600

19200

38400

57600

115200

说明：

每秒传输比特数配置，传输速率必须和对端口串口匹配，超长或嘈杂的线路可能需要较低的速度。

#### Data bits（数据位）

选项：

7

8

说明：

串口数据位宽设置，每字节中实际数据所占的比特数配置。

#### Parity（奇偶校验）

选项：

None：无

Even（偶校验）：如果数据位中 1 的个数是偶数，则奇偶位为 0。

Odd（奇校验）：如果数据位中 1 的个数是奇数，则奇偶位为 0。

Mark（传号校验）：奇偶位始终为 1。

Space（空号校验）：奇偶位始终为 0。

#### Stop Bits（停止位）

选项：

1

2

说明：

停止位用于指示串行数据包的结束。（起始位则表示数据包的开始）标准设置为 1 个停止位。与较慢的设备通信时，可能需要超过 1 个停止位。

#### Flow Control（流控制）

选项：

None（无）

Hardware RTS/CTS：通过硬件请求发送协议/清除发送协议进行流量控制。开启该功能后，如果使用了不支持硬件流控的串口设备（如 USB 转串口线缆）或者未连接串口线缆，可能会导致无法加载板载和外接 PCIe 设备 OptionROM、屏幕黑屏光标闪烁等问题。

说明：

流控制设置，流控可以防止由于缓冲区溢出而导致的数据丢失。

在发送数据时，如果接收端的缓冲区已满，可以发送一个“停止”信号来暂停数据传输。一旦缓冲区有空位，再发送一个“开始”信号以重新启动数据传输。

硬件流控使用 RTS#（请求发送）和 CTS#（清除发送）线路来发送这些开始/停止信号。

#### VT-UTF8 Combo Key Support（VT-UTF8 组合键支持）

选项：

Disable（禁用）

Enable（启用）

说明：

启用对 ANSI/VT100（一种早期终端协议标准）终端的 VT-UTF8 组合键（比如 Ctrl + Alt + 某键）支持。

#### Recorder Mode（记录器模式）

选项：

Disable（禁用）

Enable（启用）

说明：

当启用此模式时，仅发送文本数据。该功能用于捕获终端数据。

#### Resolution 100x31（扩展终端分辨率到 100×31）

选项：

Disable（禁用）

Enable（启用）

说明：

将终端分辨率扩展到 100 列 × 31 行。

#### Putty Keypad（PuTTY 的功能键和键盘）

选项：

VT100：模拟 DEC VT100 终端，通常用于早期 UNIX 系统。

Intel Linux：模拟 Linux 虚拟终端（如命令行控制台）

XTERMR6：模拟 Xterm R6 终端

SCO：模拟 SCO UNIX 环境

ESCN：使用小键盘时总是发送前缀 `ESC`

VT400：模拟 DEC VT400 终端

说明：

PuTTY 的功能键和键盘设置。

PuTTY 是 Windows 上常用的终端模拟器。

### Console Redirection Settings (EMS)（Windows 紧急管理控制台重定向设置）

#### Out-of-Band Mgmt Port（带外管理端口）

选项：

COM0

COM1

说明：

该功能用于选择客户端服务器中的串口，以供 Microsoft Windows 紧急管理服务（EMS）用于与远程主机服务器通信。

#### Terminal Type EMS（Windows 紧急管理控制台终端类型）

同上，见 Terminal Type（终端类型）。

#### Bits per second（每秒传输比特数/波特率）

同上，见 Bits per second（每秒传输比特数/波特率）。

#### Flow Control（控制流）

选项：

None

Hardware RTS/CTS

Software Xon/Xoff（软 XON/XOFF）

说明：同上，见 Flow Control（控制流）。
