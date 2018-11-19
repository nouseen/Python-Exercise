class Solution(object):

    index = 0;

    def twoSum(self, nums, target):

        positionMap = {};
        for index,nowNumber in enumerate(nums) :
            #首先判断是否有对位数据，如果有，则直接返回
            number = target - nowNumber
            if number in positionMap:
                return positionMap[number ],index;

            #否则，标记位置
            positionMap[nowNumber] =index;


nums = [-3,4,3,90];
solution = Solution();
returnValue = solution.twoSum(nums,0);
print(returnValue)