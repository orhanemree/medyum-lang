ops_count = 0
def op():
    global ops_count
    temp = ops_count
    ops_count += 1
    return temp

PRINT = op()
PLUS = op()
MINUS = op()
TIMES = op()
DIVIDE = op()
MOD = op()
EQUAL = op()
SWAP = op()
COPY = op()
DROP = op()
IF = op()
ELSE = op()
END = op()
PUSH = op()