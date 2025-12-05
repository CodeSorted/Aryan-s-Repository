from collections import deque

def water_jug():
    cap1 = 4
    cap2 = 3
    target = 2

    queue = deque()
    queue.append((0,0))

    visited = set()
    visited.add((0,0))

    while queue:
        x,y = queue.popleft()
        print("Current State : ",(x,y))

        if x == target or y == target:
            print("Target Reached")
            return
        
        new_states = []

        new_states.append((cap1,y))
        new_states.append((x,cap2))
        new_states.append((0,y))
        new_states.append((x,0))

        pour = min(y,cap1-x)
        new_states.append((x+pour,y-pour))

        pour = min(x,cap2-y)
        new_states.append((x-pour,y+pour))

        for s in new_states:
            if s not in visited:
                visited.add(s)
                queue.append(s)

water_jug()
