EXPRESSION = {
    "+": lambda x, y : x+y,
    "-": lambda x, y : x-y,
    "*": lambda x, y : x*y,
    "/": lambda x, y : x/y
}

def calc(num1, operator, num2):
    return EXPRESSION[operator](int(num1), int(num2))

def main():
    try:
        result = calc(*input().split(" "))
        print(result)
    except:
        print("수식을 잘못 입력하셨습니다.")

main()