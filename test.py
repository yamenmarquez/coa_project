from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 
doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
data= [['Descripción', 'Especificación', 'Resultado'],
       ['Aspecto', 'MEZCLA HOMOGÉNEA PERLADA' '\n' 'SIN PARTÍCULAS EN SUSPENSIÓN O GRUMOS', 'Cumple'],
       ['Color', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple'],
       ['Olor', 'SEGÚN MUESTRA DE REFERENCIA', 'Cumple'],
       ['pH', '5,75-6,25', '6,0'],
       ['Viscosidad (cP)', '13000-17000','15690'],
       ['Peso Neto (g)', '545,00-555,00', '550'],
       ['Separación de fases', 'AUSENCIA', 'Cumple'],
       ['Atributos de Calidad', 'SEGÚN ANEXO 04 – ACUERDO DE CALIDAD', 'Cumple']]
t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(0,0),(2,0),colors.green),
                       ('TEXTCOLOR',(0,0),(-1,-1),colors.blue)]))
elements.append(t)
# write the document to disk
doc.build(elements)