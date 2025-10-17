class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        self.tokens = text.split()


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.word_count = len(self.tokens)


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        super().__init__(text)
        self.vocab = set(self.tokens)


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        super().__init__(text)


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)
