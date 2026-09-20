# -*- coding: utf-8 -*-
"""
递归列出 C 盘（或指定目录）下所有文件夹和文件名。

用法:
    python list_drive.py                          # 扫描 C:\，结果写入 c_drive_list.txt
    python list_drive.py -r D:\ -o d_list.txt     # 扫描 D 盘
    python list_drive.py --no-progress            # 不显示进度
"""

import argparse
import os
import sys
import time

sys.setrecursionlimit(20000)  # 目录层级很深时，防止递归深度报错


def scan(path, out, depth, stats, progress):
    """递归扫描 path 下的所有内容，写入 out"""
    try:
        entries = list(os.scandir(path))
    except PermissionError:
        stats["denied"] += 1
        out.write("  " * depth + f"[拒绝访问] {path}\n")
        return
    except OSError as e:
        stats["error"] += 1
        code = getattr(e, "winerror", None) or e.errno
        out.write("  " * depth + f"[错误 {code}] {path}\n")
        return

    for entry in entries:
        indent = "  " * (depth + 1)
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError:
            is_dir = False

        if is_dir:
            # 符号链接 / junction 不递归，防止死循环和重复扫描
            if entry.is_symlink():
                out.write(indent + f"[链接跳过] {entry.name}\n")
                continue

            stats["dirs"] += 1
            out.write(indent + f"[目录] {entry.name}\n")

            if progress and stats["dirs"] % 2000 == 0:
                print(f"\r已扫描 目录 {stats['dirs']:,} 个 / 文件 {stats['files']:,} 个 ...",
                      end="", flush=True)

            scan(entry.path, out, depth + 1, stats, progress)
        else:
            stats["files"] += 1
            try:
                size = entry.stat(follow_symlinks=False).st_size
                size_txt = f"  ({size} 字节)"
            except OSError:
                size_txt = ""
            out.write(indent + f"[文件] {entry.name}{size_txt}\n")


def main():
    ap = argparse.ArgumentParser(description="递归列出目录下所有文件/文件夹")
    ap.add_argument("-r", "--root", default="C:\\", help="起始目录，默认 C:\\")
    ap.add_argument("-o", "--out", default="c_drive_list.txt", help="输出文件名")
    ap.add_argument("--encoding", default="utf-8", help="输出文件编码，默认 utf-8")
    ap.add_argument("--no-progress", action="store_true", help="不显示控制台进度")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"目录不存在或不可访问: {root}")
        return 1

    stats = {"dirs": 0, "files": 0, "denied": 0, "error": 0}
    start = time.time()

    with open(args.out, "w", encoding=args.encoding,
              errors="replace", buffering=1 << 20) as out:
        out.write(f"# 扫描根目录: {root}\n")
        out.write(f"# 开始时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        scan(root, out, 0, stats, not args.no_progress)

        out.write("\n# ================= 统计 =================\n")
        out.write(f"# 目录总数  : {stats['dirs']}\n")
        out.write(f"# 文件总数  : {stats['files']}\n")
        out.write(f"# 拒绝访问  : {stats['denied']}\n")
        out.write(f"# 其他错误  : {stats['error']}\n")
        out.write(f"# 耗时      : {time.time() - start:.1f} 秒\n")

    print(f"\r完成！目录 {stats['dirs']:,} 个，文件 {stats['files']:,} 个，"
          f"拒绝访问 {stats['denied']:,} 个，其他错误 {stats['error']:,} 个，"
          f"耗时 {time.time() - start:.1f} 秒")
    print(f"结果已写入: {os.path.abspath(args.out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
