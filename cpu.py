"""Tiny 8-bit CPU Emulator."""


class CPU:
    def __init__(self):
        self.registers = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
        self.memory = [0] * 256
        self.pc = 0
        self.halted = False
        self.program = []

    def load_program(self, instructions):
        self.program = instructions
        self.pc = 0
        self.halted = False

    def step(self):
        if self.halted or self.pc >= len(self.program):
            return False

        instruction = self.program[self.pc]
        op = instruction[0]

        if op == "LOAD":
            reg, value = instruction[1], instruction[2]
            self.registers[reg] = value

        elif op == "ADD":
            dest, src = instruction[1], instruction[2]
            if isinstance(src, int):
                self.registers[dest] = self.registers[dest] + src
            else:
                self.registers[dest] = self.registers[dest] + self.registers[src]

        elif op == "STORE":
            reg, addr = instruction[1], instruction[2]
            self.memory[addr] = self.registers[reg]

        elif op == "HALT":
            self.halted = True
            return False

        self.pc += 1
        return True

    def run(self):
        while self.step():
            pass


# Program 01: add 5 + 8
if __name__ == "__main__":
    cpu = CPU()
    cpu.load_program([
        ("LOAD", "R1", 5),
        ("LOAD", "R2", 8),
        ("ADD", "R1", "R2"),
        ("HALT",),
    ])
    cpu.run()
    print("Registers:", cpu.registers)
