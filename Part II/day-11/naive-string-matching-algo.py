'''
Pseudocode:
naive_string_matcher(text, pattern):
n = text.length
m = pattern.length

for s in range (n - m)
    if pattern[1..m] == text[s + 1 .. s + m]
        print "Pattern occurs with shift"  s

'''

text1 = "acaabc"
pattern1 = "aab"

text2 = "000010001010001"
pattern2 = "0001"


def naive_string_matcher(text, pattern):
  """Find pattern in text."""
  n = len(text)
  m = len(pattern)

  for s in range(n):
    if pattern == text[s:s + m]:
      return "Pattern occurs with shift {}".format(s)
    
      
def naive_string_counter(text, pattern):
  """Find pattern in text."""
  n = len(text)
  m = len(pattern)
  counter = 0

  for s in range(n):
    if pattern == text[s:s + m]:
      counter += 1

  return "Pattern '{}' occured {} times in the text '{}'".format(pattern, counter, text)
   


print(naive_string_matcher(text1, pattern1))
print(naive_string_matcher(text2, pattern2))

print(naive_string_counter(text2, pattern2))
