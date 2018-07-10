def validate(password):
    condition = [0, 0, 0, 0, 1]  # for testing all the four criterias
    for i in password:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):  # checking for capital alphabet
            condition[0] = 1
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):  # charcking for small alphabet
            condition[1] = 1
        elif i.isdigit():  # checking for digit
            condition[2] = 1
        elif i == '$' or i == '#' or i == '@':  # checking for special symbols
            condition[3] = 1
        else:  # if character other then the mentioned conditionsL
            condition[4] = 1
    # print(condition)
    if 0 in condition:
        print("not valid")
    else:
        if len(password) >= 6 and len(password) <= 12:
            print("valid")
        else:
            print("Password too long!!")

    return


def main():
    s = raw_input("Enter password: ")
    validate(s)


if __name__ == '__main__':
    main()
