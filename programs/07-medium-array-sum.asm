; 07-medium-array-sum.asm
; Difficulty: Medium
; Description: Sum values stored in memory array
; Setup: Memory[0x20-0x24] = [3, 7, 2, 9, 4]
; Expected: Memory[0x10] = 25
;
; NOTE: This program assumes values are pre-loaded in memory.
; Your emulator should support initializing memory before execution.
; Alternatively, modify this to use immediate values.

; Simple version using immediate values:
LOAD R1, 3
LOAD R2, 7
ADD R1, R2
LOAD R2, 2
ADD R1, R2
LOAD R2, 9
ADD R1, R2
LOAD R2, 4
ADD R1, R2
STORE R1, 0x10
HALT
