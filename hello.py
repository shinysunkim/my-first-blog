print('Hello, Django Girls!')

if 3 > 2:
    print ('It is true')
else:
    print ('It is false')

name = "Sun"
if name == "Ola":
    print("Hey Ola")
    # 이름이 Ola일 때
elif name == "Sonja":
    print("Hey Sonja")
    # 함수가 여러 줄일 떄
    """
    이름이 Sonja일 경우
    이름이 Sonja일 경우
    """
else:
    print("Hey Anonymous")

# 함수를 정의할 때
def hi(player):
    print("Hi "+player)
    print("How are you?")
# 함수를 불러 올 때
hi("sun")
hi("tom")
hi("sarah")

friends = ["anne", "judy", "june"]
for friends_name in friends:
    hi(friends_name)
