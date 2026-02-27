"""Tiny 8-bit CPU Emulator."""


class CPU:
    def __init__(self):
        self.registers = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
        self.pc = 0
        self.halted = False
        self.program = []
        self.memory = bytearray(256)
        self.flags = {"zero": False, "negative": False}

    def load_program(self, instructions):
        self.program = instructions
        self.pc = 0
        self.halted = False

    def _resolve(self, value):
        """Resolve a value: if it's a register name, return register contents; otherwise return the int."""
        if isinstance(value, str) and value in self.registers:
            return self.registers[value]
        return value

    def step(self):
        if self.halted or self.pc >= len(self.program):
            return False

        instruction = self.program[self.pc]
        op = instruction[0]
        jumped = False

        if op == "LOAD":
            reg, value = instruction[1], instruction[2]
            self.registers[reg] = value

        elif op == "STORE":
            reg, addr = instruction[1], instruction[2]
            self.memory[addr] = self.registers[reg] & 0xFF

        elif op == "ADD":
            dest, src = instruction[1], instruction[2]
            self.registers[dest] += self._resolve(src)

        elif op == "SUB":
            dest, src = instruction[1], instruction[2]
            self.registers[dest] -= self._resolve(src)

        elif op == "CMP":
            a_val = self._resolve(instruction[1])
            b_val = self._resolve(instruction[2])
            self.flags["zero"] = (a_val == b_val)
            self.flags["negative"] = (a_val < b_val)

        elif op == "JMP":
            self.pc = instruction[1]
            jumped = True

        elif op == "JLE":
            if self.flags["zero"] or self.flags["negative"]:
                self.pc = instruction[1]
                jumped = True

        elif op == "JGE":
            if self.flags["zero"] or not self.flags["negative"]:
                self.pc = instruction[1]
                jumped = True

        elif op == "JL":
            if self.flags["negative"]:
                self.pc = instruction[1]
                jumped = True

        elif op == "JG":
            if not self.flags["zero"] and not self.flags["negative"]:
                self.pc = instruction[1]
                jumped = True

        elif op == "HALT":
            self.halted = True
            return False

        if not jumped:
            self.pc += 1
        return True

    def run(self, max_steps=100000):
        steps = 0
        while self.step():
            steps += 1
            if steps >= max_steps:
                raise RuntimeError(f"CPU exceeded {max_steps} steps — possible infinite loop")

    def dump_registers(self):
        print("Registers:")
        for reg, val in self.registers.items():
            print(f"  {reg} = {val}")

    def dump_memory(self, start=0, end=32):
        print(f"Memory[0x{start:02X}..0x{end - 1:02X}]:")
        for addr in range(start, end):
            if addr % 16 == 0:
                print(f"  0x{addr:02X}: ", end="")
            print(f"{self.memory[addr]:02X} ", end="")
            if addr % 16 == 15 or addr == end - 1:
                print()
