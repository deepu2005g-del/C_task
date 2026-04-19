# Task 5: file manipulation

def word_count(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read().lower()

        words = text.split()
        count = {}

        for word in words:
            word = word.strip('.,!?";:()[]')
            count[word] = count.get(word, 0) + 1

        for word in sorted(count):
            print(f"{word}: {count[word]}")

    except FileNotFoundError:
        print("File not found. Please check the file name and path.")

file_name = input("Enter file name: ")
word_count(file_name)