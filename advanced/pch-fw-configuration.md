# PCH-FW Configuration（平台控制器中枢和固件配置）

PCH：Platform Controller Hub，平台控制器中枢（通常称为南桥），用于芯片组与固件相关配置。

## ME State（Intel 管理引擎状态）

选项：

Disable（禁用）

Enable（启用）

说明：

开启或关闭 Intel 管理引擎。

ME：Intel Management Engine，Intel 管理引擎状态。英特尔® 管理引擎是一个嵌入式微控制器（集成在某些英特尔芯片组上），运行一个轻量级微内核操作系统，为基于英特尔® 处理器的计算机系统提供各种功能和服务。

参见：英特尔公司. 什么是英特尔®管理引擎？[EB/OL]. [2026-03-26]. <https://www.intel.cn/content/www/cn/zh/support/articles/000008927/software/chipset-software.html>.

## ME Unconfig on RTC Clear（重置 RTC 时是否重置 ME）

选项：

Disable（禁用）

Enable（启用）

说明：

当设置为 Disabled 时，在执行 RTC Clear（清除实时时钟 RTC 的 CMOS 存储）操作后，不会重置或清除 ME 配置。

当设置为 Enable 时，在执行 RTC Clear（清除实时时钟 RTC 的 CMOS 存储）操作后，会重置或清除 ME 配置。

## Comms Hub Support（Comms 总线支持）

选项：

Disable（禁用）

Enable（启用）

说明：

部分嵌入式设备需要此总线，常见于工业物联网。按需开启。

## JHI Support（JHI 支持）

选项：

Disable（禁用）

Enable（启用）

说明：

需要操作系统支持。工业物联网可能会用到此选项，按需开启。

JHI：Intel® DAL（Dynamic Application Loader）Host Interface Service，Intel 动态应用加载器主机接口服务

英特尔® 动态应用加载器（Intel® DAL）是英特尔® 平台的一项独特功能，适用于多种形态的设备，包括工作站、台式机、笔记本、平板电脑和物联网设备。它可用于在英特尔® 融合安全与管理引擎固件上运行小段 Java* 代码。

参见：英特尔公司. Intel® Dynamic Application Loader[EB/OL]. [2026-03-26]. <https://www.intel.com/content/www/us/en/developer/tools/dal/overview.html>.

## Core Bios Done Message（核心 BIOS 初始化完成信息）

选项：

Disable（禁用）

Enable（启用）

说明：

BIOS 在完成核心 DXE 阶段后向 ME / BMC 发出的信号，意味着系统已完成对 Option ROM 的初始化。

是否将核心 BIOS 初始化完成信息发送给 Intel 管理引擎。作用：触发安全策略（如 KCS Trust）、同步双方状态，保障后续启动与管理流程顺利进行。

参见：Intel-BMC. host-misc-comm-manager[EB/OL]. [2026-03-26]. <https://github.com/Intel-BMC/host-misc-comm-manager>.

## Firmware Update Configuration（固件更新配置）

配置 Intel 管理引擎技术参数。

### ME FW Image Re-Flash（Intel 管理引擎映像重新刷写）

选项：

Disable（禁用）

Enable（启用）

控制是否允许重新刷写 Intel 管理引擎的固件的开关。

### FW Update（固件更新）

选项：

Disable（禁用）

Enable（启用）

说明：

控制是否允许更新 Intel 管理引擎的固件。

## PTT Configuration（Intel 可信平台技术配置）

PTT：Platform Trust Technology，Intel 可信平台技术。如果要安装 Windows 11，需要开启此功能。

英特尔® PTT 是符合 2.0 规范并提供与独立 TPM 相同的功能的集成 TPM，只是它驻留在系统的固件中，因此无需专用处理或内存资源。

参见：英特尔公司. 什么是可信平台模块（TPM）及其与英特尔®Platform Trust Technology（英特尔®PTT）的关系？[EB/OL]. [2026-03-26]. <https://www.intel.cn/content/www/cn/zh/support/articles/000094205/processors/intel-core-processors.html>.

### TPM Device Selection（TPM 设备选择）

选项：

dTPM

PTT

PTT 在 SkuMgr 中启用 PTT。

dTPM 1.2 在 SkuMgr 中禁用 PTT。

警告！如果要禁用 PTT/dTPM，那么存储在其中的所有数据都将丢失（如 BitLocker 恢复密钥）。

SkuMgr 是 BIOS 中的一个模块，用于管理系统的硬件配置和功能启用。

TPM 或受信任的平台模块是一种驻留在计算机主板或其处理器中的物理或嵌入式安全技术（微控制器）。TPM 使用加密技术来帮助在电脑上安全地存储基本和关键信息，以启用平台身份验证。

## FIPS Configuration（联邦信息处理标准配置）

FIPS 140-2（Federal Information Processing Standard 140-2），联邦信息处理标准 (FIPS) 出版物 140-2 是美国政府标准，它定义了信息技术产品中加密模块的最低安全要求。该标准已被 FIPS 140-3（2019 年发布）取代，2026 年 9 月起 FIPS 140-2 认证将正式过渡为历史状态。

联邦信息处理标准（FIPS）指定了联邦政府对加密模块的要求。

### FIPS Mode Select（联邦信息处理标准模式选择）

选项：

Disable（禁用）

Enable（启用）

说明：

在启用 FIPS 模式后，系统将强制使用符合 FIPS 认证的加密算法和操作，确保数据处理的安全性和合规性。

## ME Debug Configuration（Intel 管理引擎调试配置）

### HECI Timeout（HECI 超时）

选项：

Disable（禁用）

Enable（启用）

说明：

HECI，Host Embedded Controller Interface，主机嵌入式控制器接口。它是 Intel 管理引擎与主机操作系统之间的通信接口。

控制 HECI 发送/接收超时。

启用此功能后，如果主机操作系统在规定时间内未能与管理引擎建立通信，系统可能会中止该过程并报告超时错误。

### Force ME DID Init Status（强制初始化 Intel 管理引擎（ME）的设备标识符）

选项：

Disable（禁用）

Enable（启用）

说明：

启用此选项后，系统会在启动时强制初始化 Intel 管理引擎的设备标识符。

### CPU Replaces Polling Disable（禁用 CPU 更换轮询）

选项：

Disable（禁用，禁止 CPU 替代轮询，由其他机制处理轮询任务）

Enable（启用，允许 CPU 进行替代式轮询操作）

说明：

启用此选项将禁用 CPU 更换轮询循环。此设置多见于嵌入式 / IoT 或服务器硬件。

### ME DID Message（Intel 管理引擎的设备标识符信息）

选项：

Disable（禁用）

Enable（启用）

说明：

控制 Intel 管理引擎的设备标识符消息（禁用将阻止发送设备标识符消息）。Intel 管理引擎需要开启此选项。

### HECI Message check Disable（禁用 HECI 信息检查）

选项：

Disable（禁用）

Enable（启用）

说明：

HECI 是 Intel 管理引擎与主机之间的通信接口。

BIOS 在自检后等待 Intel 管理引擎应答的总线校验机制。

设置此选项可在发送 BIOS 启动路径消息时禁用消息校验。

### MBP HOB Skip（跳过 MBP HOB）

选项：

Disable（禁用）

Enable（启用）

说明：

MBP：Memory Based Protection Hand-Off Blocks，基于内存的保护交接块

启用后，BIOS 在启动过程中会跳过 Intel 管理引擎的 Memory‑Based Protection（MBP）的 HOB 区域（主要用于描述内存保护区域的信息），即不创建或不处理该区域内的 HOB（Hand‑Off Blocks）。

用于调试 Intel 管理引擎。

### HECI2 Interface Communication（HECI2 接口通信）

选项：

Disable（禁用）

Enable（启用）

说明：

添加和移除 PCI 空间中的 HECI2 设备。

HECI2（Host Embedded Controller Interface 2，主机嵌入式控制器接口 2）是 Intel 管理引擎与操作系统之间的通信接口。Intel 管理引擎的部分功能需要启用此选项。

### KT Device（KT 设备）

用于控制 KT 设备。

Disable（禁用）

Enable（启用）

说明：

KT 设备即 Intel 管理引擎的硬件接口设备，操作系统通过该设备与 Intel 管理引擎进行通信。

### D0i3 Setting for HECI Disable（D0i3 设置：用于禁用 HECI）

选项：

Disable（禁用）

Enable（启用）

说明：

以软件方式禁用 Intel 管理引擎。

软禁用的工作原理是让系统固件通过主机嵌入式控制器接口（HECI）发送“SET_ME_DISABLE”命令。这会命令管理引擎进入禁用状态。管理引擎将保持禁用状态，直到发送“ENABLE”命令。此方法被视为一种通用方法，因为它不需要实现特定于平台或处理器的代码。

参见：Protectli. Disabling the Intel Management Engine (ME)[EB/OL]. [2026-03-26]. <https://kb.protectli.com/kb/me-disable/>.

### MCTP Broadcast Cycle（MCTP 周期性广播）

选项：

Disable（禁用）

Enable（启用）

说明：

用于设置管理组件传输协议的广播周期，并将 PMT 设置为总线所有者。用于配置管理组件传输协议（MCTP）的周期性广播。

MCTP（Management Component Transport Protocol，管理组件传输协议）是一种独立于物理介质的协议，用于计算机系统中各部件之间的信息交互。此协议独立于底层物理总线，是一种独立于总线的“数据链路层”协议。

Intel 管理引擎的设备发现和管理功能需要启用此选项。

参见：新华三集团. H3C HDM MCTP 技术白皮书-6W101[EB/OL]. [2026-03-26]. <https://www.h3c.com/cn/Service/Document_Software/Document_Center/Home/Public/00-Public/Learn_Technologies/White_Paper/H3C_HDM_MCTP_WP-848/>.

## Anti-Rollback SVN Configuration（防回滚 SVN 配置）

Anti-Rollback SVN Configuration 是用于配置 Intel 管理引擎（ME）固件版本控制的选项。该功能通过引入安全版本号（SVN），防止系统降级至较旧或潜在存在安全漏洞的固件版本，从而增强系统的安全性。

### Automatic HW-Enforced Anti-Rollback SVN（自动硬件强制防回滚 SVN）

选项：

Disable（禁用）

Enable（启用）

说明：

启用后，将自动激活硬件强制的防回滚机制：一旦平台成功运行过某个版本的 ME 固件，所有具有更低 ARB-SVN（防回滚安全版本号）的固件将被禁止执行。

### Set HW-Enforced Anti-Rollback for Current SVN（为当前 SVN 设置硬件强制防回滚机制）

选项：

Disable（禁用）

Enable（启用）

说明：

为当前 ARB-SVN 值（ARB 即 Anti-Rollback，防回滚）启用硬件强制的防回滚机制。具有较低 ARB-SVN 的固件将被禁止执行。该值在命令发送后将恢复为禁用状态。

## OEM Key Revocation Configuration（OEM 密钥吊销配置）

“OEM Key Revocation Configuration”是 BIOS/UEFI 中用于管理 OEM 密钥吊销机制的选项。通常用于控制是否启用针对预装系统 OEM 密钥或证书的废止管理。

让 BIOS 通过 HECI 指令吊销（作废）CSME/ME 中的 OEM 密钥，以提升平台安全、避免旧/受损密钥继续被信任。

该功能可用于安全启动相关场景。

### Automatic OEM Key Revocation（OEM 密钥自动吊销）

选项：

Disable（禁用）

Enable（启用）

说明：

启用后，BIOS 将自动发送 HECI 命令以吊销 OEM 密钥。

### Invoke OEM Key Revocation（手动触发 OEM 密钥吊销）

选项：

Disable（禁用）

Enable（启用）

说明：

启用将发送 HECI 命令以吊销 OEM 密钥。
