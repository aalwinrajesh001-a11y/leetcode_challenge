class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ns=[""]*len(s)
        for i in range(len(indices)):
            ns[i]=s[indices.index(i)]
        return "".join(ns)
