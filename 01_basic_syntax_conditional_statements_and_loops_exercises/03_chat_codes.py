n = int(input())

for _ in range(n):
    msg = int(input())

    if msg == 88:
        print("Hello")
    elif msg == 86:
        print("How are you?")
    elif msg < 88:
        print("GREAT!")
    elif msg > 88:
        print("Bye.")