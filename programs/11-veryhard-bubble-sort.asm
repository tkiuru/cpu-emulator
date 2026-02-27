; 11-veryhard-bubble-sort.asm
; Difficulty: Very Hard
; Description: Sort 5 values using bubble sort with indirect addressing
; Expected: Memory[0x20-0x24] = [1, 2, 3, 5, 9] (sorted ascending)

DATA 0x20, 5, 3, 9, 1, 2

LOAD R4, 0x24        ; end pointer

OUTER:
LOAD R1, 0x20        ; reset pointer to start
CMP R4, 0x20
JLE DONE             ; end <= start means sorted

INNER:
CMP R1, R4
JGE NEXT_PASS        ; pointer >= end means pass done

; Load adjacent elements
LOAD R2, [R1]        ; current value
ADD R1, 1
LOAD R3, [R1]        ; next value
SUB R1, 1            ; restore pointer

; Compare and swap if out of order
CMP R2, R3
JLE NO_SWAP
STORE R3, [R1]       ; current = smaller
ADD R1, 1
STORE R2, [R1]       ; next = larger
SUB R1, 1            ; restore pointer

NO_SWAP:
ADD R1, 1            ; advance pointer
JMP INNER

NEXT_PASS:
SUB R4, 1            ; shrink end (largest is in place)
JMP OUTER

DONE:
HALT
