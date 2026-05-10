func twoSum(nums []int, target int) []int {
	res := make([]int, 0, 2)
    numMap := make(map[int]int)
	for i, n := range nums{
		compliment := target - n
		if _, ok := numMap[compliment]; ok {
			res = append(res, numMap[compliment], i)
			return res
		}
		numMap[n] = i
	}
	return res
}
