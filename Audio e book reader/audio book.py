import pypdf
from gtts import gTTS
class convert_pdf_audio:
    def __init__(self,filepath,audiopath):
        self.filepath = filepath
        self.audiopath = audiopath
    def Extract_text(self):

        pdf_file = open(self.filepath, 'rb')
       
        pdf_reader = pypdf.PdfReader(self.filepath)
      
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
    
            text += page.extract_text()
        pdf_file.close()
        return text


    def text_to_audio(self,text):
     
        tts = gTTS(text=text, lang='en')
        tts.save(self.audiopath)


    def pdf_audio(self):
        text = self.Extract_text()
      
        if text.strip():
            self.text_to_audio(text)
            print("Audio file saved at: {}".format(self.audiopath))
        else:
            print("No text found in the PDF.")

obj = convert_pdf_audio('file_name and path','audio.mp3')
obj.pdf_audio()