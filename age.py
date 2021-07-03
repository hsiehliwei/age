driving = input('請問有開過車嗎?')
if driving != '有' and driving != '沒有':
    print('你只能回答有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('很好!開車帶我去玩')
    else:
        print('可惜!你未成年不能開車')
elif driving == '沒有':
    if age >= 18:
        print('幾歲了還不去考駕照....')
    else:
        print('之後考到駕照就可以開車拉')


