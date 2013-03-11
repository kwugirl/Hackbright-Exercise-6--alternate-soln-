f = open('testing.txt')
#opens only open txt file
string_text = f.read().lower()
#read coverts txt file to string all lower case
f.close()

split_text = string_text.split(' ')
#splits string into list

word_dict = {}
#declaring the dict
 
for index in range(len(split_text)):
	# loop over range of the length of list split_text
	word = split_text[index]
	split_text[index] = word.strip('.')
	#reassigning the striped word back into split_text[index]
	 		
for word in split_text:
#loop through split_text
	if word in word_dict:
	# what does this if statement do? Asks, is this word already in the dict?
		word_dict[word]	+= 1
		#counting the words in split test 
	else:
	# when do you get into this else section? if unique word, add key to dict
		word_dict[word] = 1 
		#if there is only 1 word add it to dict




sort_num = []
for k, v in word_dict.iteritems():
# print the dict line by line	
	both_vals =  -v, k
	sort_num.append(both_vals)
	# print key, value

sort_num.sort()
print type(sort_num)
print type(sort_num[0])
# for pairs in sort_num:
# 	print type(pairs)
# 	print sort_num

for index in range(len(sort_num)):
#for index in the range of length of list sort_num	
	sort_num[index] = sort_num[index][1], -sort_num[index][0]
#in sort_num[index], change negative nums to positive and flipping #'s and words

print sort_num

for item in sort_num:
#printing tuples 
	print item
