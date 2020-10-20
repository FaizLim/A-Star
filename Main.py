import Graph_Vertex as GV

def find_common(word_1, word_2): #find no of common letters at respective places, assume len(word_1) = len(word_2)
    count = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            count += 1
    return count

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
        for i in range(len(swapping_word)):
            for j in range(len(swapping_word)):
                j += 1
                #make 1 swap per cycle for each letter
                if i+1 is not j:
                    tmp_word = swapping_word[:i] + swapping_word[j] + swapping_word[i+1:j] + swapping_word[i] + swapping_word[j+1:]
                else:
                    tmp_word = swapping_word[:i+1] + swapping_word[j] + swapping_word[i] + swapping_word[j+1:]
                print(tmp_word)

                tmp_word_vertex = GV.Vertex(tmp_word)
                word_map.add_vertex(tmp_word_vertex)
                word_map.add_edge(word_vertex, tmp_word_vertex)
        word_map.print_graph()

        # compare swap results with target (find _common)
        """
        occurrence = []
        for edge in word_vertex.get_edges()
        """

        # repeat on swapped results with highest find_common count
        #repeat all till 1 swap result == target

        return

word = input("Type your word (jumbled): ")
target = input("Type your target: ")
num = str(rearrange(word, target))
print("Done!")
print("Least no. of swaps = " + num)



