# Look up the hash for the word "cause"
cause_hash = nlp.vocab.strings['cause']
print(cause_hash)

# Look up the cause_hash to get the string
cause_string = nlp.vocab.strings[cause_hash]
print(cause_string)