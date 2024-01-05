# library that helps make our dictionary default to any data type we want
from collections import defaultdict

def groupAnagrams( strs: list[str]) -> list[list[str]]:
    
    # make anagram_map become into a dictionary in which it's keys are arrays
    anagram_map = defaultdict(list)

    # empty array that we'll add our values in for the tuples being added and their respective words which made them 
    result = []

    # for each value in dictionary
    for s in strs:

        # sorted(s) makes it so that each word in dictionary gets sorted ex: eat -> aet
        # tuple makes each char in sorted s become a tuple ex: aet -> ('a', 'e', 't')
        sorted_s = tuple(sorted(s))

        # when plugging it into the dictionary the dictionary doesnt accept duplicates so it stays as 1 key
        # we add ('a', 'e', 't') as a key in dictionary and also the words that make up tuple gets added
        # ex: 
        # ('a', 'e', 't'): ['eat', 'tea', 'ate'],
        # ('a', 'n', 't'): ['tan', 'nat'],
        # ('a', 'b', 't'): ['bat']
        anagram_map[sorted_s].append(s)

    # for each key in dictionary
    for val in anagram_map.values():

        # we make an array append each key value
        result.append(val)
    
    return result
    
input = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs= input))