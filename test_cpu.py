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
