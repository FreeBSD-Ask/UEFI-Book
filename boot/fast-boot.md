# Fast Boot（快速启动）

本选项用于优化系统启动速度，但可能会影响部分硬件的初始化。启用该功能可以显著缩短开机时间，但需要注意可能带来的兼容性问题。

可用选项如下：

Enabled（启用）

Disabled（禁用）

具体说明：

用于启用或禁用在启动过程中仅初始化启动活动选项所需的最小设备集合。该设置对 BBS（BIOS 启动规范，BIOS Boot Specification）启动选项（非 UEFI（统一可扩展固件接口，Unified Extensible Firmware Interface）启动选项）无效。如果使用外置显卡，则其 VBIOS（视频 BIOS，Video BIOS）需要支持 UEFI GOP（图形输出协议，Graphics Output Protocol）。

警告：开启此选项后可能无法再次进入 BIOS，因为启用快速启动后，系统在启动阶段会忽略所有 USB 设备（如键盘）。通常可通过重置 CMOS（互补金属氧化物半导体，Complementary Metal-Oxide-Semiconductor），或使用 Windows 的高级启动功能进入 UEFI 固件设置。参见：华硕公司. Windows 11/10 如何进入 BIOS 设置界面[EB/OL]. [2026-03-26]. <https://www.asus.com.cn/support/faq/1008829/>。提供通过 Windows 高级启动功能进入 BIOS 设置的详细步骤。需要注意的是，此方法并非对所有主板均有效，部分主板仍无法通过该方式进入 BIOS。
