string = input("enter a string containing a's and b's : ")
state = "q0"

print("\nstate transitions\n")

for ch in string:
    if state == "q0":
        if ch == 'a':
            state = "q1"
        elif ch == 'b':
            state = "q0"
        else:
            state = "invalid"
            break

    elif state == "q1":
        if ch == 'a' or ch == 'b':
            state = "q1"
        else:
            state = "invalid"
            break

if state == "q1":
    print("accepted")
else:
    print("rejected")