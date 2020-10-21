import Graph_Vertex as GV

def find_common(word_1, word_2): #find no of common letters at respective places, assume len(word_1) = len(word_2)
    count = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            count += 1
    return count

def swap(string, i, j):  #string -> list, make the swap, list -> string
    lst = []
    lst[:0] = string
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    new_string = ""
    for letter in lst:
        new_string += letter
    return str(new_string)

def recursive_swap(string):  #swaps with double loop, covers all combinations
    results = []
    for i in range(len(string)-1):
        for j in range(i+1, len(string),):
            results.append(swap(string, i, j))
    return results

def rearrange(word, target, x = 0): #main A* function
    print(word)
    #trivial cases:
    if word == target:
        pass
    elif len(word) == 2:
        x = 1

    #non-trivial cases
    else:
        word_vertex = GV.Vertex(word)
        target_vertex = GV.Vertex(target)
        word_map = GV.Graph()
        word_map.add_vertex(word_vertex) #Head vertex created - stores original

        # add vertices for 1 swap
        swapping_word = word_vertex.value
        list_of_vertices = recursive_swap(swapping_word)

        for element in list_of_vertices:  #adds every swapped string to graph
            new_vertex = GV.Vertex(element)
            word_map.add_vertex(new_vertex)
            word_map.add_edge(word_vertex, new_vertex)

        #word_map.print_graph()            #confirmation of results

        if target in word_map.graph_dict.keys():
            x += 1
        else:
        # compare swap results with target (find _common)
            occurrences = list_of_vertices
            best = []
            max = 0
            for occ in occurrences:
                num = find_common(occ, target)
                if max > num:
                    pass
                elif max == num:
                    best.append(occ)
                else:
                    max = num
                    best = [occ]
            #print(best)                 #best now stores the list with most common letters
            #This implementation is from the distance measuring component of A* (direction)

            # repeat on swapped results with highest find_common count
            min_x = 99999
            for outcome in best:
                # repeat all till 1 swap result == target
                num = rearrange(outcome, target, x + 1)
                if min_x < num:
                    pass
                else:
                    min_x = num
            x += min_x #only shortest path is taken into account

    return x

word = input("Type your word (jumbled): ")
target = input("Type your target: ")
num = str(rearrange(word, target))
print("Done!")
print("Least no. of swaps = " + num)



