from cpu import CPU


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


def test_load_indirect():
    cpu = CPU()
    cpu.memory[0x10] = 42
    cpu.load_program([
        ("LOAD", "R2", 0x10),
        ("LOAD", "R1", "[R2]"),
        ("HALT",),
    ])
    cpu.run()
    assert cpu.registers["R1"] == 42
