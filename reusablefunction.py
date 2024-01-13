def emoji_converter(message):
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
    return output


# pag sa terminal lang 'yung nasa baba while taas if GUI and such
message = input("> ")
print(emoji_converter(message))


