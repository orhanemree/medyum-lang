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
GREATER = op()
SWAP = op()
COPY = op()
DROP = op()
IF = op()
ELSE = op()
WHILE = op()
DO = op()
END = op()
PUSH = op()