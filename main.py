def main():
    
    def text_report(book):
        counts = {}
        book = book.lower()
        words = book.split()
                
        for char in book:
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1
        return len(words), counts
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

#get word count and character counts
        word_count, letter_counts = text_report(file_contents)

#print word count
        print(f"The total word count is {word_count}.")

#print character counts alphabetically
        counts = text_report(file_contents)
        for letter, count in sorted(letter_counts.items()):
            print(f"The '{letter}' character was found {count} times")
main()