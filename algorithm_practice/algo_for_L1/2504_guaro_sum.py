# () 2
# [] 3  "(()[[]])([])"
def tagging (str):
    answer = 1
    result = 0
    while str:
        a = str.pop()
        if a == "]":
            if answer == 1:
                answer *= 3
            else:
                answer = 1
        elif a == ")":
            if answer == 1:
                answer *= 2
            else:
                answer = 1
        elif a == "[":
            pass
        elif a == "(])":
            pass
        else:
            print("예외?")

    return result

a = "(()[[]])([])"
# a = input()
2(2+3*3)+2*3
