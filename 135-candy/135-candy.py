class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        
        print(left)
        print(right)
                
        sum_ = 0
        for m in range(len(left)):
            sum_ += max(left[m], right[m])
        
        return sum_
        

        
        
        
        
        # candies = [1]*len(ratings)
        # bool_ = True
        # while (bool_):
        #     bool_ = False
        #     for i in range(len(ratings)):
        #         if i != len(ratings)-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
        #             candies[i] = candies[i+1] + 1
        #             bool_ = True
        #         if i > 0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
        #             candies[i] = candies[i-1] + 1
        #             bool_ = True
        # print(candies)          
        # return sum(candies)