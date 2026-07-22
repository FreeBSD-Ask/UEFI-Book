# SDIO Configuration（SDIO 配置）

SDIO 参数配置说明。

SDIO（Secure Digital Input and Output），即安全数字输入输出接口。SDIO 协议是由 SD 卡协议演进而来，向下兼容 SD 卡协议。常用于嵌入式设备。

## SDIO Access Mode（SDIO 访问模式）

选项：

Auto（自动）

ADMA（高级 DMA 模式）

SDMA（单 DMA 模式）

PIO（可编程 IO 模式）

说明：

Auto（自动）：如果控制器支持 DMA，就以 DMA 模式访问 SD 设备；否则使用 PIO 模式。

SDMA：是 SD/eMMC 控制器中的一种基础的 DMA 模式。

ADMA：采用 ADMA（Advanced DMA）或 ADMA2 协议，支持描述符表、分散/聚集传输等特性，适合大块数据或复杂控制，性能更优。

PIO：通过 CPU 按指令逐字节处理 SD/eMMC 设备数据，CPU 参与度高，速度较慢，但兼容性强。

## Bus 0 Dev 1A Func 0

列出当前的 eMMC 设备。

### eMMC Y20128 (125.0 GB)

选项：

Auto（自动）

Floppy（软盘）

Forced FDD（强制将该设备模拟为软盘）

Hard Disk（硬盘）

说明：

大容量存储设备模拟类型。

用于将 eMMC 存储模拟为不同的设备。

Auto（自动）：小于 530 MB 的设备将被识别为软盘（Floppy）。

Forced FDD：可以将硬盘驱动器强制以软盘方式启动。
