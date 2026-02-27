from pathlib import Path

from cpu import CPU
from assembler import assemble_file

PROGRAMS_DIR = Path(__file__).parent.parent / "programs"


def run_program(filename):
    cpu = CPU()
    cpu.load_program(assemble_file(PROGRAMS_DIR / filename))
    cpu.run()
    return cpu


def test_program_01_add_two_numbers():
    cpu = run_program("01-easy-add-two-numbers.asm")
    assert cpu.registers["R1"] == 13
    assert cpu.memory[0x10] == 13


def test_program_02_count_down():
    cpu = run_program("02-easy-count-down.asm")
    assert cpu.registers["R1"] == -1
    assert cpu.memory[0x10] == 0


def test_program_03_sum_1_to_5():
    cpu = run_program("03-easy-sum-1-to-5.asm")
    assert cpu.registers["R3"] == 15
    assert cpu.memory[0x10] == 15


def test_program_04_multiply():
    cpu = run_program("04-medium-multiply.asm")
    assert cpu.registers["R3"] == 42
    assert cpu.memory[0x10] == 42


def test_program_05_fibonacci():
    cpu = run_program("05-medium-fibonacci.asm")
    assert cpu.registers["R2"] == 21
    assert cpu.memory[0x10] == 21


def test_program_06_max_of_three():
    cpu = run_program("06-medium-max-of-three.asm")
    assert cpu.registers["R4"] == 42
    assert cpu.memory[0x10] == 42


def test_program_07_array_sum():
    cpu = run_program("07-medium-array-sum.asm")
    assert cpu.registers["R1"] == 25
    assert cpu.memory[0x10] == 25


def test_program_07_array_sum_memory():
    cpu = run_program("07-medium-array-sum-memory.asm")
    assert cpu.registers["R1"] == 25
    assert cpu.memory[0x10] == 25


def test_program_08_factorial():
    cpu = run_program("08-hard-factorial.asm")
    assert cpu.registers["R2"] == 120
    assert cpu.memory[0x10] == 120
