def swap(string, i, j):  #string -> list, make the swap, list -> string
    lst = []
    lst[:0] = string
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    new_string = ""
    for letter in lst:
        new_string += letter
    return new_string

def recursive_swap(string):  #swaps recursively, returns list of results
    results = []
    for i in range(len(string)-1):
        for j in range(i+1, len(string),):
            results.append(swap(string, i, j))
    return results

print(recursive_swap("hello"))