from util import check

class Solution:

    def visit_neighbours(self, p, m,n,grid):
        x,y=p
        if x>0 :
            if grid[x-1][y]=='1':
                grid[x-1][y]=2
                self.visit_neighbours((x-1,y),m,n,grid)
        if x+1<=n-1:
            if grid[x+1][y]=='1':
                grid[x+1][y]=2
                self.visit_neighbours((x+1,y),m,n,grid)
        if y>0 :
            if grid[x][y-1]=='1':
                grid[x][y-1]=2
                self.visit_neighbours((x,y-1),m,n,grid)

        if y+1<=m-1:
            if grid[x][y+1]=='1':
                grid[x][y+1]=2
                self.visit_neighbours((x,y+1),m,n,grid)


    def numIslands(self, grid) -> int:
        m=len(grid)
        if m>0:
            n=len(grid[0])
        else:
            return 0
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count=count+1
                    self.visit_neighbours((i,j),n,m,grid)
        return count



sol=Solution()
check([[
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]],[1], sol.numIslands)


check([[
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]],[3], sol.numIslands)
