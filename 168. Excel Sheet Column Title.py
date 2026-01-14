import math


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col_str = ""
        while columnNumber >= 1:
            columnNumber -= 1
            place = columnNumber % 26
            col_str = chr(64+place+1) + col_str
            columnNumber = math.floor(columnNumber/26)
            print(place, columnNumber)

            # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
            # 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6

        return col_str


i = Solution()
# call = i.convertToTitle(2147483647)
# call = i.convertToTitle(701)
call = i.convertToTitle(52)
print(":: ", call)


# # 1 A
# # 2 B
# # 26 Z

# # 27 AA
# # 28 AB

# 701 ZY
# 701/26
# 26.96153846153846 = 26 = Z, 0.96153846153846

# if XXX < 1 and XXX > 0
# xxx = 0.96153846153846 * 26 = 26 ceil

# s = ""

# 701/26 = 26.96153846153846 = columnNumber
# if columnNumber > 26
#     s += floor(columnNumber)
#     columnNumber = 0.96153846153846*26 = 24.99999999999996 = 25

# columnNumber = columnNumber / 26

# if columnNumber > 26:
#     col_str += chr(64+math.floor(columnNumber))

#     if math.floor(columnNumber) <= 26:
#         columnNumber = math.ceil((columnNumber-1)*26)
#         col_str += chr(64+columnNumber)

#     columnNumber = columnNumber / 26


# else:
#     col_str += chr(64+math.floor(columnNumber))
