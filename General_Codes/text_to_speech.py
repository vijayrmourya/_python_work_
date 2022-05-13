import pyttsx3
import PyPDF2

pdf_file = "G:\__Entire_Github__\__Languages\Python\py_ignore_course_data\Data_structure_Udemy_competency" \
           "\Data_Structure_&_Algorithm_The_Complete_Masterclass\Visualizing_Algorithm\Why+algorithm+execution+time" \
           "+is+different+for+every+time_.pdf "

obj = open(pdf_file, 'rb')
pdfread = PyPDF2.PdfFileReader(obj)
page_no = pdfread.numPages

play = pyttsx3.init()

for num in range(0, page_no):
    page = pdfread.getPage(num)
    data = page.extractText()
    print(data)
    print(play.say(data))
    play.runAndWait()
