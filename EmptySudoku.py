#A simple Sudoku Solver built using Python and Z3, that can take input of various puzzles 
#and solve them using predicate logic

for i in range(1, 5):
    for j in range(1, 5):
        for n in range(1, 5):
            print("(declare-const P_" + str(i) + "_" + str(j) + "_" + str(n) + " Bool)")
            
print('(assert P_1_3_1)')
print('(assert P_2_1_4)')
print('(assert P_3_4_2)')
print('(assert P_4_2_3)')

for i in range(1, 5):
    for n in range(1, 5):
        row = "(assert (or"
        for j in range(1, 5):
            row += " " + "P_" + str(i) + "_" +str(j) + "_" + str(n)
            
        row += "))"
        print(row)
        
for j in range(1, 5):
    for n in range(1, 5):
        column = "(assert (or"
        for i in range(1, 5):
            column += " " + "P_" + str(i) + "_" +str(j) + "_" + str(n)
            
        column += "))"
        print(column)
        
for r in range(0, 2):
    for c in range(0, 2):
        for n in range(1, 5):
            block = "(assert (or"
            for i in range(1, 3):
                for j in range(1, 3):
                    block += " " + "P_" + str(2*r+i) + "_" + str(2*c+j) + "_" + str(n)
            block += "))"
            print(block)
            
for i in range(1, 5):
    for j in range(1, 5):
        for n in range(1, 5):
            cell = "(assert (or (not " + "P_" + str(i) + "_" + str(j) +"_" + str(n) +  ") (not (or"
            for n1 in range(1, 5):
                if n == n1:
                    continue
                cell += " " + "P_" + str(i) + "_" + str(j) +"_" + str(n1)
            cell += "))))"
            print(cell)
            
            
print("(check-sat)")
print("(get-model)")
user = input()
