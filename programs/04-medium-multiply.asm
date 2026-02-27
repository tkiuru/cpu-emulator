; Program 04: Multiply 3 × 4 (result: 12)
LOAD R1, 3       ; multiplicand
LOAD R2, 4       ; multiplier (counter)
LOAD R3, 0       ; accumulator (result)
ADD R3, R1       ; result += multiplicand
SUB R2, 1        ; counter--
CMP R2, 0
JNE 3            ; loop back to ADD
STORE R3, 0x00
HALT
