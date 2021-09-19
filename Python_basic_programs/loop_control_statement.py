# Loop control statement: Loop control statements change the execution from the normal sequence.

# ----------------- Continue statement ---------------------
# continue statement is used to skip the rest of the code for the current iteration only. Loop does not terminate
# but continues with the next iteration.

for letter in "Bandhan Singh":
    if letter == 'n':     # if letter == a then it will skip rest of the code and continue with the next iteration
        continue
    print(letter)
print("\n")
# ----------------- Break statement ------------------------
# break statement is used to terminate the loop containing it. Control of the program flows to the statement immediately after the loop

for letter in "Bandhan":
    if letter == 'd':
        break
    print(letter)
