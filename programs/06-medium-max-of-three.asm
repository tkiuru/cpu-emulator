; 06-medium-max-of-three.asm
; Difficulty: Medium
; Description: Find maximum of three values (17, 42, 8)
; Expected: Memory[0x10] = 42

LOAD R1, 17      ; value A
LOAD R2, 42      ; value B
LOAD R3, 8       ; value C
LOAD R4, 0       ; max result

; max = A
ADD R4, R1

; if B > max, max = B
CMP R2, R4
JLE SKIP_B
LOAD R4, 0
ADD R4, R2

SKIP_B:
; if C > max, max = C
CMP R3, R4
JLE DONE
LOAD R4, 0
ADD R4, R3

DONE:
STORE R4, 0x10
HALT
