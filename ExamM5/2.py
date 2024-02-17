import pdfkit
import threading
import shutil 
import os 


def convert_to_pdf(url , pdf_faylnomi , config) :
    pdfkit.from_url(url, pdf_faylnomi , configuration=config)

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

threads = []

folder_name  =  r'C:\Users\queue\OneDrive\Desktop\exam\paronimlar'  # Qavsli qo'llash belgisi bilan yozilgan yo'l
if not os.path.exists(folder_name):  # Papka mavjud emasligini tekshirish
    os.makedirs(folder_name)  # Papkani yaratish

for i in range(1, 11):
    url = 'https://tilshunos.com/paronims/?page=' + str(1)
    pdf_filename = str(i) + '.pdf'
    t = threading.Thread(target=convert_to_pdf ,  args=(url, pdf_filename , config))
    threads.append(t)
    t.start()

    # PDF faylini hozircha ko'chirmaymiz, chunki uni yaratish operatsiyasi hali bajarilmagan
    # shutil.move(pdf_filename, os.path.join(folder_name, pdf_filename))

for t in threads: 
    t.join()
