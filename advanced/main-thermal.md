# Main Thermal Configuration（主要热管理配置）

## Critical Temperature (°C)（临界温度）

选项：

90 / 95 / 100 / 105 / 110 / 115 / 117 / 119（单位是摄氏度）

Disabled（禁用）

说明：

启用后，当温度超过该阈（yù）值时，支持 ACPI 的操作系统将执行关键关机操作。允许的范围为 90℃ 至 119℃（含）。

## Passive Cooling Temperature (°C)（被动冷却温度）

选项：

80 / 85 / 90 / 95 / 100 / 105 / 107 / 109（单位是摄氏度）

Disabled（禁用）

说明：

启用后，超过此阈值后，支持 ACPI 的操作系统开始降低 CPU 速度。允许的范围为 80℃ 至 109℃（含）。

## TC1（热常数 1：ACPI 被动冷却公式的一部分）

ACPI 被动冷却公式参见：UEFI 论坛. 11.1.5.1. Processor Clock Throttling[EB/OL]. [2026-03-26]. <https://uefi.org/htmlspecs/ACPI_Spec_6_4_html/11_Thermal_Management/thermal-control.html>。

默认为 1

## TC2（热常数 2：ACPI 被动冷却公式的一部分）

默认为 1

## TSP (tenths of second)（十分之一秒）

被动冷却时的温度采样周期。单位是 100 毫秒，即 0.1 秒。

默认为 5
