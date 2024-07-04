class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Using the setter to ensure validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re
        # Split the value based on sentence-ending punctuation and filter out empty strings
        sentences = re.split(r'[.!?]', self._value)
        non_empty_sentences = [s for s in sentences if s.strip()]
        return len(non_empty_sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  # => 3

# Check other methods
print(string.is_sentence())  # => False
print(string.is_question())  # => True
print(string.is_exclamation())  # => False


