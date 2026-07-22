#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split chipset-xin-pian-zu.md by H2 headers into sub-files.

Rules:
- Split at H2 (##) boundaries (dynamically detected, not hardcoded line numbers)
- Each sub-file: first line is '# <title>' (H2 -> H1), H3 -> H2, H4 -> H3, etc.
- Parent file keeps only H1 + intro (lines before the first H2)
- UTF-8 (no BOM), LF line endings
- Don't modify any content text, only split and adjust heading levels
- Skip heading adjustment inside code blocks (``` or ~~~ fences)
- Image paths remain unchanged (../.gitbook/assets/)
"""

import os
import sys

BASE = r'c:\Users\ykla\Documents\UEFI-Book\chipset'
SOURCE = os.path.join(BASE, 'chipset-xin-pian-zu.md')
SA_OUT = os.path.join(BASE, 'sa-configuration.md')
PCH_OUT = os.path.join(BASE, 'pch-io-configuration.md')


def is_code_fence(line):
    """Check if line starts a code fence (``` or ~~~)."""
    stripped = line.lstrip()
    return stripped.startswith('```') or stripped.startswith('~~~')


def adjust_heading(line):
    """Adjust heading level down by one.
    H2(##) -> H1(#), H3(###) -> H2(##), H4(####) -> H3(###), etc.
    Only for lines with 2+ leading hashes followed by a space.
    Lines with 1 hash (# H1) are left unchanged.
    """
    i = 0
    while i < len(line) and line[i] == '#':
        i += 1
    # i = number of leading hashes
    if i >= 2 and i < len(line) and line[i] == ' ':
        return '#' * (i - 1) + line[i:]
    return line


def process_section(lines):
    """Adjust heading levels for a section, skipping code blocks."""
    result = []
    in_code = False
    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            result.append(line)
            continue
        if not in_code:
            line = adjust_heading(line)
        result.append(line)
    return result


def write_file(path, file_lines):
    """Write file with UTF-8 (no BOM), LF line endings, trailing newline."""
    text = '\n'.join(file_lines)
    if not text.endswith('\n'):
        text = text + '\n'
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)


def main():
    # Read source file as binary first to detect BOM
    with open(SOURCE, 'rb') as f:
        raw = f.read()

    has_bom = raw.startswith(b'\xef\xbb\xbf')
    if has_bom:
        raw = raw[3:]
        print('WARNING: Source file had BOM, removing it.')

    # Decode and normalize line endings to LF
    content = raw.decode('utf-8')
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    lines = content.split('\n')

    # Find H2 lines (## followed by space), NOT inside code blocks
    h2_indices = []
    in_code = False
    for i, line in enumerate(lines):
        if is_code_fence(line):
            in_code = not in_code
            continue
        if not in_code and line.startswith('## '):
            h2_indices.append(i)

    print('Found {} H2 headers:'.format(len(h2_indices)))
    for idx in h2_indices:
        print('  Line {} (1-indexed): {}'.format(idx + 1, lines[idx]))

    if len(h2_indices) != 2:
        print('ERROR: Expected 2 H2 headers, found {}'.format(len(h2_indices)))
        sys.exit(1)

    first_h2 = h2_indices[0]
    second_h2 = h2_indices[1]

    # Parent file: everything before the first H2
    parent_lines = lines[:first_h2]

    # SA section: from first H2 to just before second H2
    sa_lines = lines[first_h2:second_h2]

    # PCH-IO section: from second H2 to end of file
    pch_lines = lines[second_h2:]

    # Adjust heading levels for sub-files
    sa_lines = process_section(sa_lines)
    pch_lines = process_section(pch_lines)

    # Write all files
    write_file(SA_OUT, sa_lines)
    write_file(PCH_OUT, pch_lines)
    write_file(SOURCE, parent_lines)

    print('')
    print('=== Results ===')
    print('Created: {} ({} lines)'.format(SA_OUT, len(sa_lines)))
    print('Created: {} ({} lines)'.format(PCH_OUT, len(pch_lines)))
    print('Updated: {} ({} lines)'.format(SOURCE, len(parent_lines)))
    print('')
    print('=== Verification ===')
    print('SA first line:    {}'.format(sa_lines[0]))
    print('PCH first line:  {}'.format(pch_lines[0]))
    print('Parent first:    {}'.format(parent_lines[0]))
    print('Parent last:     {}'.format(repr(parent_lines[-1])))
    print('')

    # Verify no content loss: line count check
    total = len(parent_lines) + len(sa_lines) + len(pch_lines)
    original = len(lines)
    print('=== Line count check ===')
    print('Original total lines: {}'.format(original))
    print('Parent + SA + PCH:    {} (parent={} + sa={} + pch={})'.format(
        total, len(parent_lines), len(sa_lines), len(pch_lines)))
    if total == original:
        print('PASS: No lines lost.')
    else:
        print('WARNING: Line count mismatch! diff={}'.format(total - original))

    # Verify heading levels in sub-files
    print('')
    print('=== Heading level check (SA) ===')
    h_levels = {'#': 0, '##': 0, '###': 0, '####': 0}
    in_code = False
    for line in sa_lines:
        if is_code_fence(line):
            in_code = not in_code
            continue
        if not in_code:
            if line.startswith('# ') and not line.startswith('## '):
                h_levels['#'] += 1
            elif line.startswith('## ') and not line.startswith('### '):
                h_levels['##'] += 1
            elif line.startswith('### ') and not line.startswith('#### '):
                h_levels['###'] += 1
            elif line.startswith('#### ') and not line.startswith('##### '):
                h_levels['####'] += 1
    print('  H1={H1}, H2={H2}, H3={H3}, H4={H4}'.format(
        H1=h_levels['#'], H2=h_levels['##'], H3=h_levels['###'], H4=h_levels['####']))

    print('')
    print('=== Heading level check (PCH) ===')
    h_levels = {'#': 0, '##': 0, '###': 0, '####': 0}
    in_code = False
    for line in pch_lines:
        if is_code_fence(line):
            in_code = not in_code
            continue
        if not in_code:
            if line.startswith('# ') and not line.startswith('## '):
                h_levels['#'] += 1
            elif line.startswith('## ') and not line.startswith('### '):
                h_levels['##'] += 1
            elif line.startswith('### ') and not line.startswith('#### '):
                h_levels['####'] += 1
            elif line.startswith('#### ') and not line.startswith('##### '):
                h_levels['####'] += 1
    print('  H1={H1}, H2={H2}, H3={H3}, H4={H4}'.format(
        H1=h_levels['#'], H2=h_levels['##'], H3=h_levels['###'], H4=h_levels['####']))

    # Verify BOM absence
    print('')
    print('=== BOM check ===')
    for path in [SA_OUT, PCH_OUT, SOURCE]:
        with open(path, 'rb') as f:
            head = f.read(3)
        status = 'BOM present!' if head == b'\xef\xbb\xbf' else 'No BOM (OK)'
        print('  {}: {}'.format(os.path.basename(path), status))

    # Verify LF line endings
    print('')
    print('=== Line ending check ===')
    for path in [SA_OUT, PCH_OUT, SOURCE]:
        with open(path, 'rb') as f:
            data = f.read()
        crlf_count = data.count(b'\r\n')
        lone_cr = data.count(b'\r') - crlf_count
        print('  {}: CRLF={}, lone CR={}'.format(
            os.path.basename(path), crlf_count, lone_cr))


if __name__ == '__main__':
    main()
