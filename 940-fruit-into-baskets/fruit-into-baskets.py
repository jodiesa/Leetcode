class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        #brute force approach (one byb one search, index 1,2,3 e.g if [0] is apple but i[3] is grpae, need to restart from i[1]) o(n square) time complexity.
        #effcient solution 1st pointer will search one by one , when there is a 3rd identified fruit, 2nd pointer will remove fruits in the basket until it can add the 3rd fruit type in basket, 2nd pointer wi;ll stop at i[2] and 1st pointer will continue until new fruit type o(n)
    
        basket = {}          # like HashMap<Integer, Integer>
        left = 0
        maxFruits = 0

        for right in range(len(fruits)):
            # Add current fruit to basket
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # If basket has more than 2 types, shrink window
            while len(basket) > 2:
                fruit_count = basket[fruits[left]]
                if fruit_count == 1:
                    del basket[fruits[left]]
                else:
                    basket[fruits[left]] = fruit_count - 1
                left += 1

            # Update max window size
            maxFruits = max(maxFruits, right - left + 1)

        return maxFruits
