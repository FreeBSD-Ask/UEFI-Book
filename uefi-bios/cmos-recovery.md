# 设置 BIOS 后无法开机的处理方法（CMOS 简介）

本节介绍 CMOS 的基本概念以及在 BIOS 设置错误后如何恢复系统。

CMOS（Complementary Metal-Oxide-Semiconductor，互补金属氧化物半导体）原指一种由电池供电的芯片，用于存储 BIOS 配置信息（如时间信息、BIOS 密码和硬件设置等）。该芯片采用 CMOS 工艺制造，功耗极低，可由纽扣电池维持数据数月甚至数年。在现代 UEFI 系统中，系统的相关配置信息通常存储在非易失性 RAM（NVRAM）中，但出于习惯，人们仍将这种存储 BIOS/UEFI 设置的非易失性存储称为 CMOS。

清空 CMOS 可清除所有 BIOS 配置参数，恢复出厂默认设置。当 BIOS 设置错误导致系统无法启动时，可通过短接主板上的 CMOS 清除跳线、移除纽扣电池或使用专用按钮来清空 CMOS。具体操作方法因主板型号而异，可参考主板说明书或访问华硕官网（华硕. 主板如何 Clear CMOS[EB/OL]. [2026-03-26]. <https://www.asus.com.cn/support/faq/1040820/>）获取详细指导。

BIOS 是执行硬件初始化的固件程序，而 CMOS 是存储 BIOS 配置参数的硬件芯片。两者功能不同但紧密相关：BIOS 在启动时读取 CMOS 中的配置信息来初始化硬件。更多区别可参考联想官网（联想. BIOS 和 CMOS 有什么不同？[EB/OL]. [2026-03-26]. <https://iknow.lenovo.com.cn/detail/043962?type=undefined&keyword=BIOS&keyWordId=>）。
