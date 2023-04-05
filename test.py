import googletrans
from googletrans import Translator

translator = Translator()
# dictionary = googletrans.LANGUAGES
# for i in dictionary:
#     print(i,dictionary.get(i))

english = "Subscribe to my channel"
# spanish = "Suscríbete a mi canal"
# german = "Abonnieren Sie meinen Kanal"

# print(translator.detect(english))
# # print(translator.detect(spanish))
# # print(translator.detect(german))
# # print(translator.translate(text=spanish))
# test = translator.translate(text=spanish,dest="en")
print(translator.translate(text=english,src='en',dest='hi').text)
# print(test.text)

languages_dict = {"en":"English","bn": "Bengali", 
                  "gu":"Gujarati", "hi": "Hindi",
                  "kn": "Kannada", "ml": "Malayalam",
                  "mr": "Marathi", "pa": "Punjabi",
                  "ta": "Tamil",  "te": "Telugu",
                  "ur" :"Urdu"}
# print(languages_dict)
# Value = list(languages_dict.values())[0]
# print(Value)
# def get_keys_from_values(Values,languages_dict):
#     return [k for k, v in languages_dict.items() if v==Values][0]
# print(get_keys_from_values(Value,languages_dict))
# print(languages_dict["en"])