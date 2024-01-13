message = input(">")
words = message.split(" ")
emojis = {
    ":)": "🙂",
    ":D": "😀",
    "XD": "😂",
    "^_^": "😊",
    "8)": "😎",
    ":(": "☹️",
    ":/": "😕",
    ":P": "😛",
    ":o": "😮",
    "T-T": "😭",
    ":'(": "😢",
}

output = ""
for every_word in words:
    output += emojis.get(every_word, every_word) + " "
print(output)