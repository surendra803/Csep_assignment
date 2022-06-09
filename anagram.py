def check(s1,s2):
	if(sorted(s1)==sorted(s2)):
		print("The string is anagrams.")
	else:
		print("The string aren't anagrams.")
s1="listen"
s2="silent"
check(s1,s2)
