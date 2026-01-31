# 终端猜数字
import random

print("=========================================")
print("欢迎来到猜数字游戏")
print("=========================================")

def play_game():
    """启动猜数字游戏的主要逻辑"""
    # 获取用户输入的范围值并转换为整数
    start_num = int(input("起始数为："))
    end_num = int(input("终止数为："))

    # 生成指定范围内的随机整数
    exact_num = random.randint(start_num, end_num)

    print("===========Game Start!===================")

    # 获取用户猜测的数字并转换为整数
    guess_num = int(input("你猜的数是："))

    # 循环直到猜中数字
    while guess_num != exact_num:
        if guess_num < exact_num:
            print("猜小了")
        elif guess_num > exact_num:
            print("猜大了")
        
        # 重新获取用户的猜测
        guess_num = int(input("你猜的数是："))

    print("猜对了！答案是", exact_num)


def main():
    """主程序入口点，处理游戏循环和用户选择"""
    # 先运行一次游戏
    play_game()

    # 询问是否继续游戏
    while True:
        print("继续游戏？(Y/n)")
        choice = input().strip().lower()
        
        if choice == "y" or choice == "":
            print("-----------New Game-------------------")
            play_game()
        else:
            break

    print("================Game Over================")


if __name__ == "__main__":
    main()