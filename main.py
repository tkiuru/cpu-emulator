"""Run an assembly program on the CPU."""

import sys

from assembler import assemble_file
from cpu import CPU

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <program.asm>")
    sys.exit(1)

cpu = CPU()
cpu.load_program(assemble_file(sys.argv[1]))
cpu.run()
print("Registers:", cpu.registers)
print(f"Memory[0x00] = {cpu.memory[0x00]}")
