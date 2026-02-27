"""Tiny 8-bit CPU Emulator."""

JUMP_CONDITIONS = {
    "JNE": lambda f: not f["equal"],
    "JGT": lambda f: f["greater"],
    "JG":  lambda f: f["greater"],
    "JGE": lambda f: f["greater"] or f["equal"],
    "JLE": lambda f: not f["greater"],
    "JL":  lambda f: not f["greater"] and not f["equal"],
    "JMP": lambda f: True,
}


class CPU:
    def __init__(self):
        self.registers = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
        self.memory = [0] * 256
        self.pc = 0
        self.halted = False
        self.program = []
        self.flags = {"equal": False, "greater": False}
        self.sp = 0xFF

    def load_program(self, program):
        if isinstance(program, dict):
            self.program = program["instructions"]
            for addr, val in program.get("data", {}).items():
                self.memory[addr] = val
        else:
            self.program = program
        self.pc = 0
        self.halted = False
        self.flags = {"equal": False, "greater": False}
        self.sp = 0xFF

    def step(self):
        if self.halted or self.pc >= len(self.program):
            return False

        instruction = self.program[self.pc]
        op = instruction[0]

        if op == "LOAD":
            reg, src = instruction[1], instruction[2]
            if isinstance(src, str) and src.startswith("["):
                addr_reg = src[1:-1]
                self.registers[reg] = self.memory[self.registers[addr_reg]]
            else:
                self.registers[reg] = src

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

        elif op in JUMP_CONDITIONS:
            if JUMP_CONDITIONS[op](self.flags):
                self.pc = instruction[1]
                return True

        elif op == "CALL":
            self.memory[self.sp] = self.pc + 1
            self.sp -= 1
            self.pc = instruction[1]
            return True

        elif op == "RET":
            self.sp += 1
            self.pc = self.memory[self.sp]
            return True

        elif op == "STORE":
            reg, dest = instruction[1], instruction[2]
            if isinstance(dest, str) and dest.startswith("["):
                addr_reg = dest[1:-1]
                self.memory[self.registers[addr_reg]] = self.registers[reg]
            else:
                self.memory[dest] = self.registers[reg]

        elif op == "HALT":
            self.halted = True
            return False

        self.pc += 1
        return True

    def run(self):
        while self.step():
            pass
