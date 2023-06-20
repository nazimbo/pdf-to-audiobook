# importing the modules
import PyPDF2
import pyttsx3
from resemble import Resemble

Resemble.api_key('YOUR_API_TOKEN')

# path of the PDF file
path = open('dive-into-design-patterns-fr-demo.pdf', 'rb')

# creating a PdfReader object
pdfReader = PyPDF2.PdfReader(path)

# the page with which you want to start
from_page = pdfReader.pages[2]

# extracting the text from the PDF
text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
