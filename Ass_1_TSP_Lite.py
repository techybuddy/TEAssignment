import copy
inf = float('inf')

class TSP_AI:

    def __init__(self, matrix = None, source = 0) -> None:
        self.matrix = [ [ 0 ]*4 ]*4 if matrix is None else matrix
        self.n = len(self.matrix)
        self.source = source



    def Input(self):
        self.n = int(input('Enter city count : '))
        self.matrix = []
        for i in range(self.n):                                                         # Get the distances between cities
            self.matrix.append([ 
                inf if i == j else int(input(f'Cost to travel from city {i+1} to {j+1} : '))
                for j in range(self.n)
             ])
        print(self.matrix)
        self.source = int(input('Source: ')) % self.n                                   # Get the source city



    def solve(self):
        minCost = inf                                                                   # Initially minCost is infinity
        for i in range(self.n):
            print("Path", end='')
            cost = self._solve(copy.deepcopy(self.matrix), i, i)                        # Calling solver for each as source city
            print(f" -> {i+1}    :    Cost = {cost}")
            if cost and cost < minCost: minCost = cost                                  # If this cost is optimal, save it
        
        return minCost



    def _solve(self, matrix, currCity = 0, source = 0 ):

        if self.n < 2: return 0
        print(f" -> {currCity+1}", end='')

        for i in range(self.n):
            matrix[ i ][ currCity ] = inf                                               # Set all values in the currCity column as infinity (once visited, shouldn't be visited anymore)

        currMin, currMinPos = inf, 0
        for j in range(self.n):
            if currMin > matrix[ currCity ][ j ]:                                       # Get the nearest city to the current city
                currMin, currMinPos = matrix[ currCity ][ j ], j

        if currMin == inf: return self.matrix[ currCity ][ source ]                     # If currMin is infinity(i.e. all cities have been visited, return cost of moving from this last city to start city to complete the path-loop)
        matrix[ currCity ][ currMinPos ] = matrix[ currMinPos ][ currCity ] = inf       # Set distance from currCity to next city and vice versa to infinity
        return currMin + self._solve(matrix, currMinPos, source)                        # Calling the next recursion for selected city



# Driver code
if __name__ == '__main__':
    matrix = [ 
        [ inf,  10,   15,    20,   299,  67,   24  ],
        [ 10,   inf,  35,    25,   5,    88,   44  ],
        [ 15,   35,   inf,   30,   52,   454,  13  ],
        [ 20,   25,   30,   inf,   139,  23,   89  ],
        [ 299,   5,   52,   139,   inf,  93,   10  ],
        [ 67,   88,   454,  23,    93,   inf,  89  ],
        [ 24,   44,   13,   89,    10,   89,   inf ],
     ]

    source_city = 0
    tsp = TSP_AI(matrix, source_city)
    # tsp.Input()                                                                       # For Custom Input
    print(f"Optimal Cost : {tsp.solve()}")
