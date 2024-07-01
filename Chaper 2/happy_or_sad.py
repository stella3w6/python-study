feeling = input()

happy_emoji = feeling.count(':-)')
sad_emoji = feeling.count(':-(')

if happy_emoji == 0 and sad_emoji == 0 :
	print('none')
elif happy_emoji > sad_emoji :
	print('happy')
elif sad_emoji > happy_emoji:
	print('sad')
else:
	print('unsure')