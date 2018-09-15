symbols = ["-", "=", "_", "\"", "?", "!", "."]
user_phrase = input()
for symbol in symbols:
    user_phrase = user_phrase.replace(symbol,"")
user_phrase = user_phrase.strip().split(" ")
user_phrase = user_phrase[1:]

if user_phrase:
    count_words = len(user_phrase)
    if count_words == 1:
        reply_wordcount = "В вашей фразе {} слово.".format(count_words)
    if count_words > 1 < 4:
        reply_wordcount = "В вашей фразе {} слова.".format(count_words)
    if count_words >= 5: 
        reply_wordcount = 'В вашей фразе {} слов.'.format(count_words)

else:
    reply_wordcount = "Почему ничего нет?"

print(reply_wordcount)