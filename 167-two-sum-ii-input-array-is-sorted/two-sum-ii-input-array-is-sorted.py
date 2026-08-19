class Solution(object):
    def twoSum(self, numbers, target):
        if numbers.count(target/2)>=2:
            out = []
            out.append(numbers.index(target/2)+1)
            out.append(numbers.index(target/2)+2)
            return out
        test = list(set(numbers))
        test.sort()
        output = []
        for i in test:
            for el in test:
                if i+el==target and i!=el:
                    output.append(numbers.index(i)+1)
                    output.append(numbers.index(el)+1)
                    return output