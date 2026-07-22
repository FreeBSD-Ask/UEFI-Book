#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Split advanced-gao-ji.md by H2 headers into 22 sub-files.

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

BASE = r'c:\Users\ykla\Documents\UEFI-Book\advanced'
SOURCE = os.path.join(BASE, 'advanced-gao-ji.md')

# Ordered list of output filenames, one per H2 section (in file order).
OUTPUT_FILES = [
    'connectivity-configuration.md',
    'cpu-configuration.md',
    'power-performance.md',
    'pch-fw-configuration.md',
    'intel-tcc.md',
    'trusted-computing.md',
    'acpi-settings.md',
    'serial-port-console-redirection.md',
    'acoustic-management.md',
    'ami-graphic-output.md',
    'usb-configuration.md',
    'network-stack.md',
    'csm-configuration.md',
    'nvme-configuration.md',
    'sdio-configuration.md',
    'main-thermal.md',
    'lvds-configuration.md',
    'embedded-controller.md',
    'ram-disk.md',
    'tls-auth.md',
    'ethernet-controller-i226.md',
    'driver-health.md',
]

EXPECTED_H2_COUNT = len(OUTPUT_FILES)


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


def count_headings(lines):
    """Count heading levels outside code blocks."""
    h_levels = {'#': 0, '##': 0, '###': 0, '####': 0, '#####': 0, '######': 0}
    in_code = False
    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        stripped = line.lstrip()
        if not stripped.startswith('#'):
            continue
        # Count leading hashes
        n = 0
        while n < len(stripped) and stripped[n] == '#':
            n += 1
        # Must be followed by space or end-of-line to be a heading
        if n < len(stripped) and stripped[n] != ' ':
            continue
        key = '#' * n
        if key in h_levels:
            h_levels[key] += 1
    return h_levels


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
    # Remove a single trailing empty string produced by final newline
    if lines and lines[-1] == '':
        lines.pop()
        had_trailing_nl = True
    else:
        had_trailing_nl = False

    original_line_count = len(lines)

    # Find H2 lines (## followed by space), NOT inside code blocks
    h2_indices = []
    in_code = False
    for i, line in enumerate(lines):
        if is_code_fence(line):
            in_code = not in_code
            continue
        if not in_code and line.startswith('## ') and not line.startswith('### '):
            h2_indices.append(i)

    print('Found {} H2 headers:'.format(len(h2_indices)))
    for idx in h2_indices:
        print('  Line {} (1-indexed): {}'.format(idx + 1, lines[idx]))

    if len(h2_indices) != EXPECTED_H2_COUNT:
        print('ERROR: Expected {} H2 headers, found {}'.format(
            EXPECTED_H2_COUNT, len(h2_indices)))
        sys.exit(1)

    if len(OUTPUT_FILES) != EXPECTED_H2_COUNT:
        print('ERROR: OUTPUT_FILES list has {} entries, expected {}'.format(
            len(OUTPUT_FILES), EXPECTED_H2_COUNT))
        sys.exit(1)

    # Build section boundaries (start, end) where end is exclusive
    sections = []
    for i, start in enumerate(h2_indices):
        end = h2_indices[i + 1] if i + 1 < len(h2_indices) else len(lines)
        sections.append((start, end))

    # Parent file: everything before the first H2
    parent_lines = lines[:h2_indices[0]]

    # Write each section to its output file
    written = []
    for (start, end), out_name in zip(sections, OUTPUT_FILES):
        section_lines = lines[start:end]
        section_lines = process_section(section_lines)
        out_path = os.path.join(BASE, out_name)
        write_file(out_path, section_lines)
        written.append((out_path, out_name, section_lines))

        # Sanity: first line must be '# <title>'
        first = section_lines[0] if section_lines else ''
        if not first.startswith('# ') or first.startswith('## '):
            print('ERROR: {} first line is not H1: {!r}'.format(out_name, first))
            sys.exit(1)

    # Update parent file
    write_file(SOURCE, parent_lines)

    print('')
    print('=== Results ===')
    print('Updated parent: {} ({} lines)'.format(SOURCE, len(parent_lines)))
    for out_path, out_name, section_lines in written:
        print('Created: {} ({} lines)'.format(out_name, len(section_lines)))

    # Verify no content loss: line count check
    total = len(parent_lines) + sum(len(s) for _, _, s in written)
    print('')
    print('=== Line count check ===')
    print('Original total lines: {}'.format(original_line_count))
    print('Parent + sections:    {}'.format(total))
    if total == original_line_count:
        print('PASS: No lines lost.')
    else:
        print('WARNING: Line count mismatch! diff={}'.format(total - original_line_count))

    # Verify each sub-file first line and heading levels
    print('')
    print('=== Sub-file heading verification ===')
    for out_path, out_name, section_lines in written:
        first = section_lines[0]
        h = count_headings(section_lines)
        print('{}: first={!r} | H1={} H2={} H3={} H4={}'.format(
            out_name, first, h['#'], h['##'], h['###'], h['####']))

    # Verify parent file
    print('')
    print('=== Parent file verification ===')
    print('First line: {!r}'.format(parent_lines[0] if parent_lines else ''))
    print('Last line:  {!r}'.format(parent_lines[-1] if parent_lines else ''))
    parent_h = count_headings(parent_lines)
    print('Headings: H1={} H2={} H3={} H4={}'.format(
        parent_h['#'], parent_h['##'], parent_h['###'], parent_h['####']))

    # Verify BOM absence
    print('')
    print('=== BOM check ===')
    check_paths = [SOURCE] + [p for p, _, _ in written]
    all_ok = True
    for path in check_paths:
        with open(path, 'rb') as f:
            head = f.read(3)
        status = 'BOM present!' if head == b'\xef\xbb\xbf' else 'No BOM (OK)'
        if head == b'\xef\xbb\xbf':
            all_ok = False
        print('  {}: {}'.format(os.path.basename(path), status))

    # Verify LF line endings
    print('')
    print('=== Line ending check ===')
    for path in check_paths:
        with open(path, 'rb') as f:
            data = f.read()
        crlf_count = data.count(b'\r\n')
        lone_cr = data.count(b'\r') - crlf_count
        print('  {}: CRLF={}, lone CR={}'.format(
            os.path.basename(path), crlf_count, lone_cr))

    print('')
    if all_ok:
        print('All checks passed.')
    else:
        print('Some checks failed - review output above.')


if __name__ == '__main__':
    main()
