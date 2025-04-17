secret_message = input().split()

for i in range(len(secret_message)):
    ascii_secret = ''
    word_secret = ''
    for word in secret_message[i]:
        if word.isnumeric():
            ascii_secret += word
        else:
            word_secret += word
    length = len(word_secret)
    if length > 2:
        word_secret_flip = word_secret[-1] + word_secret[1:length - 1] + word_secret[0]
    elif length == 2:
        word_secret_flip = word_secret[-1] + word_secret[0]
    else:
        word_secret_flip = word_secret
    secret_message[i] = chr(int(ascii_secret)) + word_secret_flip

for word in secret_message:
    print(word, end=' ')