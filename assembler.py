"""Assembler: parse .asm text into CPU instruction tuples."""

import re


def _parse_int(s):
    if s.startswith("0x") or s.startswith("0X"):
        return int(s, 16)
    return int(s)


def assemble(text):
    """Parse assembly text into instructions and data.

    Returns a dict with:
        "instructions": list of tuples for cpu.load_program()
        "data": dict mapping memory addresses to values
    """
    # Pass 1: strip comments/blanks, collect labels, DATA directives
    lines = []
    labels = {}
    data = {}
    for line in text.splitlines():
        line = line.split(";")[0].strip()
        if not line:
            continue
        if line.endswith(":"):
            labels[line[:-1]] = len(lines)
            continue
        if line.upper().startswith("DATA "):
            args = [a.strip() for a in line[5:].split(",")]
            addr = _parse_int(args[0])
            for i, val in enumerate(args[1:]):
                data[addr + i] = _parse_int(val)
            continue
        lines.append(line)

    # Pass 2: parse instructions, resolving label references
    instructions = []
    for line in lines:
        parts = re.split(r"\s+", line, maxsplit=1)
        opcode = parts[0].upper()

        if len(parts) == 1:
            instructions.append((opcode,))
        else:
            args = [a.strip() for a in parts[1].split(",")]
            parsed = []
            for arg in args:
                if arg.startswith("[") and arg.endswith("]"):
                    parsed.append("[" + arg[1:-1].upper() + "]")
                elif arg in labels:
                    parsed.append(labels[arg])
                elif arg.upper().startswith("R"):
                    parsed.append(arg.upper())
                else:
                    parsed.append(_parse_int(arg))
            instructions.append((opcode, *parsed))

    return {"instructions": instructions, "data": data}


def assemble_file(path):
    """Read an .asm file and return assembled result."""
    with open(path) as f:
        return assemble(f.read())
