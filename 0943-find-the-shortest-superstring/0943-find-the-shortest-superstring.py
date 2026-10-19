class Solution(object):
    def shortestSuperstring(self, words):
        n = len(words)

        # Calculate overlap between every pair of words
        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    for k in range(min(len(words[i]), len(words[j])), 0, -1):
                        if words[i].endswith(words[j][:k]):
                            overlap[i][j] = k
                            break

        # dp[mask][i] = shortest superstring ending at word i
        dp = [[""] * n for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = words[i]

        for mask in range(1 << n):
            for i in range(n):
                if not (mask & (1 << i)):
                    continue

                for j in range(n):
                    if mask & (1 << j):
                        continue

                    new_mask = mask | (1 << j)

                    candidate = dp[mask][i] + words[j][overlap[i][j]:]

                    if dp[new_mask][j] == "" or len(candidate) < len(dp[new_mask][j]):
                        dp[new_mask][j] = candidate

        # Find the shortest string containing all words
        answer = ""

        for i in range(n):
            result = dp[(1 << n) - 1][i]

            if answer == "" or len(result) < len(answer):
                answer = result

        return answer