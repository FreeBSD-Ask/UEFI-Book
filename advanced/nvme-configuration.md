# NVMe configuration（NVMe 配置）

![NVMe 配置](../.gitbook/assets/image-20250721171013-mb7e4x3.png)

![NVMe 配置](../.gitbook/assets/image-20250721171025-jyfdidk.png)

## Self Test Option（自我测试选项）

选项：

Short（短自检）

Extended（扩展自检）

说明：

此选项和 Run Device Self Test（运行设备自我测试）有关。

请选择执行短自检（Short Self Test）或扩展自检（Extended Self Test）。

短自检大约需要几分钟完成，而扩展自检则需要更长时间。

## Self Test Action（自我测试行为）

选项：

Controller Only Test（仅控制器测试）

Controller and NameSpace test（控制器和命名空间测试）

说明：

此选项和 Run Device Self Test（运行设备自我测试）有关。

控制器和命名空间测试要更长时间才能完成。

## Run Device Self Test（运行设备自我测试）

此选项依赖 Self Test Option（自我测试选项）和 Self Test Action（自我测试行为）。

执行用户选择的“选项”和“操作”对应的设备自检程序。按下 Esc 键可中止测试。下面显示的结果为设备中最近一次自检的记录。

### Short Device Selftest Result（短自检）

Not Available：不可用，即未测试过。

### Extended Device Selftest Result（扩展自检）

Not Available：不可用，即未测试过。

## VMD Setup（VMD 卷管理设备设置）

VMD（Volume Management Device，卷管理设备）是 Intel 平台引入的硬件技术，提供对 NVMe SSD 的统一管理，并支持从 NVMe RAID 卷启动。该子菜单允许配置 VMD 控制器。

### Enable VMD Controller（启用 VMD 控制器）

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 VMD 控制器。创建 RAID 配置时，需将此项设置为 Enabled。

### Enable VMD Global Mapping（启用 VMD 全局映射）

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 VMD 全局映射。创建 RAID 配置时，需将此项设置为 Disabled，然后将对应的 SATA/M.2 接口下“Map this Root Port under VMD”项设置为 Enabled。

### Map this Root Port under VMD（在 VMD 下映射此根端口）

选项：

Disable（禁用）

Enable（启用）

说明：

根据所使用的 SATA/M.2 接口，将对应根端口映射到 VMD 下。此项仅在 Enable VMD Controller 设置为 Enabled 且 Enable VMD Global Mapping 设置为 Disabled 时可配置。

### Map PCH SATA Controller Under VMD（将 PCH SATA 控制器映射到 VMD 下）

选项：

Disable（禁用）

Enable（启用）

说明：

启用后将整个 PCH SATA 控制器映射到 VMD（Volume Management Device，卷管理设备）下统一管理，而不必逐个端口启用 Map this Root Port under VMD。该选项便于将 PCH SATA 与 CPU 直连 NVMe 一并纳入 VMD/RAID 体系。

## RAID Level Enable（RAID 级别启用）

VMD 模式下可按级别分别启用 RAID 支持。各 RAID 级别单独开关，便于按需启用，而不必一次性开启整个 Intel Rapid Storage Technology（Intel RST）驱动栈。

### RAID0

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 RAID0（Stripe，条带）级别支持。RAID0 通过条带化将数据分布在多个磁盘上以提升读写性能，但不提供冗余。

### RAID1

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 RAID1（Mirror，镜像）级别支持。RAID1 通过镜像将数据同时写入两个磁盘以提供数据冗余。

### RAID5

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 RAID5（Parity，奇偶校验）级别支持。RAID5 通过分布式奇偶校验在多个磁盘上提供数据冗余与读写性能的平衡，至少需要 3 块磁盘。

### RAID10

选项：

Disable（禁用）

Enable（启用）

说明：

启用或禁用 RAID10（Mirror+Stripe，镜像+条带）级别支持。RAID10 为 RAID1 与 RAID0 的组合，至少需要 4 块磁盘，兼顾性能与冗余。

## ZPODD（Zero Power ODD，零功耗光驱）

选项：

Disable（禁用）

Enable（启用）

说明：

ZPODD（Zero Power Optical Disc Drive，零功耗光驱）是 SATA 协议定义的电源管理特性，允许在光驱空闲时切断其供电，使光驱在 S0 工作状态下的功耗降至接近零。该项仅在 VMD 模式下连接 ZPODD 兼容光驱时启用。
