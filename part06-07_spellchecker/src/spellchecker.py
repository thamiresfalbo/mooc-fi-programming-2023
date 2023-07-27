# write your solution here
user_text = input("Write text:")
user_list = user_text.split(" ")

wordlist = []
with open("wordlist.txt") as wordlist_file:
    for line in wordlist_file:
        wordlist.append(line.strip())

final = []
for i in user_list:
    if i.lower() not in wordlist:
        final.append(f"*{i}*")
    else:
        final.append(i)

print(" ".join(final))
