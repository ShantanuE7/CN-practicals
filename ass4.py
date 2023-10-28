def main():
    no = int(input("Enter the number of nodes: "))
    
    dm = [[0] * no for _ in range(no)]
    route = [{'dist': [0] * no, 'from': [0] * no} for _ in range(no)]
    
    print("Enter the distance matrix:")
    
    for i in range(no):
        for j in range(no):
            dm[i][j] = int(input())
            # Set distance from i to i as 0
            dm[i][i] = 0
            route[i]['dist'][j] = dm[i][j]
            route[i]['from'][j] = j
    
    flag = 0
    while not flag:
        flag = 1
        for i in range(no):
            for j in range(no):
                for k in range(no):
                    if route[i]['dist'][j] > route[i]['dist'][k] + route[k]['dist'][j]:
                        route[i]['dist'][j] = route[i]['dist'][k] + route[k]['dist'][j]
                        route[i]['from'][j] = k
                        flag = 0

    for i in range(no):
        print("Router info for router:", i + 1)
        print("Dest\tNext Hop\tDist")
        for j in range(no):
            print(f"{j+1}\t{route[i]['from'][j]+1}\t\t{route[i]['dist'][j]}")

if __name__ == "__main__":
    main()


'''
OUTPUT:
Enter the number of nodes: 3
Enter the distance matrix:
4
5
9
8
3
7
5
2
8
Router info for router: 1
Dest    Next Hop        Dist
1       1               0
2       2               5
3       3               9
Router info for router: 2
Dest    Next Hop        Dist
1       1               8
2       2               0
3       3               7
Router info for router: 3
Dest    Next Hop        Dist
1       1               5
2       2               2
3       3               0


'''