# https://www.youtube.com/watch?v=-fx6aDxcWyg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25
# https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        X = word1; Y = word2; m = len(X); n = len(Y)
		# Implement Longest Common Subsequence DP
		# LCS of X and Y is ea [X = "heap", Y = "pea"]
		# in X LCS will remain intact and remaining charecters will be removed
		# in LCS add the charecters present in Y
        dp = [[0]*(n+1) for i in range(m+1)]
        # in 0th row and 0th column No common subsecuence can be so 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        
        lenOfLCS = dp[-1][-1]
        numberOfDeletion = len(X) - lenOfLCS
        numberOfInsertion = len(Y) - lenOfLCS
        
        totalSteps = numberOfDeletion + numberOfInsertion
        
        return totalSteps