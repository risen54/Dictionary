# Vocab Dictionary

**Description:** I am well enough in English but my vocabulary is poor. There are some words which I come across frequently but always forget the meaning. So I made this program to help me out. If I find an unknown word, I can search for it's definition and then add it to this dictionary and search for it whenever I need it. I know I can simply google it but wanted to flex my coding skills 😜.

## What is what?

### def adder():
Adds a word to the file in this format:
`word : definition`

code:
```py
def adder(word, meaning):
    with open('file.txt', 'a') as f:
        f.write('\n' + word + " : " + meaning)
        print("Done!")
```

### def searcher():
Searches for the word

code:
```py
def searcher(word):
    data = [line for line in open('file.txt').readlines() if word in line]  # Checks if word exists
    if data:
        print("There you go!\n" + data[0])
    else:
        print("Sadly... Georgenotfound...")  # The End
```

### def randomizer():
Prints out a random word with it's definition

code:
```py
def randomizer():
    with open('file.txt') as f:
        content = f.readlines()
        word = choice(content)
    return word
```

### def exit():
Umm... exits?

code:
```py
exit()
```
