import PyPDF2

# function to ask for user input file
def analyze_book():
    pdf_file = input("Enter name of pdf file to analyze :")
    pdf_to_text(pdf_file)


# function to convert pdf file into text
def pdf_to_text(pdf_file):
    with open(pdf_file, "rb") as pdffileobj:
        reader = PyPDF2.PdfReader(pdffileobj)
        result = []
        x = len(reader.pages)
        for i in range(0, x):
            current_page = reader.pages[i]
            current_text = current_page.extract_text()
            result.append(current_text)
        result = " ".join(result)
        clean_text(result)


# function to convert text to lowercase and alphabetic characters
def clean_text(text):
    # convert text to list of strings for easier manipulation
    text = list(text.split())
    # empty list to store new text
    new_text = []
    for word in text:
        # filter out special characters
        word = "".join(filter(str.isalpha, word))
        # if not empty string, add lowercase form to new list
        if word:
            new_text.append(word.lower())
    create_dict(new_text)


# function to create a dictionary for word-freq pairs
def create_dict(new_text):
    word_freq = {}
    for word in new_text:
        if word not in word_freq.keys():
            word_freq[word] = 0
        word_freq[word] += 1
    get_stats(word_freq)


# function to get and print statistics
def get_stats(word_freq):
    vocab_range = len(word_freq.keys())
    sorted_word_freq = sorted(word_freq, key=word_freq.get, reverse=True)
    word_count = sum(word_freq.values())
    print("\n----Kai's Ebook Analyzer----\n")
    print("Vocabulary range:", vocab_range, "\n")
    print("Word count:", word_count, "\n")
    print("Top 10 words:\n")
    for i in range(1, 11):
        word = sorted_word_freq[i - 1]
        freq = word_freq[word]
        print(i, ")", word, "=", freq)


# main call to program
analyze_book()
