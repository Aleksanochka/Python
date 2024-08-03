Twice_members = {'Jihyo': 1997, 'Nayeon ': 1995, 'Jeongyeon': 1996,
           'Momo': 1996, 'Sana': 1996, 'Mina': 1997,
           'Dahyun': 1998, 'Rose': 'Rose is not a Twice member'}
print(Twice_members,
      f"Jihyo's year of birth: {Twice_members['Jihyo']}",
      f"Only 7 girls? {Twice_members.get('Chaeyoung', ' And where are the others?')}", sep='\n')

Twice_members.update({'Chaeyoung': 1999, 'Tzuyu ': 1999})
print(Twice_members.pop('Rose'))
print('full band: ', *[item for item in Twice_members.items()], sep='\n')

my_set = {'Rose', 'Rose', 'Rose', 1997, ("On the Ground", 2021)}
print("My set:", my_set)

my_set.update({'rosie is roses', ("Hard to Love", 2022)})
my_set.remove(1997)
print('Modified set:', my_set)
