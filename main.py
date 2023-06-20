import PyPDF4
from gtts import *

# path of the PDF file
path = open('sample.pdf', 'rb')

# creating a PdfReader object
pdfReader = PyPDF4.PdfFileReader(path)

count = len(pdfReader.pages)  # counts number of pages in pdf file
text_list = []  # list to store text from pdf file

# extracting text from each page of pdf file
for i in range(count):
    try:
        page = pdfReader.getPage(i)
        text_list.append(page.extractText())
    except:
        pass

text = "\n".join(text_list)  # combining all text from text_list into one string
print(text)

# Set language
language = 'en'

try:
    # Call gTTS
    audio = gTTS(text=text, lang=language, slow=False)

    # Save as mp3 file
    audio.save("audio.mp3")
except:
    pass
