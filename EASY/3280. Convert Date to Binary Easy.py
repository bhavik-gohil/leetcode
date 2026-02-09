class Solution:
    def to_binary(self, n):
        bin_str = ""
        while n != 0:
            if n % 2 == 0:
                bin_str = "0"+bin_str
            else:
                bin_str = "1"+bin_str

            n = n//2
        return bin_str

    def convertDateToBinary(self, date: str) -> str:
        [x, y, z] = date.split("-")
        return f"{self.to_binary(int(x))}-{self.to_binary(int(y))}-{self.to_binary(int(z))}"


i = Solution()
call = i.convertDateToBinary("2080-02-29")
print("-::", call)
