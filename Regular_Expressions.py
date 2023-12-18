# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Search the string to see if it starts with "The" and ends with "Spain"
import re
pattern= ("^The.*Spain$")
text= "The rain in Spain"
x= re.search(pattern, text)
print(x)

# Search how many times hello occur in the text

text= '''Hello is an interjection used to express emotion or feelings. It is most commonly used as a greeting when you meet someone or answer the phone.
The word hello is believed to have originated from the word hello or hello which were used as greetings in the past.
When Alexander Graham Bell invented the telephone, he wanted people to use the word "ahoy" as a greeting. However, his rival Thomas Edison suggested "hello", and the rest is history.
You might receive a random "hello" text message from someone'''

pattern= ("hello")

y= re.findall(pattern, text)
print(len(y))
print(y)

text= '''In the distant ocean, a powerful cyclone was forming, threatening to unleash its fury upon the coastline.
       Meanwhile, the brave scientist studied the cyclone's patterns, hoping to understand its nature. 
       As the storm intensified, the resilient sailors prepared for the challenges dyclone, anticyclone, 
       that lay ahead, knowing they would face the unpredictable elements of the cyclone. 
       The skyline painted a dramatic backdrop for this extraordinary battle between man and nature.'''

pattern= ("[a-z]+yclone")
z=re.findall(pattern, text)
print(len(z))
print(z)
pattern1= "p.....ns"
a= re.search(pattern1, text)
print(a)