import Graph_Vertex as GV

def find_common(word_1, word_2): #find no of common letters at respective places
    count = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            count += 1
    return count

def rearrange(word, target): #main A* function
    if word == target:
        print("Done! ")
        return
    else:
        word_vertex = GV.Vertex(word)
        target_vertex = GV.Vertex(target)
        word_map = GV.Graph()
        word_map.add_vertex(word_vertex) #Head vertex created - stores original

        # add vertices for 1 swap
        swapping_word = word_vertex.value #temp var for word
        for i in range(len(swapping_word)-1):
            for j in range(len(swapping_word)):
                j =+ 1
                tmp_word = swapping_word
                #make 1 swap per cycle for each letter
                tmp = tmp_word[i]
                tmp_word[i] = tmp_word[j]
                tmp_word[j] = tmp
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
rearrange(word, target)



