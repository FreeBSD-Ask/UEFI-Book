# BIOS 与 UEFI 简介

本节介绍 BIOS 和 UEFI 的基本概念、发展历程及主要区别。

BIOS（Basic Input/Output System，基本输入输出系统）是计算机启动时最先执行的固件程序，多采用汇编语言编写以实现硬件直接操作。BIOS 最早出现于 20 世纪 70 年代（1974 年，加里·基尔代尔为 Intel 8080 微处理器开发的 CP/M 操作系统首次引入了 BIOS 概念），其工作流程包括加电自检（POST）、硬件初始化、引导加载等步骤，目的是识别和初始化处理器、内存、硬盘驱动器、光驱以及其他硬件。BIOS 采用实模式运行，地址空间限制在 1 MB 以内。

UEFI（Unified Extensible Firmware Interface，统一可扩展固件接口）是一种规范，定义了操作系统和平台固件之间的软件接口，多采用 C/C++ 编写以支持模块化开发。相比 BIOS，UEFI 具有支持更大磁盘分区（GPT）、图形界面、网络启动、安全启动（Secure Boot）等优势。UEFI 的原型 EFI 最早由 Intel 于 1998 年启动的 Intel Boot Initiative（IBI）计划开发，至 EFI 1.10 版本后于 2005 年交由统一 EFI 论坛（UEFI Forum）继续维护并更名为 UEFI。UEFI 取代了基本输入输出系统（BIOS）的固件接口，大多数 UEFI 固件实现仍提供对 BIOS 服务的遗留支持以兼容旧操作系统。

目前主流电脑（自 2012 年微软要求 Windows 8 认证必须支持 UEFI 起，约 2012—2013 年间）配备的都是 UEFI，而不是传统的 BIOS。由于 UEFI 在界面和操作逻辑上与 BIOS 类似，且需要向后兼容，人们仍习惯将其统称为 BIOS 或 UEFI BIOS。
