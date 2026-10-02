class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new =[]
        greatest = 0
        for i in range(len(arr)-1):
            greatest = 0
            for x in arr[i+1:]:
                if x >= greatest:
                    greatest = x        
            new.append(greatest)
        new.append(-1)
        return(new)

