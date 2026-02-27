; Program 08: Reverse array [5, 3, 8, 1, 4] in place
; Store array at 0x10..0x14
LOAD R1, 5
STORE R1, 0x10
LOAD R1, 3
STORE R1, 0x11
LOAD R1, 8
STORE R1, 0x12
LOAD R1, 1
STORE R1, 0x13
LOAD R1, 4
STORE R1, 0x14
; Set up pointers
LOAD R1, 0x10    ; front pointer
LOAD R2, 0x14    ; back pointer
; Swap loop
LOAD R3, [R1]    ; R3 = array[front]
LOAD R4, [R2]    ; R4 = array[back]
STORE R4, [R1]   ; array[front] = R4
STORE R3, [R2]   ; array[back] = R3
ADD R1, 1        ; front++
SUB R2, 1        ; back--
CMP R2, R1       ; back > front?
JGT 12           ; if so, keep swapping
HALT
