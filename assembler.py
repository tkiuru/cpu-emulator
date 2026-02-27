"""Assembler: parse .asm text into CPU instruction tuples."""

import re


def assemble(text):
    """Parse assembly text into a list of instruction tuples."""
    # Pass 1: strip comments/blanks, collect labels and their indices
    lines = []
    labels = {}
    for line in text.splitlines():
        line = line.split(";")[0].strip()
        if not line:
            continue
        if line.endswith(":"):
            labels[line[:-1]] = len(lines)
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
                elif arg.startswith("0x") or arg.startswith("0X"):
                    parsed.append(int(arg, 16))
                else:
                    parsed.append(int(arg))
            instructions.append((opcode, *parsed))

    return instructions


def assemble_file(path):
    """Read an .asm file and return instruction tuples."""
    with open(path) as f:
        return assemble(f.read())
