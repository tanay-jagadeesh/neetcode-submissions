class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        parts = path.split('/')

        for p in parts: 
            if p == "." or p =='':
                continue
            elif p == ".." and stack:
                stack.pop()
            elif p == ".." and not stack:
                continue
            else: 
                stack.append(p)
        
        return "/" + "/".join(stack)




    """
     e.g. /neetcode/practice//...///../courses

     ['', 'neetcode', 'practice', '', '...', '', '..', 'courses']

     if '' then we continue

    """
