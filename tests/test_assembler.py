from assembler import assemble


def test_assemble_add_two_numbers():
    source = """\
LOAD R1, 5
LOAD R2, 8
ADD R1, R2
STORE R1, 0x00
HALT
"""
    result = assemble(source)
    assert result["instructions"] == [
        ("LOAD", "R1", 5),
        ("LOAD", "R2", 8),
        ("ADD", "R1", "R2"),
        ("STORE", "R1", 0),
        ("HALT",),
    ]
    assert result["data"] == {}


def test_assemble_ignores_comments_and_blanks():
    source = """\
; this is a comment

LOAD R1, 1   ; inline comment

; another comment
HALT
"""
    result = assemble(source)
    assert result["instructions"] == [("LOAD", "R1", 1), ("HALT",)]


def test_assemble_hex_values():
    source = "STORE R1, 0xFF"
    result = assemble(source)
    assert result["instructions"] == [("STORE", "R1", 255)]


def test_assemble_indirect_register():
    source = "LOAD R1, [R2]"
    result = assemble(source)
    assert result["instructions"] == [("LOAD", "R1", "[R2]")]


def test_assemble_labels():
    source = """\
LOAD R1, 5
LOOP:
SUB R1, 1
JNE LOOP
HALT
"""
    result = assemble(source)
    assert result["instructions"] == [
        ("LOAD", "R1", 5),
        ("SUB", "R1", 1),
        ("JNE", 1),
        ("HALT",),
    ]


def test_assemble_data_directive():
    source = """\
DATA 0x20, 3, 7, 2
LOAD R1, 0
HALT
"""
    result = assemble(source)
    assert result["instructions"] == [("LOAD", "R1", 0), ("HALT",)]
    assert result["data"] == {0x20: 3, 0x21: 7, 0x22: 2}
