from random import choice


def main():
    def searcher(word):
        with open('file.txt') as f:
            content = f.readlines()
            i = 0
            while True:
                if i < len(content):  # Just keeps sure it is in the file length
                    if word in content[i]:
                        print("There you go!\n" + content[i])
                        break
                    else:
                        i += 1
                else:
                    print("Sadly... Georgenotfound...")  # The end...
                    break

    def adder(word, meaning):
        with open('file.txt', 'a') as f:
            f.write('\n' + word + " : " + meaning)
            print("Done!")

    def randomizer():
        with open('file.txt') as f:
            content = f.readlines()
            word = choice(content)
        return word

    while True:
        print("\033[4m~= Welcome to The Dictionary lord! =~\033[0m")  # Warm Welcome

        tasks = ['', '1) Search for the meaning of the word', '2) Add a word', '3) Remind a random word', '4) Exit']
        for i in range(len(tasks)):
            print(tasks[i])

        try:
            task = int(input("What do you want to do?\n|} "))
            if task < len(tasks):  # Checks if the index exists
                if task == 1:
                    input_word = input("Enter the word: ")
                    searcher(input_word)
                elif task == 2:
                    wor = input("Enter the word to add: ").lower()
                    defi = input("Enter definition: ").lower()
                    adder(wor, defi)
                elif task == 3:
                    print(randomizer())
                elif task == 4:
                    exit()
                else:
                    print("-_- '0' is not in the list")
            else:
                print("-_- Index greater than the total number of jobs")

        except ValueError:
            print("-_- Incorrect input, please enter the index. Not the word.")


if __name__ == '__main__':
    main()
