import time
# from quicksort import qsort
    # this import was used to test quicksort for fun

def readAlpha():
    with open("words_alpha.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()        # Reading all words from the file
        alphaList = [0]*len(lines)
        for i in range (len(lines)):    
            alphaList[i] = lines[i][:-1]    # removing newline character and adding to list
        file.close()
    return alphaList

def readSanat():
    sanaList = []
    with open("kaikkisanat.txt", "r", encoding="utf-8") as file:
        for line in file:
            sanaList.append(line[:-1])  #removing newline character
        file.close()
    return sanaList

if __name__ == "__main__":
    start = time.time()
    alphaList = readAlpha() # Reading words to a list
    sanaList = readSanat()
    mid2 = time.time()

    # Sorting the list so we can use built in string comparison functionality while searching for common words
    alphaList.sort()
    sanaList.sort()

    mid = time.time()

    alphaIndex = 0  # Index of alphaList, "English" words
    sanaIndex = 0   # Index if sanaList, "Finnish" words
    total = 0       # Total number of matching words
    while alphaIndex < len(alphaList):  # Loop ends if we run out of English words to compare
        if sanaIndex == len(sanaList):  # Also breaks if there are no more Finnish words.
            break                           # Could've added to while condition but hey :)

        alphaWord = alphaList[alphaIndex]   # Current english word
        sana = sanaList[sanaIndex]          # Current finnish word
        if alphaWord == sana:       # If we have a match,
            alphaIndex += 1         # move both indecies by 1
            sanaIndex += 1
            total += 1              # and add to total.
            continue

        if alphaWord > sana:    # Comparing words
            sanaIndex += 1      # alphaWord is 'bigger', so increasing sanaIndex to catch up
        else:
            alphaIndex += 1     # sana is 'bigger', so increasing alphaIndex to catch up

    end = time.time()
    
    print()
    print(f"Adding words to lists: {round(mid2-start,4)}s")
    print(f"Sorting the lists: {round(mid-mid2,4)}s")
    print(f"Finding common words: {round(end-mid,4)}s")
    print(f"Total run time: {round(end-start, 4)}s")    # Around 0.17-0.19s on my hardware.
    print("Total matching words found:", total)     # 1250
    #print("Final list indeces:", alphaIndex, sanaIndex) # Shows that we run out of english words first. Great for debugging!
    print()
