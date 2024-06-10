import emoji

# Sample text with emojis
text = input("Enter text with emoji to demojize the sentence : ")

text_without_emoji = emoji.demojize(text)

print(text_without_emoji)