; Program 05: Fibonacci - compute fib(8) = 21
LOAD R1, 0       ; a = fib(0)
LOAD R2, 1       ; b = fib(1)
LOAD R3, 8       ; counter
LOAD R4, 0       ; temp = 0
ADD R4, R2       ; temp = b
ADD R2, R1       ; b = a + b
LOAD R1, 0       ; a = 0
ADD R1, R4       ; a = old b
SUB R3, 1        ; counter--
CMP R3, 0
JNE 3            ; loop back to LOAD R4
STORE R1, 0x00
HALT
