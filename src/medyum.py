#!/usr/bin/env python

from ops import *
import sys

def lex_program(program):
    program = program.split()
    block_stack = []

    for ip in range(len(program)):
        op = program[ip]

        if op == "yaz":
            program[ip] = (PRINT, )

        elif op == "+":
            program[ip] = (PLUS, )

        elif op == "-":
            program[ip] = (MINUS, )

        elif op == "*":
            program[ip] = (TIMES, )

        elif op == "/":
            program[ip] = (DIVIDE, )

        elif op == "%":
            program[ip] = (MOD, )

        elif op == "==":
            program[ip] = (EQUAL, )

        elif op == "takasla":
            program[ip] = (SWAP, )

        elif op == "kopyala":
            program[ip] = (COPY, )

        elif op == "düşür":
            program[ip] = (DROP, )

        elif op == "ise":
            block_stack.append((IF, ip))
            program[ip] = (IF, )

        elif op == "değilse":
            if_addr = block_stack.pop()
            if if_addr[0] == IF:
                program[if_addr[1]] = (IF, ip)
            else:
                assert False, "unreachable"
            block_stack.append((ELSE, ip))
            program[ip] = (ELSE, )

        elif op == "son":
            if_or_else_addr = block_stack.pop()
            if if_or_else_addr[0] == IF:
                program[if_or_else_addr[1]] = (IF, ip)
            elif if_or_else_addr[0] == ELSE:
                program[if_or_else_addr[1]] = (ELSE, ip)
            else:
                assert False, "unreachable"
            program[ip] = (END, )

        else:
            program[ip] = (PUSH, op)

    return program

def run_program_from_file(file_path):
    with open(file_path) as f:
        program =  lex_program(f.read())
        stack = []
        ip = 0

        while ip < len(program):
            op = program[ip]

            if op[0] == PRINT:
                a = stack.pop()
                print(a)
                ip += 1

            elif op[0] == PLUS:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
                ip += 1

            elif op[0] == MINUS:
                a = stack.pop()
                b = stack.pop()
                stack.append(a - b)
                ip += 1

            elif op[0] == TIMES:
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
                ip += 1

            elif op[0] == DIVIDE:
                a = stack.pop()
                b = stack.pop()
                stack.append(a // b)
                ip += 1

            elif op[0] == MOD:
                a = stack.pop()
                b = stack.pop()
                stack.append(a % b)
                ip += 1

            elif op[0] == EQUAL:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a == b))
                ip += 1

            elif op[0] == SWAP:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
                ip += 1

            elif op[0] == COPY:
                a = stack.pop()
                stack.append(a)
                stack.append(a)
                ip += 1

            elif op[0] == DROP:
                a = stack.pop()
                ip += 1

            elif op[0] == IF:
                a = stack.pop()
                if a:
                    ip += 1
                else:
                    ip = op[1] + 1

            elif op[0] == ELSE:
                ip = op[1]

            elif op[0] == END:
                ip += 1

            elif op[0] == PUSH:
                stack.append(int(op[1]))
                ip += 1

            else:
                print(json.dumps(op))
                assert False, "unreachable"


if __name__ == "__main__":
    filename = sys.argv[1]
    run_program_from_file(filename)