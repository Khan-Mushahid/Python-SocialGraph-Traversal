# percepts = []
# table = {
#     (("A", "Dirty"),): "Clean",
#     (("A", "Clean"),): "Right",
#     (("B", "Dirty"),): "Clean",
#     (("B", "Clean"),): "Left"
# }

# def lookup_table(percepts, table):
#     action = table.get(tuple(percepts))
#     return action

# def table_driven_agent(percept):
#     percepts.append(percept)
#     action = lookup_table(percepts, table)
#     return action

# def main():
#     print('percept \t\t\t Action')
#     print(percepts, '\t\t' ,table_driven_agent(('A','Dirty')))

# main()

#Reflex agent

# goalState = {'A' : '0' , 'B' : '0'}
# acyion = 0 # 0 = Clean, 1 = Dirty
# cost = 0
# roomstate = {'A' : '1' , 'B' : '1'}

#initial inupts
# print("Enter the starting location of rooms(A/B)")
# location = input()

# for room in roomstate:
#     action = input("Enter the state of " + room + "(0 mean clean 1 means Dirty)")
# roomstate[room] = action
# print("Current state: " + str(roomstate))
# print("Goal state: " + str(goalState))
# print("vaccum cleaner is placed in location " + str(location))
# if(roomstate != goalState):
#     if(roomstate['A'] == 1): #if dirty
#         roomstate['A'] = '0'
#         cost+=1
#         print("Location A was dirty\nation A has been clean ")
#     if(roomstate == goalState):
#         print("Goalstate has been met.")
#         print("\nTotal cost: " + str(cost))

#     else:
#         print("\nAll rooms are already clean")
#         print("\nTotal cost:  " + str(cost))

    
# percepts = []
# table = {
#         (('A', 'Clean'),): 'Move Right',
#         (('A', 'Dirty'),): 'Remove the dirt',
#         (('B', 'Dirty'),): 'Remove the dirt',
#         (('B', 'Clean'),): 'Move Left',
#         (('A', 'Clean'),('A', 'Clean'),): 'Move Right',
#         (('A', 'Clean'), ('A', 'Dirty'),): 'Remove the dirt',
#         (('B', 'Dirty'), ('B', 'Dirty'),): 'Remove the dirt',
#         (('B', 'Dirty'), ('B', 'Clean'),): 'Move Left',
#         (('A', 'Dirty'), ('A', 'Dirty'),): 'Remove the dirt',
#         (('A', 'Dirty'), ('A', 'Clean'),): 'Move Right',
#         (('A', 'Clean'), ('A', 'Clean'), ('B', 'Dirty'),): 'Remove the dirt',
#         (('A', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'),): 'Move Right'
#     }
    
# def lookup_table(percepts, table):
#      action = table.get(tuple(percepts))
#      return action

# def table_driven_agent(percept):
#     percepts.append(percept)
#     action = lookup_table(percepts, table)
#     return action

# def main():
#     print('percept \t\t\t Action')
#     print(percepts, '\t\t' ,table_driven_agent(('A','Clean')))
#     print(percepts, '\t\t' ,table_driven_agent(('A','Clean')))
#     print(percepts, '\t\t' ,table_driven_agent(('B','Dirty')))
    

# main()

#Reflex agent

# #Reflex based agents
# goalState={'A': '0', 'B': '0', 'C':'0'}
# action=0 #0=clean, 1=dirty
# cost =  0
# roomState={'A': '1', 'B': '1','C':'1'}
# #initial inputs
# print("Enter the starting location of rooms(A/B)")
# location=input()
# for room in roomState:
#     action=input("Enter the state of " +room+ "(0 means Clean 1 means Dirty)")
#     roomState[room]=action
# print("Current state: " + str(roomState))
# print("Goal State: "+ str(goalState))
# print("Vaccum cleaner is placed in location: "+ str(location))
# if(roomState != goalState):
#     if(roomState['A']=='1'):
#         roomState['A']='0'
#         cost+=1
#         print("Loacation A was dirty \n Location A has been cleaned")
#     if(roomState==goalState):
#         print("Goal State has been met.")
#         print("\nTotal Cost: "+ str(cost))
#     else:
#         print("\nA is clean")
#         print("\nA-> B")
#         print("\n Cost for moving within rooms=1")
#         cost+=1
#         if(roomState['B']=='1'):
#             roomState['B']=='0'
#             cost+=1
#             print("Loacation B was dirty \n Location B has been cleaned")
#         if(roomState == goalState):
#             print("Goal state has been met.")
#             print("\nTotal cost: "+ str(cost))
        
#         if(roomState['C']=='1'):
#             roomState['B']=='0'
#             cost+=1
#             print("Loacation B was dirty \n Location B has been cleaned")
#         if(roomState == goalState):
#             print("Goal state has been met.")
#             print("\nTotal cost: "+ str(cost))
#         else:
#              print("\nB is clean")
#              print("\nB-> C")
#              print("\n Cost for moving within rooms=1")
#              cost+=1
        
# print("\nAll rooms are already clean")
# print("\nTotal cost: "+ str(cost))
# goalState = {'A': '0', 'B': '0', 'C': '0', 'D': '0'}
# actions = {'0': 'CLEAN', '1': 'DIRTY'}
# cost = 0
# roomstate = {'A': '1', 'B': '1', 'C': '1', 'D': '1'}

# print("Enter the starting location of the vacuum (A/B/C/D):")
# location = input().strip().upper()


# while location not in ['A', 'B', 'C', 'D']:
#     print("Invalid location. Please enter A, B, C, or D:")
#     location = input().strip().upper()

# for room in roomstate:
#     if room != location:
#         print(f"Enter the status of room {room} (0 for clean, 1 for dirty):")
#         status = input().strip()
#         while status not in ['0', '1']:
#             print("Invalid status. Please enter 0 for clean, 1 for dirty:")
#             status = input().strip()
#         roomstate[room] = status

# print("Current state:", roomstate)
# print("Goal state:", goalState)
# print("Vacuum cleaner is placed in location:", location)

# while roomstate != goalState:
#     if roomstate[location] == '1': 
#         roomstate[location] = '0'
#         cost += 1
#         print(f"Location {location} was dirty.")
#         print(f"Location {location} has been cleaned.")


#     if location == 'A':
#         location = 'B'
#     elif location == 'B':
#         location = 'C'
#     elif location == 'C':
#         location = 'D'
#     # elif location == 'D':
#     #     location = 'A'

#     if roomstate[location] == '1':
#         cost += 1

#     print("Moved to location:", location)

# print("\nGoal state has been met.")
# print("\nTotal cost:", cost)


#lab04
# mygraph={"A":["B","C"],
#           "B":["D","E"],
#           "C":["F"],
#           "D":[],
#           "E":["F"]
#         }
# print(mygraph["A"])

















#BFS
# def my_bfs(mygraph, start_node):
#     visited = []
#     queue = []
#     visited.append(start_node)
#     queue.append(start_node)

#     while queue:
#         current_node = queue.pop(0)
#         print(current_node, end=" ")

#         for neighbor in mygraph[current_node]:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)

# mygraph = {
#     "1": ["2", "3" , "4"],
#     "2": ["5", "6"],
#     "3":[],
#     "4":["7", "8"],
#     "5": ["9","10"],
#     "6": [],
#     "7":["11","12"],
#     "8":[],
#     "9":[],
#     "10": [],
#      "11":[],
#     "12": [],
#     
# }

# print("BFS Traversal:")
# my_bfs(mygraph, "A")


#DFS


visited_bfs = []
queue = []
goal = "Uzma"

def my_bfs(mygraph, start_node):
    global visited_bfs
    global queue

    visited_bfs.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        if current_node == goal:
            return

        for neighbor in mygraph[current_node]:
            if neighbor not in visited_bfs:
                visited_bfs.append(neighbor)
                queue.append(neighbor)

visited_dfs = []

def my_dfs(mygraph, start_node):
    global visited_dfs

    visited_dfs.append(start_node)
    print(start_node, end=" ")

    if start_node == goal:
        return

    for neighbor in mygraph[start_node]:
        if neighbor not in visited_dfs:
            my_dfs(mygraph, neighbor)
            if goal in visited_dfs:  
                return

mygraph = {
    'Amina': ['Sara', 'Razi', 'Ahmed'],
    'Sara': ['Amina'],
    'Razi': ['Amina', 'Ali', 'Ahmed'],
    'Ali': ['Razi'],
    'Ahmed': ['Amina', 'Razi', 'Ahsan'],
    'Rida': ['Hassan', 'Taha'],
    'Hassan': ['Rida'],
    'Taha': ['Rida', 'Uzma', 'Ahsan'],
    'Uzma': ['Taha', 'Ahsan'],
    'Ahsan': ['Ahmed', 'Taha', 'Uzma']
}


print("BFS TRAVERSAL:")
my_bfs(mygraph, "Sara")

print("\nDFS TRAVERSAL:")
my_dfs(mygraph, "Sara")












    







