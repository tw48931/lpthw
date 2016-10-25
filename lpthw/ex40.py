class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

lyrics1 = ["Happy birthday to you",
		   "I don't want to get sued",
		   "So I'll stop right there"]	

lyrics2 = ["They rally around the family",
		   "With pockets full of shells"]	

User_song = int(raw_input("Please enter the number of song that you like:"))

if User_song == 1:
	happy_bday = Song(lyrics1)
	happy_bday.sing_me_a_song()
elif User_song == 2:					
	bulls_on_parade = Song(lyrics2)
	bulls_on_parade.sing_me_a_song()
else:
	print "We don't have this song!"

