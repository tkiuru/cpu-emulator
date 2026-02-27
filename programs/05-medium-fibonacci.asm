; 05-medium-fibonacci.asm
; Difficulty: Medium
; Description: Compute 8th Fibonacci number
; Expected: Memory[0x10] = 21
; Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

LOAD R1, 0       ; fib(n-2)
LOAD R2, 1       ; fib(n-1)
LOAD R3, 8       ; counter (which fib number)
LOAD R4, 0       ; temp for swap

; Handle edge cases
CMP R3, 0
JLE STORE_R1
CMP R3, 1
JLE STORE_R2

SUB R3, 1        ; adjust counter

LOOP:
CMP R3, 0
JLE DONE

; R4 = R1 + R2
LOAD R4, 0
ADD R4, R1
ADD R4, R2

; shift: R1 = R2, R2 = R4
LOAD R1, 0
ADD R1, R2
LOAD R2, 0
ADD R2, R4

SUB R3, 1
JMP LOOP

STORE_R1:
STORE R1, 0x10
HALT

STORE_R2:
STORE R2, 0x10
HALT

DONE:
STORE R2, 0x10
HALT
