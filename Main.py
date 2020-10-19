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

        

        return

word = input("Type your word (jumbled): ")
target = input("Type your target: ")
rearrange(word, target)

def find_common(word_1, word_2): #find no of common letters at respective places
    count = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            count += 1
    return count

