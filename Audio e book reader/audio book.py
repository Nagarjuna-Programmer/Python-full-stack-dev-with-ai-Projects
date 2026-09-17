from pypdf import PdfReader
reader=PdfReader("abstract1 pdf2.pdf")
text=reader.pages[0].extract_text()


from gtts import gTTS
tts = gTTS(text=text, lang='en')
tts.save('ouput.mp3')