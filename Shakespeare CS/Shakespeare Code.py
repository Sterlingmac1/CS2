import string


stop_words = ['and', 'or', 'i', 'the', 'a', 'to', 'of', 'in', 'is', 'it', 'that', 'you', 'my', 'not','with','his','be','have','but','your','he','our','me','for','what','all','so','as','him','we','do','are','will','which','no','on','this','they','from','yet','by','if','now','her','shall','o','thy','thee','she','then','here','an','go','am','thou','when','come','when']
counts = dict()
def shakespeare():
    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()

    
    for line in fhand:
        line = line.rstrip()
        # First two parameters are empty strings
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in stop_words:
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
    print(counts)

    
def writecsv():
    try:
        with open("write.csv", 'w') as outfile:

            outfile.write("words,Count\n")

            sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            top_15 = sorted_items[:15]
            

            for key, value in top_15:
                row = f"{key},{value}\n"
                outfile.write(row)
    
        print("yes")
    except Exception as e:
        print("an error occured:", e)


def main():
    shakespeare()
    writecsv()
main()