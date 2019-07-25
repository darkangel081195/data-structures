letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
keys = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
         ".--","-..-","-.--","--.."]
dic = dict(list(zip(keys,letters)))
se = []
def morse_code(count,res,char,length):
	if count == (length - 1):
		if morse[char:] in dic:
			res = res + 1
		return res

	word = ''
	for i in range(char,len(morse)):
		word = word + morse[i]

		if word not in dic:
			continue
		else:
			count = count + 1
			res = morse_code(count,res,i+1,length)
			count = count - 1
	return res

word = input().strip()
# word='infy'
morse=''
for let in word:
	morse = morse + keys[ord(let)-ord('a')]

res = morse_code(0,0,0,len(word))


print(res)
