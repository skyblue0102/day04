#list
big_bang = ['GD', '태양', '탑', '대성', '승리']
exo = ['백현', '첸']
# big_bang.append('인하')
big_bang.insert(1, '인하')
# print(big_bang*3)
# exo.extend(big_bang)
# exo += big_bang
exo.append(big_bang)
print(exo)
print(exo[2][2])  # 태양
print(exo[-1][-4])

exo[-2] = '시우민'
print(exo)
# print(exo.pop()) #빅뱅 pop
print(exo[2].pop()) #빅뱅 pop
print(exo)
print(exo[2].pop(-2)) #빅뱅 pop
print(exo)
del exo[2][-1] #대성 삭제
print(exo)
# exo.remove('인하')  (작동안됨)
# print(exo)
exo[2].remove('인하')
print(exo)

# scores = ('B+', 'A+', 'C+')
# print(scores[1], scores[2])
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores[1], scores[2])


