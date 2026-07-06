# this is not the correct approach
def wordPattern(pattern: str, s: str) -> bool:
    words=s.split()
    return (len(set(pattern))==len(set(words)))






# correct approach 

# def wordPattern(pattern: str, s: str) -> bool:
#     words = s.split()
    
#     if len(pattern) != len(words):
#         return False
        
#     char_to_word = {}
#     word_to_char = {}
    
#     for char, word in zip(pattern, words):
#         # Check if character is already mapped to a different word
#         if char in char_to_word and char_to_word[char] != word:
#             return False
#         # Check if word is already mapped to a different character
#         if word in word_to_char and word_to_char[word] != char:
#             return False
            
#         # Create the bidirectional links
#         char_to_word[char] = word
#         word_to_char[word] = char
        
#     return True
