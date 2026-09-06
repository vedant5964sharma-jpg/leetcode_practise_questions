class Solution(object):
    def findLongestChain(self, pairs):
        # Sort pairs by ending value
        pairs.sort(key=lambda x: x[1])

        count = 0
        last = float('-inf')

        # Select pair if its start is greater than
        # the ending value of previous pair
        for start, end in pairs:
            if start > last:
                count += 1
                last = end

        return count