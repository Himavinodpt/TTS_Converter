from gtts import gTTS
import os
text="today is a good day"
output=gTTS(text=text,lang='en',slow=False)
output.save('output.mp3')
os.system('mpg123 output.mp3')
