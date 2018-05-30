from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 
doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
data= [['Descripción', 'Especificación', 'Resultado'],
       ['Aspecto', 'MEZCLA HOMOGÉNEA PERLADA SIN PARTÍCULAS EN SUSPENSIÓN O GRUMOS', 'Cumple'],
       ['Color', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple'],
       ['Olor', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple']]
t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
                       ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
elements.append(t)
# write the document to disk
doc.build(elements)