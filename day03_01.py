# # print("I'm a boy")
# #
# # # army = '''우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.
# # #        하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'''
# #
# # army = '우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\t하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'
# # print(army)
#
# # start = 'Na ' * 4 + '\n'
# # middle = 'hey ' * 3 + '\n'
# # end = '안녕.'
# # print(start + start + middle  + end)
# #
# # univ = 'inha university'
# # print(univ[5:])
# # print(univ[5:15])
# # print(univ[-10:])
# # print(univ[::2])
# # print(univ[5:-6])
# # print(univ[-10:-6])
# #
# # print(len(univ))
# # print(univ.split())
# # print(univ.split('i'))
# #
# # pokemons_list = ['피카츄', '꼬부기', '이상해', '파이리']
# # pokemons_string = ', '.join(pokemons_list)
# # print(pokemons_string)
# # pokemons_st = '\n'.join(pokemons_list)
# # print(pokemons_st)
# #
# # inha = 'a duck goes into a sea'
# # print(inha.replace('a', 'a nice'))
# # print(inha.replace('a ', 'a nice'))
# # print(inha.replace('a ', 'a nice '))
# #
# # subjects = ' python, data structure, database  '
# # print(subjects.strip())
# # blurt = "what the...!!?"
# # print(blurt.strip('.?!')
# # subjects = ' python, data structure, database  '
# # print(subjects.find('data'), subjects.index('data'))
# # print(subjects.find('inha')) #-1 return)
# # print(subjects.index('inha')) #exception!
#
# song = """when an eel grabs your arm,
# And it causes great harm,
# That's - a moray!"""
# # song = song.replace('m', 'M')
# # print(song)
# # idx = song.rfind('m')
# # song = song.replace(song[idx], song[idx].upper())
# # print(song.endswith('Moray!'))
#
# song_list = song.split()
# print(song_list)
# song_list[14] = song_list[14].title()
# song_string = ''.join(song_list)
# print(song_string)

#while
# while True:
#     dan = int(input('Dan (0 to quit): '))
#     if dan == 0: #exit
#         break
#     if 1 < dan < 10: #if dan >= 2 and <=9:
#         i = 1
#         while i < 10:
#             print('{0} * {1} = {2}'.format(dan, i, dan * i))
#             i = i + 1
#         break
#     else:
#         print('2에서 9사이의 값을 입력 하세요')
#
# while True:
#     dan = int(input('Dan (0 to quit): '))
#     if dan == 0: #exit
#         break
#     if 1 < dan < 10: #if dan >= 2 and <=9:
#         for i in range(1, 10, 2):
#             while i < 10:
#                 print('{0} * {1} = {2}'.format(dan, i, dan * i))
#             break
#         else:
#             print('2에서 9사이의 값을 입력 하세요')


number = int(input("정수 입력 : "))
is_prime = True

# k = 1
# while k <= number:
#     if number % k == 0:
#         counts = counts + 1
#     k = k + 1
# if counts == 2:
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is NOT prime number!')
for k in range(2, number):
    if number % k == 0:
            is_prime = False
            break
    print(k)

if is_prime: #0이 아니면
    print(f'{number} is prime number!')
else:
    print(f'{number} is not prime number!')



