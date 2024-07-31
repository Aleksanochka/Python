immutable_var = 'hi', 1, (1, 1, 'my'), ['name is', 'Usagi Tsukino']
print(immutable_var)

# immutable_var[-1] = ('name is', 'Usagi Tsukino') ошибка при попытке изменить элемент кортежа
# immutable_var[-1] = ('name is', 'Usagi Tsukino')
#     ~~~~~~~~~~~~~^^^^
# TypeError: 'tuple' object does not support item assignment

immutable_var[-1][1] = 'Rey Hino'  # можно изменить список внутри кортежа
print(immutable_var[-2][2], immutable_var[-1])

mutable_list = ['my favourite name is ', 'Milana']
mutable_list[1] = 'Aleksandra'
print(mutable_list)
