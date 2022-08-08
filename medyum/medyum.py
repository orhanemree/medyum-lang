from .ops import *
import sys

def is_int(string):
    if string[0] in ('-', '+'):
        return ststringr[1:].isdigit()
    return string.isdigit()

def lex_program(program):
    program = list(map(lambda x: x.split("//")[0], program)) # ignore comments
    program = list(map(lambda x: x.split(), program)) # slice to words
    program = list(filter(lambda x: x != [], program)) # ignore empty rows
    program = [item for sublist in program for item in sublist] # convert nested array to flat array
    block_stack = []

    for ip in range(len(program)):
        op = program[ip]

        # print
        if op == "yanyaz":
            program[ip] = (PRINT, )
            
        elif op == "yaz":
            program[ip] = (PRINTLN, )

        # input
        elif op == "oku":
            program[ip] = (INPUT, )

        # math
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
            
        # logic
        elif op == "==":
            program[ip] = (EQUAL, )

        elif op == "!=":
            program[ip] = (NOT_EQUAL, )

        elif op == ">":
            program[ip] = (GREATER, )

        elif op == "<":
            program[ip] = (LESS, )

        elif op == ">=":
            program[ip] = (GREATER_OR_EQUAL, )

        elif op == "<=":
            program[ip] = (LESS_OR_EQUAL, )

        elif op == "&&":
            program[ip] = (AND, )

        elif op == "||":
            program[ip] = (OR, )
            
        # variables
        elif op == "=":
            program[ip] = (SET, )

        elif op == "?":
            program[ip] = (GET, )

        # methods
        elif op == "takasla":
            program[ip] = (SWAP, )

        elif op == "kopyala":
            program[ip] = (COPY, )

        elif op == "düşür":
            program[ip] = (DROP, )

        # exit
        elif op == "çık":
            program[ip] = (EXIT, )

        # conditions
        elif op == "ise":
            block_stack.append((IF, ip))
            program[ip] = (IF, )

        elif op == "değilse":
            if_addr = block_stack.pop()
            if if_addr[0] == IF:
                program[if_addr[1]] = (IF, ip)
            else:
                assert False, "`değilse` yalnızca `ise` ifadesinden sonra kullanılabilir."
            block_stack.append((ELSE, ip))
            program[ip] = (ELSE, )

        elif op == "eşleştir":
            block_stack.append((SWITCH, ip))
            program[ip] = (SWITCH, )

        elif op == "ile":
            block_stack.append((CASE, ip))
            program[ip] = (CASE, )

        # loops
        elif op == "iken":
            block_stack.append((WHILE, ip))
            program[ip] = (WHILE, )

        elif op == "yap":
            block_stack.append((DO, ip))
            program[ip] = (DO, )

        # end
        elif op == "bitir":
            last_block = block_stack.pop()
            if last_block[0] == IF:
                program[last_block[1]] = (IF, ip)
                program[ip] = (END, ip + 1)
            elif last_block[0] == ELSE:
                program[last_block[1]] = (ELSE, ip)
                program[ip] = (END, ip + 1)
            elif last_block[0] == DO:
                program[last_block[1]] = (DO, ip)
                while_addr = block_stack.pop()
                program[ip] = (END, while_addr[1])
            elif last_block[0] == SWITCH:
                program[last_block[1]] = (SWITCH, )
                program[ip] = (DROP, )
            elif last_block[0] == CASE:
                program[last_block[1]] = (CASE, ip)
                program[ip] = (END, ip + 1)
            else:
                assert False, "`bitir` yalnızca `ise, değilse, eşleştir, ile, yap` ifadelerinden sonra kullanılabilir."

        # push
        elif is_int(op):
            program[ip] = (PUSH, op)

        # (push variable)
        else:
            program[ip] = (VAR, op)

    return program

def run_program(program):
    stack = []
    memory = {}

    ip = 0
    while ip < len(program):
        op = program[ip]

        # push
        if op[0] == PUSH:
            stack.append(int(op[1]))
            ip += 1

        # print
        elif op[0] == PRINT:
            a = stack.pop()
            print(int(a), end=" ")
            ip += 1

        elif op[0] == PRINTLN:
            a = stack.pop()
            print(int(a))
            ip += 1

        # input
        elif op[0] == INPUT:
            a = input("> ")
            stack.append(int(a))
            ip += 1 

        # math
        elif op[0] == PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
            ip += 1

        elif op[0] == MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
            ip += 1

        elif op[0] == TIMES:
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
            ip += 1

        elif op[0] == DIVIDE:
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
            ip += 1

        elif op[0] == MOD:
            a = stack.pop()
            b = stack.pop()
            stack.append(b % a)
            ip += 1

        # logic
        elif op[0] == EQUAL:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b == a))
            ip += 1

        elif op[0] == NOT_EQUAL:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b != a))
            ip += 1

        elif op[0] == GREATER:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b > a))
            ip += 1

        elif op[0] == LESS:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b < a))
            ip += 1

        elif op[0] == GREATER_OR_EQUAL:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b >= a))
            ip += 1

        elif op[0] == LESS_OR_EQUAL:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b <= a))
            ip += 1

        elif op[0] == AND:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(bool(b) and bool(a)))
            ip += 1
            
        elif op[0] == OR:
            a = stack.pop()
            b = stack.pop()
            stack.append(int(bool(b) or bool(a)))
            ip += 1

        # variables
        elif op[0] == VAR:
            stack.append(op)
            ip += 1

        elif op[0] == SET:
            a = stack.pop()
            b = stack.pop()
            memory[a[1]] = int(b)
            ip += 1

        elif op[0] == GET:
            a = stack.pop()
            stack.append(memory[a[1]])
            ip += 1

        # methods
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

        # exit
        elif op[0] == EXIT:
            a = stack.pop()
            exit(not bool(a)) # should we remove "not" little bit confused here
            ip += 1 # necessary ?

        # conditions
        elif op[0] == IF:
            a = stack.pop()
            if a:
                ip += 1
            else:
                ip = op[1] + 1

        elif op[0] == ELSE:
            ip = op[1]

        elif op[0] == SWITCH:
            ip += 1

        elif op[0] == CASE:
            a = stack.pop()
            b = stack.pop()
            stack.append(b)
            if a == b:
                ip += 1
            else:
                ip = op[1] + 1

        # loops
        elif op[0] == WHILE:
            ip += 1

        elif op[0] == DO:
            a = stack.pop()
            if a:
                ip += 1
            else:
                ip = op[1] + 1

        # end
        elif op[0] == END:
            ip = op[1]

        else:
            assert False, "unreachable"

def main(file_path):
    with open(file_path) as f:
        program = lex_program(f.readlines())
        run_program(program)

        print()

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)