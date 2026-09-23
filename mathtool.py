import sys
import math
MaxVal = 10000

def show_help():
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("  python mathtool.py                          — вывод справки")
    print("  python mathtool.py --help                   — вывод справки")
    print("  python mathtool.py solve                    — ввод коэффициентов с клавиатуры")
    print("  python mathtool.py solve -a 1 -b -3 -c 2    — решение с заданными коэффициентами")
    print()
    print("Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000.")

def keyboard_reader():
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    except ValueError:
        print("ОШИБКА: коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
    return a, b, c

def read_from_args(args):
    if args[0] != "-a" or args[2] != "-b" or args[4] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    try:
        a = int(args[1])
        b = int(args[3])
        c = int(args[5])
    except ValueError:
        print("ОШИБКА: коэффициент не является числом", file=sys.stderr)
        sys.exit(1)
    return a, b, c

def solve(a, b, c):
    if abs(a) > MaxVal or abs(b) > MaxVal or abs(c) > MaxVal:
        print("ОШИБКА: значение слишком большое или слишком маленькое", file=sys.stderr)
        sys.exit(1)
    if a == 0 and b == 0:
        print("ОШИБКА: это не уравнение", file=sys.stderr)
        sys.exit(1)
    if a == 0:
        print("Уравнение линейное")
        x = -c / b
        print(f"x = {x:.3f}")
        return
    print("Уравнение квадратное")
    D = b * b - 4 * a * c
    print(f"D = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")

args = sys.argv[1:]
if len(args) == 0 or args[0] == "--help":
    show_help()
    sys.exit(0)
if args[0] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)
if len(args) == 1:
    a, b, c = keyboard_reader()
elif len(args) == 7:
    a, b, c = read_from_args(args[1:])
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)
solve(a, b, c)
sys.exit(0)