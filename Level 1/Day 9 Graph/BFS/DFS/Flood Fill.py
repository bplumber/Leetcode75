class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        r = len(image)
        c = len(image[0])
        start = image[sr][sc]
        
        def hlp(tr, tc, color):
            nonlocal r, c, start
            if tr < 0 or tr >= r or tc < 0 or tc >= c:
                return
            if image[tr][tc]==start:
                image[tr][tc]=color
                hlp(tr-1, tc, color)
                hlp(tr+1, tc, color)
                hlp(tr, tc+1, color)
                hlp(tr, tc-1, color)
            else:
                return
        hlp(sr, sc, color)
        return image