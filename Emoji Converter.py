message = input("> ")
words = message.split(" ")
emojis = {
    ":)" : "☺️",
    ":(" : "😔"
}
output = ""
for x in words:
    output += emojis.get(x, x) + " "
print(output)

