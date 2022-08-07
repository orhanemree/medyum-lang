ops_count = 0
def op():
    global ops_count
    temp = ops_count
    ops_count += 1
    return temp

# push
PUSH = op()

# print
PRINT = op() # yaz

# math
PLUS = op() # +
MINUS = op() # -
TIMES = op() # *
DIVIDE = op() # /
MOD = op() # %

# logic
EQUAL = op() # ==
NOT_EQUAL = op() # !=
GREATER = op() # >
LESS = op() # <
GREATER_OR_EQUAL = op() # >=
LESS_OR_EQUAL = op() # <=
AND = op() # &&
OR = op() # ||

# variables
VAR = op()
SET = op() # =
GET = op() # ?

# methods
SWAP = op() # takasla
COPY = op() # kopyala
DROP = op() # düşür

# conditions
IF = op() # ise
ELSE = op() # değilse

# loops
WHILE = op() # iken
DO = op() # yap

# end
END = op() # bitir