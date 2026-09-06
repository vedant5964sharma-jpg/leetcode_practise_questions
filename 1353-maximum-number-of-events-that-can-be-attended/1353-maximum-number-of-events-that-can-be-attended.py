import heapq

class Solution(object):
    def maxEvents(self, events):
        events.sort()

        heap = []
        day = 0
        i = 0
        count = 0

        while i < len(events) or heap:

            # If no event is available, jump to next event
            if not heap:
                day = events[i][0]

            # Add all events starting today
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove expired events
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # Attend event ending earliest
            if heap:
                heapq.heappop(heap)
                count += 1
                day += 1

        return count