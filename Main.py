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

def recursive_swap(string):  #swaps recursively, returns list of results
    results = []
    for i in range(len(string)-1):
        for j in range(i+1, len(string),):
            results.append(swap(string, i, j))
    return results

def rearrange(word, target): #main A* function

    #trivial cases:
    if word == target:
        return 0
    elif len(word) == 2:
        return 1

    #non-trivial cases
    else:
        word_vertex = GV.Vertex(word)
        target_vertex = GV.Vertex(target)
        word_map = GV.Graph()
        word_map.add_vertex(word_vertex) #Head vertex created - stores original

        # add vertices for 1 swap
        swapping_word = word_vertex.value #temp var for word
        list_of_vertices = recursive_swap(swapping_word)

        for element in list_of_vertices:
            print(element)
            new_vertex = GV.Vertex(element)
            word_map.add_vertex(new_vertex)
            word_map.add_edge(word_vertex, new_vertex)
        word_map.print_graph()

        # compare swap results with target (find _common)
        """
        occurrence = []
        for edge in word_vertex.get_edges()
        """

        # repeat on swapped results with highest find_common count
        #repeat all till 1 swap result == target

        return #(no of swaps)

word = input("Type your word (jumbled): ")
target = input("Type your target: ")
num = str(rearrange(word, target))
print("Done!")
print("Least no. of swaps = " + num)



