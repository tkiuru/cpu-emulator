; 12-veryhard-primes.asm
; Difficulty: Very Hard
; Description: Check if 17 is prime
; Expected: Memory[0x10] = 1 (true, 17 is prime)
;
; Algorithm: Trial division from 2 to sqrt(n)
; For 17: check divisibility by 2, 3, 4 (4*4=16 < 17, 5*5=25 > 17)

LOAD R1, 17      ; number to test
LOAD R2, 2       ; divisor, start at 2
LOAD R3, 1       ; result: assume prime (1 = true)

CHECK_LOOP:
; Check if R2 * R2 > R1 (done checking)
LOAD R4, 0
ADD R4, R2
; Compute R2 * R2 using repeated addition
LOAD R3, 0       ; use R3 as temp counter
ADD R3, R2

SQUARE_LOOP:
CMP R3, 1
JLE SQUARE_DONE
ADD R4, R2
SUB R3, 1
JMP SQUARE_LOOP

SQUARE_DONE:
; R4 now holds R2 * R2
CMP R4, R1
JG IS_PRIME       ; if divisor^2 > n, it's prime

; Check if R1 % R2 == 0
LOAD R3, 0
ADD R3, R1

MOD_LOOP:
CMP R3, R2
JL MOD_DONE
SUB R3, R2
JMP MOD_LOOP

MOD_DONE:
CMP R3, 0
JLE NOT_PRIME     ; if remainder is 0, not prime

ADD R2, 1         ; try next divisor
JMP CHECK_LOOP

NOT_PRIME:
LOAD R3, 0
STORE R3, 0x10
HALT

IS_PRIME:
LOAD R3, 1
STORE R3, 0x10
HALT
