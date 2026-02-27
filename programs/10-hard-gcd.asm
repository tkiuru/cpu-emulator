; 10-hard-gcd.asm
; Difficulty: Hard
; Description: Compute GCD of 48 and 18 using Euclidean algorithm
; Expected: Memory[0x10] = 6
; GCD(48, 18) = GCD(18, 12) = GCD(12, 6) = GCD(6, 0) = 6

LOAD R1, 48      ; a
LOAD R2, 18      ; b

LOOP:
CMP R2, 0
JLE DONE

; temp = a % b (using repeated subtraction)
LOAD R3, 0
ADD R3, R1       ; R3 = a (copy)

MOD_LOOP:
CMP R3, R2
JL MOD_DONE
SUB R3, R2
JMP MOD_LOOP

MOD_DONE:
; a = b, b = a % b
LOAD R1, 0
ADD R1, R2       ; a = b
LOAD R2, 0
ADD R2, R3       ; b = remainder

JMP LOOP

DONE:
STORE R1, 0x10
HALT
