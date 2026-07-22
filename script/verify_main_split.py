import os

base = r"c:\Users\ykla\Documents\UEFI-Book\main"
files = [
    "top-header.md",
    "menu-options.md",
    "main-page-content.md",
    "right-help-info.md",
    "keyboard-help.md",
    "bottom-version-info.md",
    "main-zhu-cai-dan.md",
]

print(f"{'file':<28} {'BOM':<6} {'CRLF':<6} {'first_line'}")
print("-" * 80)
for f in files:
    p = os.path.join(base, f)
    with open(p, "rb") as fh:
        data = fh.read()
    has_bom = data.startswith(b"\xef\xbb\xbf")
    has_crlf = b"\r\n" in data
    has_lf = b"\n" in data
    # decode for first line
    if has_bom:
        text = data[3:].decode("utf-8", errors="replace")
    else:
        text = data.decode("utf-8", errors="replace")
    first_line = text.split("\n", 1)[0]
    line_ending = "CRLF" if has_crlf else ("LF" if has_lf else "none")
    print(f"{f:<28} {str(has_bom):<6} {line_ending:<6} {first_line}")
