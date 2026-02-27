"""Run an assembly program on the CPU."""

from assembler import assemble_file
from cpu import CPU

cpu = CPU()
cpu.load_program(assemble_file("01-easy-add-two-numbers.asm"))
cpu.run()
print("Registers:", cpu.registers)
print(f"Memory[0x00] = {cpu.memory[0x00]}")
