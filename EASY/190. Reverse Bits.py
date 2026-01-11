from decimal import Decimal


class Solution:
    # def get_binary(self, decimal):
    #     remainder_str = ""
    #     flag = True
    #     while flag:
    #         if decimal % 2 == 0:
    #             remainder_str = "0"+remainder_str
    #             decimal = decimal//2
    #         else:
    #             remainder_str = "1"+remainder_str
    #             decimal = (decimal-1)//2
    #         if decimal == 0:
    #             flag = False
    #     return remainder_str

    # def get_decimal(self, binary_str):
    #     ln = len(binary_str)
    #     i = 0
    #     place = 0
    #     sum = 0
    #     while i < ln:
    #         sum = sum + int(Decimal(int(binary_str[i]) * (2 ** place)))
    #         place += 1
    #         i += 1
    #     return int(sum)

    # def reverseBits(self, n: int) -> int:
    #     bits = self.get_binary(n)
    #     ln = len(bits)
    #     decimal = self.get_decimal("0"*(32-ln)+bits)
    #     return decimal

    # def reverseBits(self, n: int) -> int:
    #     bit_str = ""
    #     while n != 0:
    #         bit = n % 2
    #         bit_str = str(bit)+bit_str
    #         n = (n-bit)//2

    #     bit_str = "0"*(32-len(bit_str))+bit_str
    #     new_decimal = 0
    #     place = 0
    #     while place < 32:
    #         new_decimal += int(bit_str[place]) * pow(2, place)
    #         place += 1

    #     return new_decimal

    def reverseBits(self, n: int) -> int:
        place = 31
        new_decimal = 0

        while place > 0:
            bit = n % 2
            n = n >> 1
            new_decimal += bit * pow(2, place)
            place -= 1
            
        return new_decimal


i = Solution()
call = i.reverseBits(43261596)
print(":: ", call)

