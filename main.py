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
print(f"Result: Memory[0x10] = {cpu.memory[0x10]}")
print()
print("Registers:", cpu.registers)
print()
print("Memory dump:")
for row in range(0, 256, 16):
    values = " ".join(f"{cpu.memory[row + i]:02X}" for i in range(16))
    print(f"  0x{row:02X}: {values}")
