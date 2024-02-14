import pyjokes

def listen():
    tell_some_jokes()

def tell_some_jokes():
    return talkback((pyjokes.get_joke()))

def talkback(jokes):
    print(jokes)
    inp = int(input("1 : To Hear More.\n0 : To Exit.\n"))
    if inp == 1:
        listen()
    else:
        return 0

listen()