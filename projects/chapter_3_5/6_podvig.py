dict_words = [['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'], 
              ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 
'формулами', 'формулах'], 
              ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'], 
              ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'], 
              ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']]

class Morph:
    def __init__(self, *args) -> None:
        self._words = list(map(lambda x: x.strip(" .,!?;:").lower(), args))
        # self.words = words

    def add_word(self, word):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)

    def get_words(self):
        return tuple(self._words)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return other.lower() in self._words
    
    # def __req__(self, word) -> bool:
    #     return word.lower() in self.words
    

dict_words = [Morph(*i) for i in dict_words]
# text = input()
text = "Мы будем устанавливать связь завтра днем."
words = (i.strip(";:,.?!").lower() for i in text.split())
res = sum(word == morph for word in words for morph in dict_words)
print(res)