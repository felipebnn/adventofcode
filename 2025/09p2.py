#!/bin/env python3

with open('09_input.txt', 'r') as f:
    txt = f.read().strip('\n')

tiles = [ tuple([ int(x) for x in t.split(',') ]) for t in txt.split('\n') ]

# start compacting coordinates
x_coords = set()
y_coords = set()
for tile in tiles:
    x_coords.add(tile[0])
    y_coords.add(tile[1])

x_mapping = {}
r_x_mapping = {}
x = 0
for x_coord in sorted(x_coords):
    x_mapping[x_coord] = x
    r_x_mapping[x] = x_coord
    x += 2

y_mapping = {}
r_y_mapping = {}
y = 0
for y_coord in sorted(y_coords):
    y_mapping[y_coord] = y
    r_y_mapping[y] = y_coord
    y += 2
    
tiles = [ (x_mapping[x], y_mapping[y]) for x, y in tiles ]
# finished compacting coordinates

# draw edges
max_x = x_mapping[max(x_coords)]
max_y = y_mapping[max(y_coords)]
m = [
    [ 0 for _ in range(max_x+1) ]
    for _ in range(max_y+1)
]

def lerp(a, b):
    if a[0] == b[0]:
        if a[1] < b[1]:
            return ( a[0], a[1] + 1 )
        return ( a[0], a[1] - 1 )
    if a[0] < b[0]:
        return ( a[0] + 1, a[1] )
    return ( a[0] - 1, a[1] )

for i in range(-1, len(tiles)):
    a = tiles[i-1]
    b = tiles[i]
    m[a[1]][a[0]] = 1
    while a != b:
        a = lerp(a, b)
        m[a[1]][a[0]] = 1

# flood fill
# n = (3, 3)
n = (20, 250)
visited = { n }
q = [ n ]
m[n[1]][n[0]] = 1
while q:
    n = q.pop()
    nx, ny = n

    def traverse(dx, dy):
        x = nx+dx
        y = ny+dy
        if x < 0 or y < 0 or y >= len(m) or x >= len(m[0]) or (x,y) in visited or m[y][x] == 1:
            return
        m[y][x] = 1
        q.append((x, y))
        visited.add((x, y))

    traverse(0, 1)
    traverse(0, -1)
    traverse(1, 0)
    traverse(-1, 0)

# build 2d prefix
prefix = [
    [ 0 for _ in range(len(m[0])+1) ]
    for _ in range(len(m)+1)
]
for i in range(len(m)):
    for j in range(len(m[i])):
        prefix[i][j] = m[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

def query(a, b):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))

    return prefix[y2][x2] - prefix[y1-1][x2] - prefix[y2][x1-1] + prefix[y1-1][x1-1]

# calculate ans
largest_area = 0
for i in range(len(tiles)-1):
    a = tiles[i]
    for j in range(i+1, len(tiles)):
        b = tiles[j]

        # compacted area
        area1 = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
        if query(a, b) == area1:
            # sparse area
            area2 = (abs(r_x_mapping[a[0]]-r_x_mapping[b[0]])+1) * (abs(r_y_mapping[a[1]]-r_y_mapping[b[1]])+1)
            if area2 > largest_area:
                largest_area = area2

print(largest_area)

