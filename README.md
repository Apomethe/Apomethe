- 👋 Hi, I’m @Apomethe
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Apomethe/Apomethe is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
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

