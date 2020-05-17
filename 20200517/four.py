def numPoints(points, r):
    cal_distance = lambda p1, p2: pow(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2), 0.5)
    cal_center
    max_count = 0
    for i, point1 in enumerate(points):
        count = 0
        for j, point2 in enumerate(points):
            if i == j:
                continue
    print(max_count)
    return max_count

io = [
    [
        [[[-2,0],[2,0],[0,2],[0,-2]], 2],
        4
    ],
    [
        [[[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], 5],
        5
    ]
]

results = []
for (i, o) in io[:0]:
    result = numPoints(i[0], i[1])
    print(result)
    print(result == o)
    results.append((result == o, result))

print(results)
