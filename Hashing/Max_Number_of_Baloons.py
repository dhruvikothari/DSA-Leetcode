class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnttxt = Counter(text)
        balloon = Counter("balloon")

        instance = len(text)  # or float("inf")
        for c in balloon:
            instance = min(instance, cnttxt[c] // balloon[c])
        return instance
