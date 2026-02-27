; 02-easy-count-down.asm
; Difficulty: Easy
; Description: Count down from 5 to 0
; Expected: Memory[0x10] = 0, program executes 6 iterations

LOAD R1, 5

LOOP:
STORE R1, 0x10
SUB R1, 1
CMP R1, 0
JGE LOOP

HALT
