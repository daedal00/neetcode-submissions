func groupAnagrams(strs []string) [][]string {
    res := make(map[[26]int][]string)
    for _, s := range strs{
        ordMap := [26]int{}
        for _, char := range s {
            ordMap[char-'a']++
        }
        res[ordMap] = append(res[ordMap], s)
    }
    resList := make([][]string, 0)
    for _, val := range res {
        resList = append(resList, val)
        }
    return resList
}
