; Program 03: Sum numbers 1 to 5 (result: 15)
LOAD R1, 0       ; accumulator (sum)
LOAD R2, 5       ; counter
ADD R1, R2       ; sum += counter
SUB R2, 1        ; counter--
CMP R2, 0
JNE 2            ; loop back to ADD
STORE R1, 0x00
HALT
