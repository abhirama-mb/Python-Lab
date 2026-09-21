string = input("enter a string containing a's and b's : ")
state = "q0"

print("\nstate transitions\n")

for ch in string:
    if state == "q0":
        if ch == 'a':
            state = "q1"
        else:
            state = "invalid"
            break

    elif state == "q1" or state == "q2":
        if ch == 'a':
            state = "q1"
        elif ch == 'b':
            state = "q2"
        else:
            state = "invalid"
            break

                        

if state == "q2":
    print("accepted")
else:
    print("rejected")