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
    assert cpu.registers["R1"] == 15
    assert cpu.memory[0] == 15


def test_program_04_multiply():
    cpu = run_program("04-medium-multiply.asm")
    assert cpu.registers["R3"] == 12
    assert cpu.memory[0] == 12


def test_program_05_fibonacci():
    cpu = run_program("05-medium-fibonacci.asm")
    assert cpu.registers["R1"] == 21
    assert cpu.memory[0] == 21


def test_program_06_max_of_three():
    cpu = run_program("06-medium-max-of-three.asm")
    assert cpu.registers["R1"] == 7
    assert cpu.memory[0] == 7


def test_program_07_array_sum():
    cpu = run_program("07-medium-array-sum.asm")
    assert cpu.registers["R1"] == 150
    assert cpu.memory[0] == 150


def test_program_08_reverse_array():
    cpu = run_program("08-medium-reverse-array.asm")
    # [5, 3, 8, 1, 4] reversed → [4, 1, 8, 3, 5]
    assert cpu.memory[0x10:0x15] == [4, 1, 8, 3, 5]
