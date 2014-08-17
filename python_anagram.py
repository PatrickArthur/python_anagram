def reverse(string):
  reverse = []
  reverse.append(string[::-1])
  sort='\n'.join(reverse)
  if sort == string:
    print "Anagram"
  else:
    print "Not Anagram"


reverse("joe")

