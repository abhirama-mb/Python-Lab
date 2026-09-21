string = input("Enter a string containing a's and b's: ")

state = "q0"

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
        if ch == 'a':
            state = "q1"
        elif ch == 'b':
            state = "q2"
        else:
            state = "invalid"
            break

    elif state == "q2":
        if ch == 'a':
            state = "q1"
        elif ch == 'b':
            state = "q3"
        else:
            state = "invalid"
            break

    elif state == "q3":
        if ch == 'a':
            state = "q1"
        elif ch == 'b':
            state = "q0"
        else:
            state = "invalid"
            break

if state == "q3":
    print("accepted")
else:
    print("rejected")