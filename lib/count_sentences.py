#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
        if type(value) != str:
            print("The value must be a string.")
            raise ValueError("The value must be a string.")
        self.value = value

  def is_sentence(self):
        return self.value.endswith(".")

  def is_question(self):
        return self.value.endswith("?")

  def is_exclamation(self):
        return self.value.endswith("!")

  def count_sentences(self):
        sentence_endings = ['.', '?', '!']
        return sum(self.value.endswith(ending) for ending in sentence_endings)


# Example usage:
# string = MyString()
# string.value = "This is a string! It has three sentences. Right?"
# print(string.count_sentences())  # Output: 3