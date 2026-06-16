func topKFrequent(nums []int, k int) []int {
    count := make(map[int]int)
    for _, num := range nums {
        count[num]++
    }

    freq := make([][2]int, 0, len(count))
    for num, cnt := range count {
        freq = append(freq, [2]int{cnt, num})
    }
    sort.Slice(freq, func(i, j int) bool {
        return freq[i][0] > freq[j][0]
    })

    res := make([]int, k)
    for i := 0; i < k; i++ {
        res[i] = freq[i][1]
    }
    return res
}
