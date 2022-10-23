album = [("Welcome to my nightmare", "Alice Cooper", 1975),
         ("Bad company", "Bad company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Riding the Lighting", "Metallica", 1984),
         ]
print(len(album))
for name, artist, year in album:
    print("Album: {}, Artist: {},Year: {}"
          .format(name, artist, year))
