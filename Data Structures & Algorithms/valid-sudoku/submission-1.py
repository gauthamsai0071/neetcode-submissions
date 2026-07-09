class Solution:
    def isValidSudoku(self, mat: List[List[str]]) -> bool:
        '''
        00,01,02
        10,11,12
        20,21,22

        r=[0,1,2]
        c=[0,1,2]
        '''
        n=len(mat);m=len(mat[0])
        def checkRow(mat,r):
            seen={}
            for i in range(n):
                if mat[r][i] in seen and mat[r][i]!='.':
                    return False
                else:
                    seen[mat[r][i]]=1
            return True


        def checkCol(mat,c):
            seen={}
            for j in range(m):
                if mat[j][c] in seen and mat[j][c]!='.':
                    return False
                else:
                    seen[mat[j][c]]=1
            return True

        def checkBox(mat,r,c):
            seen={}
            startRow=(r//3)*3
            startCol=(c//3)*3

            for i in range(startRow, startRow+3):
                for j in range(startCol, startCol+3):
                    if mat[i][j] in seen and mat[i][j]!='.':
                        return False
                    else:
                        seen[mat[i][j]]=1
            return True
        
        for i in range(n):
            if checkRow(mat,i) == False:
                return False
                
        for j in range(m):
            if checkCol(mat,j) == False:
                return False
        
        for i in range(0,n,3):
            for j in range(0,m,3): 
                b=checkBox(mat,i,j)
                if b==False:
                    return False
        return True
