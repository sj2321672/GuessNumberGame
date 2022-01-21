# 猜數字遊戲
import random

# 正確答案
ans = random.randint(1, 100)

# 答案範圍
minNum = 1
maxNum = 100

# 判斷遊戲是否結束
gameOver = True

print("猜數字遊戲，範圍在", minNum, "~", maxNum, "之間")

while gameOver:
    # 輸入答案
    num = int(input("請輸入數字："))

    # 如果輸入的數字不在範圍內
    if num <= minNum or num >= maxNum:
        print("請輸入範圍內的數")
        print("範圍在", minNum, "~", maxNum, "之間")

    # 如果正確答案比輸入的數字大
    elif ans > num:
        minNum = num
        print("範圍在", minNum, "~", maxNum, "之間")

    # 如果正確答案比輸入的數字小
    elif ans < num:
        maxNum = num
        print("範圍在", minNum, "~", maxNum, "之間")

    # 猜對正確答案
    else:
        gameOver = False
# 遊戲結束
print("猜對了！遊戲結束。")
