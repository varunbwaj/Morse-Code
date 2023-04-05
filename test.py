import googletrans
from googletrans import Translator

translator = Translator()
dictionary = googletrans.LANGUAGES
for i in dictionary:
    print(i,dictionary.get(i))

# english = "Subscribe to my channel"
# spanish = "Suscríbete a mi canal"
# german = "Abonnieren Sie meinen Kanal"

# # print(translator.detect(english))
# # print(translator.detect(spanish))
# # print(translator.detect(german))
# # print(translator.translate(text=spanish))
# test = translator.translate(text=spanish,dest="en")
# print(test.text)