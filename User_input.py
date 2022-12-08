message = ""
while True:
    message = input("Your message, please: ")
    if message == '0123':
        break
    else:
        print("Try again, please")
print("Good: " + message)
