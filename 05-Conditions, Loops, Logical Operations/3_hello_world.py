for num in range(101):
    if not (num % 3 or num % 5):
        print("Hello world", num)
    elif not num % 3:
        print("Hello", num)
    elif not num % 5:
        print("world", num)
