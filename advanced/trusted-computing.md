# Trusted computing（可信计算）

## Security Device Support（安全设备支持）

选项：

Disable（禁用）

Enable（启用）

说明：

禁用后，操作系统将不会显示安全设备。TCG EFI 协议和 INT 1Ah 接口将不可用。

启用后，以下所有项目将可用：

### SHA256 PCR Bank（SHA256 PCR 存储单元）

选项：

Disable（禁用）

Enable（启用）

说明：

TPM 所需的一种算法。随意修改可能影响 BitLocker 恢复密钥的有效性（与特定算法存在绑定关系）。

### SHA384 PCR Bank（SHA384 PCR 存储单元）

同上。

### SM3_256 PCR Bank（SM3_256 PCR 存储单元）

同上。

### Pending Operation（待执行操作）

选项：

None（无）

TPM Clear（重置 TPM）

为安全设备安排操作。注意：计算机将重启以完成安全设备状态的更改。

### Platform Hierarchy（平台层级）

选项：

Disable（禁用）

Enable（启用）

说明：

是否允许平台固件使用 TPM 进行密钥管理和固件验证。

平台层级即受平台制造商控制的 TPM 2.0 密钥管理层次。由平台固件控制，主要用于系统启动过程中的安全验证。

### Storage Hierarchy（存储层级）

选项：

Disable（禁用）

Enable（启用）

说明：

在 TPM 2.0 中，存储层级用于存储密钥、策略和授权值，供平台所有者使用。由平台所有者控制，主要用于密钥和策略管理。启用后，操作系统可以使用 TPM 进行密钥存储和策略管理。

### Endorsement Hierarchy（批准层级）

选项：

Disable（禁用）

Enable（启用）

说明：

由 TPM 制造商控制，主要用于认证 TPM 的真实性。

### Physical Presence Spec Version（物理存在规范版本）

选项：

1.2

1.3

说明：

选择此项目将告知 OS 支持 PPI（Physical Presence Interface，物理存在接口）规范版本 1.2 或 1.3。请注意，一些 HCK 测试（一种用于验证硬件设备和驱动程序与 Windows 操作系统的兼容性的测试框架，用于获得数字证书）可能不支持版本 1.3。
物理存在接口利用行业标准的高级配置和电源接口（ACPI）在操作系统和 BIOS 之间提供通信机制，使操作系统和 BIOS 能够协作，提供简单直接的平台用户体验来管理 TPM，而无需牺牲安全性。

### Device Select（设备选择）

选项：

Auto（自动）

TPM 1.2

TPM 2.0

说明：

使用此项选择支持的 TPM 设备。TPM 1.2 将仅支持 TPM 1.2 设备，TPM 2.0 将仅支持 TPM 2.0 设备，自动（Auto）模式则同时支持两者；在默认情况下，如果未找到 TPM 2.0 设备，将选中 TPM 1.2 设备。
