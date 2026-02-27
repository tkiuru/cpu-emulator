; 09-hard-division.asm
; Difficulty: Hard
; Description: Integer division 47 / 5 with quotient and remainder
; Expected: Memory[0x10] = 9 (quotient), Memory[0x11] = 2 (remainder)
; 47 = 5 * 9 + 2

LOAD R1, 47      ; dividend
LOAD R2, 5       ; divisor
LOAD R3, 0       ; quotient

LOOP:
CMP R1, R2
JL DONE          ; if dividend < divisor, done
SUB R1, R2       ; dividend -= divisor
ADD R3, 1        ; quotient++
JMP LOOP

DONE:
STORE R3, 0x10   ; store quotient
STORE R1, 0x11   ; store remainder (what's left in R1)
HALT
