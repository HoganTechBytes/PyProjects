import sys, random

print('Welcome to the "Psych" Sidekick Name Generator.')

first = ('Baby oil', 'Bad News', 'Big Burps',
         'Bill "Beenie-Weenie"', 'Bob "Stinkbug"',
         'Bowel Noises', 'Boxelder', 'Bud "Lite"',
         'Butterbean', 'Buttermilk', 'Buttocks',
         'Chad', 'Chesterfield', 'Chewy', 'Cinnabuns',
         'Cleet', 'Cornbread', 'Crab Meat', 'Crapps',
         'Dark Skies', 'Dennis Clawhammer', 'Dicman',
         'Elphonso', 'Fancypants', 'Figgs', 'Foncy',
         'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy',
         'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
         'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
         'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks',
         'Old Scratch', 'Ovaltine', 'Pennywhistle', '"Pitchfork" Ben',
         'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo',
         'Scratchensniff', 'Scut', 'Sid "The Squirts"',
         'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki',
         'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
         'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
         'Winston "Jazz Hands"', 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

repeats = True

while repeats:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print(f'Your "Psych" Sidekick name is: {firstName} {lastName}')

    newName = input("Pick another name? (y/n): ")
    if newName.lower() in ["n", "no"]:
        repeats = False
    