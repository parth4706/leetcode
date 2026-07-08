class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        time = 0
        wait = 0
        n = len(customers)
        for i in range(n):
            if time > customers[i][0]:
                wait += (time - customers[i][0])
            elif time < customers[i][0]:
                time = customers[i][0]
            wait += customers[i][1]
            time += customers[i][1]



        return float(wait)/float(n)
