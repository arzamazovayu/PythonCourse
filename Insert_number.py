t = int ( input() )
list_of_results =[]
while t > 0:
    nd = input()
    string = input()

    list_nd = list(map(int, nd.split()))
    n = list_nd[0]
    d = list_nd[1]
    list_string = list(map(int, string))
    q = 0

    for i in range(n):
        
        if d <= list_string[i]:
            q += 1
        else:
            list_string.insert(i, d)
            break
        if q == len(list_string):
            list_string.insert(n, d)
            break
        
    list_of_results.append(list_string)
    t -= 1

for value in list_of_results:
    res = "".join([str(val) for val in value])
    print(res) 