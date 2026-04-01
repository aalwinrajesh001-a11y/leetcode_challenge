class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=list(title.split(" "))
        for i in range(len(l)):
            n=len(l[i])
            if n==1 or n==2:
                l[i]=l[i].lower()
            else:
                l[i]=(l[i])[0].upper()+(l[i])[1:].lower()
        string=" ".join(l)
        return string

        
