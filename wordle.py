import sys


def word_check(word,required_locations,required_letter,required_missing_letter):
    w = list(word)
    rloc = list(required_locations)
    rlet = list(required_letter)
    rmisslet = list(required_missing_letter)

    # check locations that MUST exist in specific location
    for i in range(5):
        if (rloc[i] != "0" and w[i] != rloc[i]):
            return False

    # check letter that need to exist, just sorta anywhere
    for i in range(len(rlet)):
        if (rlet[i] != "0" and rlet[i] not in word):
            return False

    # check letter should not, just sorta anywhere
    for i in range(len(rmisslet)):
        if (rmisslet[i] != "0" and rmisslet[i] in word):
            return False

    return True

def main():
    f = open('wordle-list.txt', 'r')
    words = f.readlines()
    
    count = 0
    for w in words:
        count += 1
        status = word_check(w,sys.argv[1],sys.argv[2],sys.argv[3])
        if(status == True):
            print("Word{}: {} {}".format(count, w.strip(),status))

if __name__ == "__main__":
    main()