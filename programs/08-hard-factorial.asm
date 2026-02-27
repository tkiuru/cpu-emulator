; 08-hard-factorial.asm
; Difficulty: Hard
; Description: Compute 5! (factorial of 5) using CALL/RET
; Expected: Memory[0x10] = 120
; 5! = 5 * 4 * 3 * 2 * 1 = 120

LOAD R1, 5       ; n = 5
LOAD R2, 1       ; result = 1

LOOP:
CMP R1, 1
JLE DONE
CALL MULTIPLY    ; result = result * n
SUB R1, 1        ; n--
JMP LOOP

DONE:
STORE R2, 0x10
HALT

; Subroutine: R2 = R2 * R1 (using repeated addition)
MULTIPLY:
LOAD R3, 0       ; temp product
LOAD R4, 0
ADD R4, R2       ; counter = result
MULT_LOOP:
CMP R4, 0
JLE MULT_DONE
ADD R3, R1       ; temp += n
SUB R4, 1
JMP MULT_LOOP
MULT_DONE:
LOAD R2, 0
ADD R2, R3       ; result = temp
RET
