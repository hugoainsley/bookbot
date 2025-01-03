def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    word_count(file_contents)
    character_count(file_contents)
    print("--- End report ---")

def word_count(contents):
    count = 0
    words = contents.split()
    for word in words:
        count += 1
    print(f"{count} words found in the document")

def sort_on(dict):
    return dict["num"]

def character_count(contents):
    characters_count = {}
    characters_list = []
    for char in contents:
        lower_char = char.lower()
        if lower_char in characters_count:            
            characters_count[lower_char] += 1
        else:
            characters_count[lower_char] = 1

    for char in characters_count:
        if char.isalpha():
            characters_list.append({"char": char, "num": characters_count[char]})
    
    characters_list.sort(reverse=True, key=sort_on)

    for dic in characters_list:
        print('The ' + "'" + dic["char"] + "'" + f' character was found {dic["num"]} times')

main()
