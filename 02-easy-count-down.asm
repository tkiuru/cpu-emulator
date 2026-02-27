; Program 02: Count down from 5 to 0
LOAD R1, 5
SUB R1, 1
CMP R1, 0
JNE 1
STORE R1, 0x00
HALT
