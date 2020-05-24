class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        self.dot_prods = []
        self.delete(nums1, nums2)
        return max(self.dot_prods)
        # return self.max_dot

    def delete(self, nums1, nums2):
        # print("n12", nums1, nums2)
        # dot_product = sum(map(lambda xy: xy[0] * xy[1], zip(nums1, nums2)))
        # print(dot_product, subnums2, subnums2, dot_product, len(subnums1), len(subnums2))
        # self.max_dot = max(self.max_dot, dot_product)
        # print(self.max_dot)
        for i in range(-1, len(nums1)):
            if i == -1:
                subnums1 = nums1
            else:
                subnums1 = nums1[:i] + nums1[i+1:]
            if len(subnums1) is 0:
                continue
            # print("s1", subnums1)

            for j in range(-1, len(nums2)):
                if j == -1:
                    subnums2 = nums2
                else:
                    subnums2 = nums2[:j] + nums2[j+1:]
                if len(subnums2) is 0:
                    continue
                # print(len(subnums1), len(subnums2), subnums1, subnums2)
                if len(subnums1) == len(subnums2):
                    dot_product = sum(map(lambda xy: xy[0] * xy[1], zip(subnums1, subnums2)))
                    # print(dot_product, subnums2, subnums2, dot_product, len(subnums1), len(subnums2))
                    # self.max_dot = max(self.max_dot, dot_product)
                    self.dot_prods.append(dot_product)
                if j != -1:
                    self.delete(subnums1, subnums2)

inputs = [
    [
        [2,1,-2,5], [3,0,-6]
    ],
    [[3,-2], [2,-6,7]],
    [[-1,-1],[1,1]],
    [
        [5,-4,-3],
[-4,-3,0,-4,2]
    ]
]
outputs = [
    18, 21, -1, 28
]

results = []
for (i, o) in zip(inputs, outputs):
    s = Solution()
    result = s.maxDotProduct(i[0], i[1])
    print(result)
    print(result == o)
    results.append((result == o, result))

print("all")
print(results)


# class S:
#     max_dot = float('-inf')
#     def cal_max(self, nums1, nums2):
#         self.delete(nums1, nums2)
#         return self.max_dot

#     def delete(self, nums1, nums2):
#         nums1_length = len(nums1)
#         for i in range(1, len(nums1)):
#             subnums1 = nums1[:i] + nums1[i+1:]
#             for j in range(1, len(nums2)):
#                 subnums2 = nums2[:j] + nums2[j+1:]
#                 if len(subnums1) == len(subnums2):
#                     dot_product = sum(map(lambda xy: xy[0] * xy[1], zip(subnums1, subnums2)))
#                     print(dot_product, subnums2, subnums2, dot_product, len(subnums1), len(subnums2))

#                     self.max_dot = max(self.max_dot, dot_product)
#                 self.delete(subnums1, subnums2)
# nums1 = [2, -6, 7, 8, 9]
# nums2 = [2, -6, 7, 8, 9]
# length = 2

# s = S()
# print(s.cal_max(nums1, nums2))