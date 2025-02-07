def fizzbuzz(num):
    if num%3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        return "fizzbuzz"
    elif num%3 == 0:
        print("fizz")
        return "fizz"
    elif num % 5 == 0:
        print("buzz")
        return "buzz"
    else:
        print(str(num))
        return str(num)

if __name__ == '__main__':
    for i in range(1, 101):
       fizzbuzz(i)