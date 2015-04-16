

for i in range(0,10):
    if i == 5:
        continue

    elif i == 6:
        continue

    print i, "is not equal to 5 or 6"

    option = raw_input("press a 0 to exclude:\n")

    if option == '0':
        print "excluded\n"
        continue

    else:
        print "included\n"