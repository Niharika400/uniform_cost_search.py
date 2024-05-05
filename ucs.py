q = []
visited = []
graph = [['S', 'Z', 0], ['A', 'S', 1], ['B', 'S', 5], ['C', 'S', 15], ['G', 'A', 10], ['G', 'B', 5], ['G', 'C', 5]]

def generate_children(curr_state):
    global graph
    global q
    global visited
    for i in range(len(graph)):
        if graph[i][1] == curr_state[1]:
            new_cost = curr_state[0] + graph[i][2]
            new_state = [new_cost, graph[i][0]]
            
            for j in range(len(q)):
                if q[j][1] == new_state[1]:
                    if new_state[0] < q[j][0]:
                        q[j] = new_state
                    found = True
                    break
            if not found:
                q.append(new_state)
            
            for k in range(len(visited)):
                if visited[k][1] == new_state[1]:
                    if new_state[0] < visited[k][0]:
                        visited[k] = new_state
                    
                    break
            if not found:
                visited.append(new_state)
def uniform_cost_search(s,g):
    global q
    while(1):
        q.sort()
        curr_state=q[0]
        if curr_state[1]==g:
            print(curr_state)
            exit()
        del q[0]    
           
        visited.append(curr_state)
        generate_children(curr_state)
   

def main():
    s = 'S'
    g = 'G'
    uniform_cost_search(s, g)

if __name__ == "__main__":
    main()