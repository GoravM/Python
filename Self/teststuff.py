def lengthOfLongestSubstring( s: str) -> int:
    seen = {}
    prev_longest = ""
    curr_longest = ""

    for i,c in enumerate(s):
        if c in seen:
            prev_longest = curr_longest
            
    

input = "pwwkew"
# 3 b/c of wke
print(lengthOfLongestSubstring(input))

# for i,c in enumerate(s):
        
#         if c in seen:
#             return len(longest)
#         seen[c] = i
#         print(seen)
#         longest += c
#     return len(longest)