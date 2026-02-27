; 03-easy-sum-1-to-5.asm
; Difficulty: Easy
; Description: Compute sum of 1 to 5 (official test program)
; Expected: Memory[0x10] = 15

LOAD R1, 1
LOAD R2, 5
LOAD R3, 0

LOOP:
ADD R3, R1
ADD R1, 1
CMP R1, R2
JLE LOOP

STORE R3, 0x10
HALT
