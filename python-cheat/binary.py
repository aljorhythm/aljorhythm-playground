def brecurs(l, s=None, e=None, depth=0):
    if s == None:
        s = 0
    if e == None:
        e = len(l) - 1

    print("\t" * depth, "l", l[s:e + 1])
    print("\t" * depth, "s", s, "e", e)
    
    if s >= e:
        return

    mid = (s + e) // 2
    print("\t" * depth, "mid: ", mid)
    print("\t" * depth, "left", s, mid)
    brecurs(l, s, mid, depth+1)
    print("\t" * depth, "right", mid + 1, e)
    brecurs(l, mid + 1, e, depth+1)

for i in range(7):
    print("length", i)
    l = [x for x in range(i)]
    print(l)
    # brecurs(l)
    if l:
        l[(i -1)//2] = "mid-end"
        print(l)
    print("****")
    print("")