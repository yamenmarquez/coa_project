import os
from reportlab.pdfgen import canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import inch, cm
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
stylesheet=getSampleStyleSheet()


# Ruta donde se guaradaran los archivos
saved_coa_path = ".coas_por_enviar" + os.sep

# Ruta de donde se lee la BBD de excell y la plantilla pdf
files_path = "files" + os.sep

# Nombre del archivo pdf que se utiliza como plantilla
pdf_template_file_name = 'template_sh_fases.pdf'

# Se inicializa la variable inch la cual se utiliza para los calculo de posicionamiento del texto en el pdf cambas
inch = 72

width, height = A4


created_pdf_name = saved_coa_path + 'referencia' + 'lote' + '.pdf'
c = canvas.Canvas(created_pdf_name)
template = PdfReader(files_path + pdf_template_file_name, decompress=False).pages
t = pagexobj(template[0])
c.doForm(makerl(c, t))
c.setFillColor(colors.blue)
c.drawString(1.8*inch, 8.92*inch, 'Quala')
c.drawString(2.42*inch, 8.72*inch, 'COA-No-1111')
c.drawString(2.06*inch, 8.51*inch, 'Shampoo Colageno 550 ml')
c.drawString(1.60*inch, 8.32*inch, '0199')
c.drawString(2.84*inch, 8.12*inch, '2018-05-29')
c.drawString(2.75*inch, 7.92*inch, '2020-05-29')
c.drawString(2.50*inch, 7.71*inch, '100')
c.drawString(2.60*inch, 7.52*inch, '12')
c.drawString(2.58*inch, 7.31*inch, '1200')
 
# doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# container for the 'Flowable' objects
# elements = []

aspecto = Paragraph('''
                    MEZCLA HOMOGÉNEA PERLADA SIN PARTÍCULAS EN SUSPENSIÓN O GRUMOS''',
                    stylesheet["BodyText"])
 
data= [['Descripción', 'Especificación', 'Resultado'],
       ['Aspecto', aspecto, 'Cumple'],
       ['Color', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple'],
       ['Olor', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple'],
       ['pH', '5,75-6,25', '6,0'],
       ['Viscosidad (cP)', '13000-17000','15690'],
       ['Peso Neto (g)', '545,00-555,00', '550'],
       ['Separación de fases', 'AUSENCIA', 'Cumple'],
       ['Atributos de Calidad', 'SEGÚN ANEXO 04 – ACUERDO DE CALIDAD', 'Cumple']]
t=Table(data, colWidths=[1.65*inch, 3.37*inch, 1.06*inch])
t.setStyle(TableStyle([('INNERGRID',(0,0),(-1,-1), 0.25, colors.black),
                       ('BOX',(0,0),(-1,-1), 0.25, colors.black),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.black)]))
# elements.append(t)
# # write the document to disk
# doc.build(elements)
t.wrapOn(c, width, height)
t.drawOn(c, 1.11*inch, 4.76*inch)

c.showPage()
c.save()