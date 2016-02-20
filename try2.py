import nltk
# input_sentence = "Boycott all Apple products  until such time as Apple gives cellphone info to authorities regarding radical Islamic terrorist couple from Cal"
# text = nltk.word_tokenize(input_sentence)
# list_of_tokens = nltk.pos_tag(text)

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+|[^\w\s]+')

content_text = 'Boycott all Apple products until such time as Apple gives cellphone info to authorities regarding radical Islamic terrorist couple from Cal'
tokenized_content = tokenizer.tokenize(content_text)
content_model = nltk.NgramModel(3, tokenized_content)

starting_words = content_model.generate(100)[-2:]
content = content_model.generate(words_to_generate, starting_words)
print ' '.join(content)
