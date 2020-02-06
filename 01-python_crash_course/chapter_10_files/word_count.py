def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # ~ msg = "Sorry, the file " + filename + " does not exist."
        # ~ print(msg)
        pass #si decido no hacer nada
    else:
        #Count the approximate number of words in the file.
        words = contents.split() 
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames: 
    count_words(filename)
