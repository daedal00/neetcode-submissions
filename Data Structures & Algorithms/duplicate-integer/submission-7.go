func hasDuplicate(nums []int) bool {
    ans := make(map[int]struct{}, len(nums))
    for _, num := range nums{
        if _, ok := ans[num]; ok {
            return true
        }
        ans[num] = struct{}{}
    }
    return false
}
