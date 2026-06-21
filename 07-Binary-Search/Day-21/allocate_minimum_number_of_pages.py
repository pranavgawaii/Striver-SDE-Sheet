class Solution:
    def findPages(self, A: list[int], N: int, M: int) -> int:
        if M > N:
            return -1
            
        def isPossible(pages):
            studentCount = 1
            pagesAllocated = 0
            
            for book_pages in A:
                if pagesAllocated + book_pages > pages:
                    studentCount += 1
                    pagesAllocated = book_pages
                else:
                    pagesAllocated += book_pages
                    
            return studentCount <= M
            
        low = max(A)
        high = sum(A)
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return result
