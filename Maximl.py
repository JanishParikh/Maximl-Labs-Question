from collections import defaultdict, Counter

def smallest_substring(S):
    j = ''.join(set(S))
    dict_t = Counter(j)
    required = len(dict_t)
    left = 0
    right = 0
    uniqueDict = {}
    min_window_len = float("inf")
    window_l = None
    window_r = None
    uniqueCharCount = 0
    while right < len(S):
 
       
        uniqueDict[S[right]] = uniqueDict.get(S[right], 0) + 1
 

        if S[right] in dict_t and uniqueDict[S[right]] == dict_t[S[right]]:
            uniqueCharCount += 1
 
       
        while left <= right and uniqueCharCount == required:
 
           
            if right - left + 1 < min_window_len:
                min_window_len = right - left + 1
                window_l = left
                window_r = right
 
            uniqueDict[S[left]] -= 1
            if S[left] in dict_t and uniqueDict[S[left]] < dict_t[S[left]]:
                uniqueCharCount -= 1
 
           
            left += 1
 
       
        right += 1
    return "" if min_window_len == float("inf") else len(S[window_l: window_r + 1])
 
 
S = input()
 
result = smallest_substring(S)
print (result)