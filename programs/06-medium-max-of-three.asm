; Program 06: Find the max of three numbers (3, 7, 5) → 7
LOAD R1, 3
LOAD R2, 7
LOAD R3, 5
; max(R1, R2) → R1
CMP R1, R2
JGT 7            ; R1 > R2? skip copy
LOAD R1, 0
ADD R1, R2       ; R1 = R2
; max(R1, R3) → R1
CMP R1, R3
JGT 11           ; R1 > R3? skip copy
LOAD R1, 0
ADD R1, R3       ; R1 = R3
STORE R1, 0x00
HALT
