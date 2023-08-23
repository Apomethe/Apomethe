def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = int(input("Nhập một số nguyên dương: "))
    result = factorial(num)
    print(f"Giai thừa của {num} là {result}")

if __name__ == "__main__":
    main()
