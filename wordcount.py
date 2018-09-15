user_phrase = input()

if user_phrase.strip():
    user_phrase = user_phrase.split(" ")
    user_phrase = user_phrase[1:]
    count_words = len(user_phrase)

    reply_wordcount = 'В вашей фразе {} слов(а).'.format(count_words)

else:
    reply_wordcount = "Почему ничего нет?"
    
print(reply_wordcount)