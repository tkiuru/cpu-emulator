; 07-medium-array-sum-memory.asm
; Difficulty: Medium
; Description: Sum values stored in memory array using indirect addressing
; Expected: Memory[0x10] = 25

DATA 0x20, 3, 7, 2, 9, 4

LOAD R1, 0       ; accumulator
LOAD R2, 0x20    ; pointer
LOAD R3, 5       ; counter

LOOP:
LOAD R4, [R2]    ; load value from memory
ADD R1, R4       ; sum += value
ADD R2, 1        ; pointer++
SUB R3, 1        ; counter--
CMP R3, 0
JGT LOOP

STORE R1, 0x10
HALT
