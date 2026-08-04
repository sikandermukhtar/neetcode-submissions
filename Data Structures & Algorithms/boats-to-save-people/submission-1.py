class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_count = 0
        l, r = 0, len(people) - 1
        while l <= r:

            if l == r:
                boat_count += 1
                break

            weight_sum = people[l] + people[r]
            if weight_sum > limit:
                r -= 1
                boat_count += 1
                # print("Sum Greater boat count:", boat_count)
            elif weight_sum < limit:
                boat_count += 1
                # print("Sum Lesser boat count:", boat_count)
                l += 1
                r -= 1
            else:
                boat_count += 1
                # print("Equal boat count:", boat_count)
                l += 1
                r -= 1
        return boat_count
