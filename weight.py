import os

for root, dirs, files in os.walk("."):
    for f in files:
        if ".c" in f:
            path = root + '/' + f
            with open(path, 'r') as file:
                text = file.read()
                incomment = False
                wc = [0, 0]
                for i in range(len(text)-1):
                    if text[i] == '/' and text[i+1] == '*':
                        incomment = True
                    elif text[i] == '*' and text[i+1] == '/':
                        incomment = False

                    if incomment:
                        wc[1] += 1
                    else:
                        wc[0] += 1
                print(f'{path}, {wc[0]}, {wc[1]}')
