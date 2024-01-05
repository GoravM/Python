
def longestCommonPrefix(strs):
    wordatit = ""
    mylist = []
    
    if len(strs) < 2:
        return strs[0]

    for i in range(1, len(strs)):
        if len(strs[i]) > len(strs[0]):
            strs[i] = strs[i][0:len(strs[0])]

        for j in range(0, len(strs[i])):
            if strs[0][j] == strs[i][j]:
                wordatit += strs[i][j]
            else:
                break

        mylist.append(wordatit)
        wordatit = ""

    return min(mylist)


mywords = ["cir", "car"]
# returns "c"

print(longestCommonPrefix(strs= mywords))