import sys


def isFloat(string):
    try:
        float(string)
        return True
    except:
        return False


def check(exp):
    if len(exp) == 0:
        return True
    return False


def get_pol_degree(buff):
    max = 0
    if buff['X^2'] == 0 and buff['X^1'] == 0 and len(buff) == 3:
        return 0
    if buff['X^2'] == 0 and len(buff) == 3:
        return 1
    try:
        for key, val in buff.items():
            if int(key[2]) > max:
                max = int(key[2])
    except:
        print('Powers are incorrect')
        sys.exit()
    return max


def sqrt(disc):
    start = disc
    for i in range(10):
        start = (start + (disc / start)) / 2
    return start


def get_discriminant(buff):
    disc = buff['X^1'] ** 2 - 4 * buff['X^0'] * buff['X^2']
    if disc == 0:
        print("Discriminant = 0, the solution is:")
        print((buff['X^1'] * -1) / (2 * buff['X^2']))
    elif disc < 0:
        print("Discriminant is negative, the two complex solutions are:")
        print(str((buff['X^1'] * -1) / (2 * buff['X^2'])) + " + i" + str(sqrt(disc * -1) / (2 * buff['X^2'])))
        print(str((buff['X^1'] * -1) / (2 * buff['X^2'])) + " - i" + str(sqrt(disc * -1) / (2 * buff['X^2'])))
    else:
        print("Discriminant is strictly positive, the two solutions are:")
        print(((buff['X^1'] * -1) + sqrt(disc)) / (2 * buff['X^2']))
        print(((buff['X^1'] * -1) - sqrt(disc)) / (2 * buff['X^2']))


def is_solve(buff):
    if buff['X^2'] == 0 and buff['X^1'] == 0 and len(buff) == 3:
        print('There are no solutions')
        sys.exit()


def all_to_one(left, right):
    buff = {'X^0': 0, 'X^1': 0, 'X^2': 0}
    left = left.split()
    right = right.split()
    for i in range(len(left)):
        if isFloat(left[i]):
            if not len(left) < (i + 2) and left[i + 1] == "*":
                if not left[i + 2] in buff and (i == 0 or left[i - 1] == '+'):
                    buff[left[i + 2]] = float(left[i])
                elif not left[i + 2] in buff:
                    buff[left[i + 2]] = float(left[i]) * (-1)
                elif i == 0:
                    buff[left[i + 2]] += float(left[i])
                elif left[i - 1] == '+':
                    buff[left[i + 2]] += float(left[i])
                else:
                    buff[left[i + 2]] -= float(left[i])
    for i in range(len(right)):
        if isFloat(right[i]):
            if not len(right) < (i + 2) and right[i + 1] == "*":
                if not right[i + 2] in buff and (i == 0 or right[i - 1] == '+'):
                    buff[right[i + 2]] = float(right[i]) * (-1)
                elif not right[i + 2] in buff:
                    buff[right[i + 2]] = float(right[i])
                elif i == 0:
                    buff[right[i + 2]] -= float(right[i])
                elif right[i - 1] == '+':
                    buff[right[i + 2]] -= float(right[i])
                else:
                    buff[right[i + 2]] += float(right[i])
    print('Reduced form: ', end="")
    for key, val in buff.items():
        if key == "X^0" and val < 0:
            print('- ' + str(val * -1) + ' * ' + str(key), end=" ")
        elif key == "X^0":
            print(str(val) + ' * ' + str(key), end = " ")
        elif val < 0:
            print('- ' + str(val * -1) + ' * ' + str(key), end = " ")
        else:
            print('+ ' + str(val) + ' * ' + str(key), end=" ")
    print("= 0")
    if buff['X^2'] == 0 and buff['X^1'] == 0 and buff['X^0'] == 0 and len(buff) == 3:
        print('All the real numbers are solution')
        sys.exit()
    is_solve(buff)
    print('Polynomial degree:', get_pol_degree(buff))
    if get_pol_degree(buff) > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit()
    if get_pol_degree(buff) == 2 and not buff['X^2'] == 0:
        get_discriminant(buff)
    if get_pol_degree(buff) == 1:
        print('The solution is:')
        print(buff['X^0'] / (buff['X^1'] * -1))


def solve(exp):
    left = exp[0]
    right = exp[1]
    if check(left):
        print('Incorrect left part')
        sys.exit()
    if check(right):
        print('Incorrect right part')
        sys.exit()
    all_to_one(left, right)


def pow_sps(exp):
    buff = []
    try:
        exp = exp.split()
        for i in range(len(exp)):
            if exp[i] == "X" and exp[i + 1] == "^" and exp[i + 2].isnumeric():
                exp[i] = "X^" + str(exp[i + 2])
                exp[i + 2] = "Z"
        for i in range(len(exp)):
            if not exp[i] == "^" or not exp[i] == "Z":
                buff.append(exp[i])
    except:
        print('Powers are incorrect.')
        sys.exit()
    return " ".join(buff)


def get_line(line):
    exp = line
    exp = " ".join(exp.split(" "))
    exp = pow_sps(exp)
    exp = exp.split("=")
    if len(exp) == 2:
        solve(exp)
    elif len(exp) == 1:
        print('There must be at least one sign "=".')
        sys.exit()
    else:
        print('There must be only one sign "=".')
        sys.exit()


def main():
    if len(sys.argv) == 2:
        get_line(sys.argv[1])
    else:
        print("The program should receive one argument.")


if __name__ == '__main__':
    main()
