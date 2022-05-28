import random
from tkinter import *
from tkinter import messagebox

codealpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
char_to_morse = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def atbash(txta):
    ciphertxt = str()
    for i in txta:
        if i.isalpha():
            if i.isupper():
                x = codealpha.index(i.lower())
                ciphertxt += codealpha[25-x].upper()
            else:
                x = codealpha.index(i)
                ciphertxt += codealpha[25-x]
        else:
            ciphertxt += i
    return ciphertxt


def caesar(txtb, shift):
    ciphertxt = str()
    for i in txtb:
        if i.isalpha():
            if i.isupper():
                x = codealpha.index(i.lower())
                ciphertxt += codealpha[(x+shift) % 26].upper()
            else:
                x = codealpha.index(i)
                ciphertxt += codealpha[(x+shift) % 26]
        else:
            ciphertxt += i
    return ciphertxt


def numerical(txtc):
    ciphertxt = str()
    for i in txtc:
        if i.isalpha():
            x = str(codealpha.index(i.lower())+1)
            ciphertxt += x
            ciphertxt += " "
        elif i.isspace():
            ciphertxt = ciphertxt[:-1]
            ciphertxt += "."
            ciphertxt += " "
    return ciphertxt[:-1]


def unnumerical(txtd):
    plaintxt = str()
    ciphertxt = txtd.split()
    for i in ciphertxt:
        if i.isnumeric():
            x = codealpha[int(i)-1]
            plaintxt += x
        elif i.endswith("."):
            y = i[:-1]
            x = codealpha[int(y)-1]
            plaintxt += x
            plaintxt += " "
    return plaintxt


def vigenere(txte, keyv):
    ciphertxt = str()
    numkey = []
    for i in keyv:
        x = codealpha.index(i.lower())
        numkey.append(x)
    index = 0
    for i in txte:
        ciphertxt += caesar(i, numkey[index % len(numkey)])
        index += 1
    return ciphertxt


def unvigenere(txtf, keyu):
    return caesar(vigenere(txtf, atbash(keyu)), 1)


def reverse(txtg):
    ciphertxt = str()
    for i in range(len(txtg)):
        ciphertxt += txtg[-(i+1)]
    return ciphertxt


def phonetic(txth):
    nato = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "x-ray", "yankee", "zulu"]
    ciphertxt = str()
    for i in txth:
        if i.isalpha():
            x = codealpha.index(i.lower())
            ciphertxt += nato[x]
            ciphertxt += " "
    return ciphertxt


def anagram(txti):
    ciphertxt = str()
    plaintxt = []
    for i in txti:
        plaintxt.append(i)
    for i in range(len(txti)):
        x = plaintxt[random.randint(0, len(plaintxt)-1)]
        ciphertxt += x
        plaintxt.remove(x)
    return ciphertxt
        

def morse(txtj):
    ciphertxt = str()
    for i in txtj:
        if i.upper() in list(char_to_morse.keys()):
            ciphertxt += char_to_morse[i.upper()]
            ciphertxt += " "
    return ciphertxt[:-1]


def unmorse(txtk):
    plaintxt = str()
    words = txtk.split("   ")
    chars = []
    for i in words:
        x = i.split()
        for y in x:
            if y in list(char_to_morse.values()):
                chars.append(list(char_to_morse.keys())[list(char_to_morse.values()).index(y)])
        chars.append(" ")
    for i in chars:
        plaintxt += i
    return plaintxt[:-1]


def binary(txtl):
    ciphertxt = str()
    for i in txtl:
        x = str(bin(ord(i)))[2:]
        while len(x) < 8:
            x = "0" + x
        ciphertxt += x
        ciphertxt += " "
    return ciphertxt[:-1]


def unbinary(txtm):
    cipher = txtm.split()
    plaintxt = str()
    for i in cipher:
        plaintxt += chr(int(i, 2))
    return plaintxt


def railfence(txtn, row):
    ciphertxt = []
    down = True
    tier = 0
    for i in range(row):
        ciphertxt.append(str())
    row -= 1
    for i in txtn:
        if i.isalpha():
            ciphertxt[tier] += i
            if down:
                tier += 1
            else:
                tier -= 1
            if tier == 0:
                down = True
            elif tier == row:
                down = False
    return "".join(ciphertxt)


def unrailfence(txto, row):
    cycle = 2 * row - 2
    cycount = int(len(txto) / cycle)
    rem = len(txto) % cycle
    plain = []
    tier = 0
    global prog
    prog = 0
    down = True
    for i in range(len(txto)):
        plain.append(str())
    for i in txto:
        if tier == 0:
            plain[prog * cycle] = i
            if rem == 0 and cycount == prog + 1:
                tier += 1
                prog = 0
                down = True
            elif rem != 0 and cycount == prog:
                tier += 1
                prog = 0
                down = True
            else:
                prog += 1
        elif tier == row - 1:
            plain[tier + prog * cycle] = i
            if rem < row and cycount == prog + 1:
                tier += 1
                prog = 0
                down = True
            elif rem >= row and cycount == prog:
                tier += 1
                prog = 0
                down = True
            else:
                prog += 1
        else:
            if down:
                plain[tier + int(prog / 2) * cycle] = i
            else:
                plain[(int(prog / 2) + 1) * cycle - tier] = i
            if tier + 1 > rem and 2 * cycount == prog + 1:
                tier += 1
                prog = 0
                down = True
            elif 0 < rem <= row and tier <= rem - 1 and 2 * cycount == prog:
                tier += 1
                prog = 0
                down = True
            elif rem > row and tier <= cycle - rem and 2 * cycount == prog:
                tier += 1
                prog = 0
                down = True
            elif rem > row and tier > cycle - rem and 2 * cycount == prog - 1:
                tier += 1
                prog = 0
                down = True
            else:
                prog += 1
                down = not down
    return "".join(plain)


prog = Tk()
prog.title("Cryptographical Translator")
prog.iconbitmap("icon.ico")

root = LabelFrame(prog, padx=5, pady=5)
root.pack(padx=10, pady=10, anchor=CENTER)

Label(root, text="Enter text:").grid(row=0, column=0)
txt = Text(root, height=25, width=70)
txt.grid(row=1, column=0)

mid = LabelFrame(root, bd=0)
mid.grid(row=0, column=1, rowspan=2)

Label(root, text="Output text:").grid(row=0, column=2)
right = LabelFrame(root, relief=RIDGE)
right.grid(row=1, column=2)
outtxt = Text(right, height=25, width=70)
outtxt.pack()

drop = StringVar()
drop.set("Choose cipher:")

keylab = Label(mid, text="Key:")
key = Entry(mid)


def keybox(*args):
    if drop.get() == "Caesar" or drop.get() == "Vigenere" or drop.get() == "Rail Fence":
        keylab.grid(row=3, column=0)
        key.grid(row=4, column=0, padx=5)
    else:
        keylab.grid_remove()
        key.grid_remove()


def toggledropdown(val):
    encryptlist = ["Caesar", "Atbash", "Numerical", "Vigenere", "Reverse", "Rail Fence", "Morse", "Binary", "Phonetic", "Anagram"]
    decryptlist = ["Caesar", "Atbash", "Numerical", "Vigenere", "Reverse", "Rail Fence", "Morse", "Binary"]
    if val == 1:
        ciphsel = OptionMenu(mid, drop, *encryptlist, command=keybox)
        ciphsel.grid(row=2, column=0)
    elif val == 2:
        if drop.get() == "Phonetic" or drop.get() == "Anagram":
            drop.set("Caesar")
        ciphsel = OptionMenu(mid, drop, *decryptlist, command=keybox)
        ciphsel.grid(row=2, column=0)


def trans():
    outtxt.delete('1.0', END)
    if not var.get():
        messagebox.showerror("Invalid Request", "Please select whether you'd like to encrypt or decrypt before running translation.")
    elif var.get() == 1:
        if drop.get() == "Caesar":
            outtxt.insert('1.0', caesar(txt.get('1.0', 'end-1c'), int(key.get())))
        elif drop.get() == "Atbash":
            outtxt.insert('1.0', atbash(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Numerical":
            outtxt.insert('1.0', numerical(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Vigenere":
            outtxt.insert('1.0', vigenere(txt.get('1.0', 'end-1c'), key.get()))
        elif drop.get() == "Reverse":
            outtxt.insert('1.0', reverse(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Rail Fence":
            outtxt.insert('1.0', railfence(txt.get('1.0', 'end-1c'), int(key.get())))
        elif drop.get() == "Morse":
            outtxt.insert('1.0', morse(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Binary":
            outtxt.insert('1.0', binary(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Phonetic":
            outtxt.insert('1.0', phonetic(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Anagram":
            outtxt.insert('1.0', anagram(txt.get('1.0', 'end-1c')))
    elif var.get() == 2:
        if drop.get() == "Caesar":
            outtxt.insert('1.0', caesar(txt.get('1.0', 'end-1c'), -int(key.get())))
        elif drop.get() == "Atbash":
            outtxt.insert('1.0', atbash(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Numerical":
            outtxt.insert('1.0', unnumerical(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Vigenere":
            outtxt.insert('1.0', unvigenere(txt.get('1.0', 'end-1c'), key.get()))
        elif drop.get() == "Reverse":
            outtxt.insert('1.0', reverse(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Rail Fence":
            outtxt.insert('1.0', unrailfence(txt.get('1.0', 'end-1c'), int(key.get())))
        elif drop.get() == "Morse":
            outtxt.insert('1.0', unmorse(txt.get('1.0', 'end-1c')))
        elif drop.get() == "Binary":
            outtxt.insert('1.0', unbinary(txt.get('1.0', 'end-1c')))


var = IntVar()
encrypt = Radiobutton(mid, text="Encrypt", variable=var, value=1, command=lambda: toggledropdown(1))
encrypt.grid(row=0, column=0)
decrypt = Radiobutton(mid, text="Decrypt", variable=var, value=2, command=lambda: toggledropdown(2))
decrypt.grid(row=1, column=0)
translate = Button(mid, text="Translate", command=trans)
translate.grid(row=5, column=0, pady=5)

prog.mainloop()
