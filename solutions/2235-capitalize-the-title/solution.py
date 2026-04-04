class Solution:
    def capitalizeTitle(self, title: str) -> str:
        w = title.split()
        for i in range(len(w)):
            if len(w[i]) <= 2:
                w[i] = w[i].lower()
            else:
                w[i] = w[i].capitalize()
        return " ".join(w)
