"""Tiny 8-bit CPU Emulator."""


class CPU:
    def __init__(self):
        self.registers = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
        self.memory = [0] * 256
        self.pc = 0
        self.halted = False
        self.program = []
        self.flags = {"equal": False, "greater": False}

    def load_program(self, instructions):
        self.program = instructions
        self.pc = 0
        self.halted = False
        self.flags = {"equal": False, "greater": False}

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

        elif op == "SUB":
            dest, src = instruction[1], instruction[2]
            if isinstance(src, int):
                self.registers[dest] = self.registers[dest] - src
            else:
                self.registers[dest] = self.registers[dest] - self.registers[src]

        elif op == "CMP":
            reg, val = instruction[1], instruction[2]
            left = self.registers[reg]
            right = val if isinstance(val, int) else self.registers[val]
            self.flags["equal"] = left == right
            self.flags["greater"] = left > right

        elif op == "JNE":
            addr = instruction[1]
            if not self.flags["equal"]:
                self.pc = addr
                return True

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
