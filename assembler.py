"""Assembler: parse .asm text into CPU instruction tuples."""

import re


def assemble(text):
    """Parse assembly text into a list of instruction tuples."""
    instructions = []
    for line in text.splitlines():
        # Strip comments
        line = line.split(";")[0].strip()
        if not line:
            continue

        # Split opcode from arguments
        parts = re.split(r"\s+", line, maxsplit=1)
        opcode = parts[0].upper()

        if len(parts) == 1:
            # No arguments (e.g. HALT)
            instructions.append((opcode,))
        else:
            args = [a.strip() for a in parts[1].split(",")]
            parsed = []
            for arg in args:
                if arg.startswith("[") and arg.endswith("]"):
                    parsed.append("[" + arg[1:-1].upper() + "]")
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
