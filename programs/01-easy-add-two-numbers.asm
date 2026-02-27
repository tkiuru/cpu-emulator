; 01-easy-add-two-numbers.asm
; Difficulty: Easy
; Description: Add two numbers and store result
; Expected: Memory[0x10] = 13

LOAD R1, 5
LOAD R2, 8
ADD R1, R2
STORE R1, 0x10
HALT
