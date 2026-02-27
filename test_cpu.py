from cpu import CPU
from assembler import assemble


def test_load():
    cpu = CPU()
    cpu.load_program([("LOAD", "R1", 42), ("HALT",)])
    cpu.run()
    assert cpu.registers["R1"] == 42


def test_add_registers():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 10),
        ("LOAD", "R2", 20),
        ("ADD", "R1", "R2"),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 30


def test_add_immediate():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 7),
        ("ADD", "R1", 3),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 10


def test_halt_stops():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 1),
        ("HALT",),
        ("LOAD", "R1", 99),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 1


def test_store():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 42),
        ("STORE", "R1", 10),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.memory[10] == 42


def test_store_hex_address():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R2", 99),
        ("STORE", "R2", 0x10),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.memory[0x10] == 99


def test_program_01():
    """Program 01: LOAD 5, LOAD 8, ADD → R1=13."""
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 5),
        ("LOAD", "R2", 8),
        ("ADD", "R1", "R2"),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 13


def test_sub_immediate():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 10),
        ("SUB", "R1", 3),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 7


def test_sub_register():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 20),
        ("LOAD", "R2", 5),
        ("SUB", "R1", "R2"),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 15


def test_cmp_jne_loops():
    """SUB and JNE loop: count from 3 down to 0."""
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 3),   # 0
        ("SUB", "R1", 1),    # 1
        ("CMP", "R1", 0),    # 2
        ("JNE", 1),          # 3 → jump back to SUB
        ("HALT",),           # 4
    ])
    cpu.run()
    assert cpu.registers["R1"] == 0


def test_jne_no_jump_when_equal():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 0),
        ("CMP", "R1", 0),
        ("JNE", 0),          # should NOT jump, values are equal
        ("HALT",),
    ])
    cpu.run()
    assert cpu.halted


def test_program_02():
    """Program 02: Count down from 5 to 0."""
    source = """\
LOAD R1, 5
SUB R1, 1
CMP R1, 0
JNE 1
STORE R1, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R1"] == 0
    assert cpu.memory[0] == 0


def test_program_03():
    """Program 03: Sum 1 to 5 = 15."""
    source = """\
LOAD R1, 0
LOAD R2, 5
ADD R1, R2
SUB R2, 1
CMP R2, 0
JNE 2
STORE R1, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R1"] == 15
    assert cpu.memory[0] == 15


def test_program_04():
    """Program 04: Multiply 3 × 4 = 12."""
    source = """\
LOAD R1, 3
LOAD R2, 4
LOAD R3, 0
ADD R3, R1
SUB R2, 1
CMP R2, 0
JNE 3
STORE R3, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R3"] == 12
    assert cpu.memory[0] == 12


def test_program_05():
    """Program 05: Fibonacci fib(8) = 21."""
    source = """\
LOAD R1, 0
LOAD R2, 1
LOAD R3, 8
LOAD R4, 0
ADD R4, R2
ADD R2, R1
LOAD R1, 0
ADD R1, R4
SUB R3, 1
CMP R3, 0
JNE 3
STORE R1, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R1"] == 21
    assert cpu.memory[0] == 21


def test_jgt_jumps_when_greater():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 10),
        ("CMP", "R1", 5),
        ("JGT", 4),          # should jump past the LOAD
        ("LOAD", "R1", 0),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 10


def test_jgt_no_jump_when_less():
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 3),
        ("CMP", "R1", 5),
        ("JGT", 4),          # should NOT jump
        ("LOAD", "R1", 99),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 99


def test_program_06():
    """Program 06: Max of (3, 7, 5) = 7."""
    source = """\
LOAD R1, 3
LOAD R2, 7
LOAD R3, 5
CMP R1, R2
JGT 7
LOAD R1, 0
ADD R1, R2
CMP R1, R3
JGT 11
LOAD R1, 0
ADD R1, R3
STORE R1, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R1"] == 7
    assert cpu.memory[0] == 7
