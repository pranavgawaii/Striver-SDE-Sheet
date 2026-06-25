class Solution:
    def sortStack(self, s: list[int]) -> None:
        if not s:
            return
            
        def insert_sorted(val):
            if not s or s[-1] <= val:
                s.append(val)
                return
                
            temp = s.pop()
            insert_sorted(val)
            s.append(temp)
            
        val = s.pop()
        self.sortStack(s)
        insert_sorted(val)
