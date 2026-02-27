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


def test_assemble_add_two_numbers():
    source = """\
LOAD R1, 5
LOAD R2, 8
ADD R1, R2
STORE R1, 0x00
HALT
"""
    cpu = CPU()
    cpu.load_program(assemble(source))
    cpu.run()
    assert cpu.registers["R1"] == 13
    assert cpu.memory[0] == 13


def test_assemble_ignores_comments_and_blanks():
    source = """\
; this is a comment

LOAD R1, 1   ; inline comment

; another comment
HALT
"""
    instructions = assemble(source)
    assert instructions == [("LOAD", "R1", 1), ("HALT",)]


def test_assemble_hex_values():
    source = "STORE R1, 0xFF"
    instructions = assemble(source)
    assert instructions == [("STORE", "R1", 255)]


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
