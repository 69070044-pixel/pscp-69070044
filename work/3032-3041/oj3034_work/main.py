"""OJ3034"""
n, k,  = [int(x) for x in input().split()]
queue = [] 
line_is_full = False

for i in range(k):
    # create ช่องของแถว
    i += 1
    queue.append([]) 

while n:
    row = int(input()) - 1 # -1 เพื่อให้กลายเป็น index
    queue[row].append(row + 1) # add row value to list
    for q in queue:
        if q: # q is not []
            line_is_full = True
        else:
            # found [] mean line not full
            line_is_full = False
            break #don't loop more
    if line_is_full:
        # now line full
        for q in range(k):
            # take first people in the line
            queue[q].pop(0)
    n -= 1
result = 0
# find people remainning in queue list
for q in queue:
    result += len(q)
print(result)