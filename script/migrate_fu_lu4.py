"""UEFI-Book 项目重构第一步：删除 fu-lu4/ 前缀，将每章提升为顶级目录。

操作内容：
1. 创建 6 个顶级目录（uefi-bios / main / advanced / chipset / security / boot）
2. 将 fu-lu4/ 下的 7 个父页面文件迁移到对应顶级目录（其中 save-exit 迁移到根目录）
3. 检查 fu-lu4/ 是否还有残留文件
4. 若 fu-lu4/ 已空则删除该目录，否则仅报告

本脚本仅做文件系统层面的移动操作，不修改任何文件内容。
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# 项目根目录
ROOT = Path(r"c:\Users\ykla\Documents\UEFI-Book")

# 需要创建的 6 个顶级目录
TOP_LEVEL_DIRS = ["uefi-bios", "main", "advanced", "chipset", "security", "boot"]

# 文件迁移映射：(源相对路径, 目标相对路径)
MIGRATIONS = [
    ("fu-lu4/uefi-bios-gai-shu-yu-jing-gao.md", "uefi-bios/uefi-bios-gai-shu-yu-jing-gao.md"),
    ("fu-lu4/main-zhu-cai-dan.md", "main/main-zhu-cai-dan.md"),
    ("fu-lu4/advanced-gao-ji.md", "advanced/advanced-gao-ji.md"),
    ("fu-lu4/chipset-xin-pian-zu.md", "chipset/chipset-xin-pian-zu.md"),
    ("fu-lu4/security-an-quan.md", "security/security-an-quan.md"),
    ("fu-lu4/boot-qi-dong.md", "boot/boot-qi-dong.md"),
    ("fu-lu4/save-exit-bao-cun-yu-tui-chu.md", "save-exit-bao-cun-yu-tui-chu.md"),  # 根目录
]


def create_top_level_dirs() -> list[str]:
    """创建 6 个顶级目录，返回已创建（或已存在）的目录列表。"""
    created = []
    for name in TOP_LEVEL_DIRS:
        target = ROOT / name
        target.mkdir(parents=True, exist_ok=True)
        created.append(str(target))
    return created


def migrate_files() -> tuple[list[str], list[str]]:
    """迁移文件，返回 (成功列表, 失败列表)。"""
    succeeded: list[str] = []
    failed: list[str] = []

    for src_rel, dst_rel in MIGRATIONS:
        src = ROOT / src_rel
        dst = ROOT / dst_rel

        if not src.exists():
            failed.append(f"源文件不存在: {src}")
            continue

        if dst.exists():
            failed.append(f"目标已存在，跳过: {dst}")
            continue

        # 确保目标父目录存在
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.move(str(src), str(dst))
            succeeded.append(f"{src_rel} -> {dst_rel}")
        except OSError as exc:
            failed.append(f"迁移失败 {src_rel} -> {dst_rel}: {exc}")

    return succeeded, failed


def check_fu_lu4_remaining() -> list[Path]:
    """检查 fu-lu4/ 目录中剩余的文件/子目录。"""
    fu_lu4 = ROOT / "fu-lu4"
    if not fu_lu4.exists():
        return []
    return [p for p in fu_lu4.iterdir()]


def try_remove_fu_lu4(remaining: list[Path]) -> str:
    """若 fu-lu4/ 已空则删除，否则返回报告。"""
    fu_lu4 = ROOT / "fu-lu4"
    if not fu_lu4.exists():
        return "fu-lu4/ 目录已不存在（可能已被删除）"

    if remaining:
        names = ", ".join(p.name for p in remaining)
        return f"fu-lu4/ 目录仍有 {len(remaining)} 个残留项，未删除。残留: {names}"

    # 目录为空，安全删除
    try:
        fu_lu4.rmdir()
        return "fu-lu4/ 目录已空，已成功删除"
    except OSError as exc:
        return f"fu-lu4/ 目录已空但删除失败: {exc}"


def verify(succeeded: list[str], failed: list[str], created_dirs: list[str]) -> None:
    """打印验证信息。"""
    print("=" * 60)
    print("UEFI-Book fu-lu4/ 迁移验证报告")
    print("=" * 60)

    print("\n[1] 顶级目录创建情况：")
    for d in created_dirs:
        exists = "OK" if Path(d).exists() else "MISSING"
        print(f"  [{exists}] {d}")

    print("\n[2] 文件迁移成功 (%d)：" % len(succeeded))
    for item in succeeded:
        print(f"  [OK] {item}")

    if failed:
        print("\n[3] 文件迁移失败 (%d)：" % len(failed))
        for item in failed:
            print(f"  [FAIL] {item}")
    else:
        print("\n[3] 文件迁移失败：0")

    # 验证 7 个目标文件存在
    print("\n[4] 目标文件存在性校验：")
    expected_targets = [ROOT / dst_rel for _, dst_rel in MIGRATIONS]
    all_ok = True
    for t in expected_targets:
        ok = "OK" if t.exists() else "MISSING"
        if not t.exists():
            all_ok = False
        print(f"  [{ok}] {t}")

    # 检查 fu-lu4/ 残留与目录删除
    remaining = check_fu_lu4_remaining()
    removal_msg = try_remove_fu_lu4(remaining)
    print("\n[5] fu-lu4/ 目录最终状态：")
    print(f"  {removal_msg}")
    if remaining:
        print("  残留项明细：")
        for p in remaining:
            kind = "DIR" if p.is_dir() else "FILE"
            print(f"    [{kind}] {p.name}")

    print("\n" + "=" * 60)
    if not failed and all_ok:
        print("总结：全部操作成功完成")
    else:
        print("总结：存在失败项，请检查上方日志")
    print("=" * 60)


def main() -> int:
    # 1. 创建顶级目录
    created_dirs = create_top_level_dirs()

    # 2. 迁移文件
    succeeded, failed = migrate_files()

    # 3 & 4. 验证 + 检查残留 + 删除空目录
    verify(succeeded, failed, created_dirs)

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
