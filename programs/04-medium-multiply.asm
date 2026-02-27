; 04-medium-multiply.asm
; Difficulty: Medium
; Description: Multiply 6 x 7 using repeated addition
; Expected: Memory[0x10] = 42

LOAD R1, 6       ; multiplicand
LOAD R2, 7       ; multiplier (counter)
LOAD R3, 0       ; result accumulator

LOOP:
CMP R2, 0
JLE DONE
ADD R3, R1       ; result += multiplicand
SUB R2, 1        ; counter--
JMP LOOP

DONE:
STORE R3, 0x10
HALT
