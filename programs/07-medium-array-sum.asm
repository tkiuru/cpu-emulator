; Program 07: Sum an array of 5 numbers (result: 150)
; Store array [10, 20, 30, 40, 50] at addresses 0x10..0x14
LOAD R1, 10
STORE R1, 0x10
LOAD R1, 20
STORE R1, 0x11
LOAD R1, 30
STORE R1, 0x12
LOAD R1, 40
STORE R1, 0x13
LOAD R1, 50
STORE R1, 0x14
; Sum the array
LOAD R1, 0       ; accumulator
LOAD R2, 0x10    ; pointer
LOAD R3, 5       ; counter
LOAD R4, [R2]    ; load value from memory
ADD R1, R4       ; sum += value
ADD R2, 1        ; pointer++
SUB R3, 1        ; counter--
CMP R3, 0
JNE 13           ; loop back to LOAD R4, [R2]
STORE R1, 0x00   ; store result
HALT
