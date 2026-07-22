# Intel® Time Coordinated Computing（TCC，英特尔® 时间协调计算）

Intel® 时间协调计算（Intel® TCC）可为实时应用提供优化的计算和时间性能。支持基于无线和有线融合网络的 IEEE\* 802.1 时间敏感网络（TSN）。

参见：英特尔公司. 英特尔®时序协调计算（TCC）用户指南[EB/OL]. [2026-03-26]. <https://www.intel.com/content/www/us/en/docs/tcc-tools/tutorial-vtune-profiler/2022-2/step-7-configure-intel-tcc-tools-in-bios.html>.

## Intel® TCC Mode（Intel TCC 模式）

选项：

Disable（禁用）

Enable（启用）

说明：

控制 Intel® TCC 模式。启用后，系统将修改相关设置以提升实时性能。启用 Intel® TCC 模式时，下方将显示完整的设置列表及其当前状态。

## Software SRAM（软 SRAM）

选项：

Disable（禁用）

Enable（启用）

说明：

SRAM 即静态随机存取存储器（Static Random Access Memory）。

软件 SRAM 能够为实时应用分配低延迟的内存缓冲区。软件 SRAM 是一种利用硬件能力的软件构造，通过将物理地址空间的一部分分配到缓存中，使这些地址不太可能被自身或其他进程驱逐。

启用后将分配 1 路 LLC（最后一级缓存）；如果可用缓存配置子区域（Cache Configuration subregion）存在，则将根据该子区域进行分配。

## Data Streams Optimizer（数据流优化器）

选项：

Disable（禁用）

Enable（启用）

说明：

控制由数据流优化器工具所选的调优配置。该工具通过多种调优配置，指导 BIOS 将特定值写入寄存器，从而提升处理器子系统之间的数据传输效率。

启用后将使用 DSO 子区域对系统进行调优。DSO 设置将覆盖与 Intel® TCC 模式存在重叠的设置。

## TCC Error Log（TCC 错误日志）

选项：

Disable（禁用）

Enable（启用）

说明：

Intel® TCC 错误日志功能可查看 BIOS 启动过程中发生的错误。启用后将把 TCC 流程中的错误转储到内存。

## Intel® TCC Authentication Menu（Intel TCC 认证菜单）

### IO Fabric Low Latency（IO Fabric 低延迟模式）

选项：

Disable（禁用）

Enable（启用）

说明：

IO Fabric 指 I/O 架构。

启用此选项将关闭部分 PCH IO 架构中的电源管理功能。该选项提供了最激进的 IO Fabric 性能设置，但不支持 S3 睡眠状态。适用于高性能/实时计算。

### GT CLOS（图形技术服务类别）

选项：

Disable（禁用）

Enable（启用）

说明：

Graphics Technology (GT) Class of Service，图形技术服务类别。

控制图形技术（GT）服务类别。启用后将减少图形的 LLC 分配，以最小化图形工作负载对 LLC（最后一级缓存）的影响。可提高实时性能和系统响应速度。

#### RAPL PL1 Enable（启用运行平均功率限制 1）

长期功率限制，平均功耗

#### RAPL PL2 Enable（启用运行平均功率限制 2）

短期功率限制，峰值功耗
