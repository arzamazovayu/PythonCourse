import math
t = int ( input() )
list_of_list_of_max = []
while t > 0:
    n = int ( input() )
    ai = input()
    a = list(map(int, ai.split()))
    list_of_max = []

    while n > 0:
        an = a[:]
        an[n-1] = a[n-1] + 1
        s = math.prod(an)
        list_of_max.append(s)
        n -= 1
    list_of_list_of_max.append(max(list_of_max))
    t -= 1
for max_value in list_of_list_of_max:
    print(max_value)    
