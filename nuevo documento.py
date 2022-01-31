from reportlab.pdfgen import canvas

frase = ['El patio de mi casa,', 'es particular', 'cuando llueve se moja', 'como los demás']

documento = canvas.Canvas('documentoTexto.pdf')

obxTexto = documento.beginText()
obxTexto.setTextOrigin(100, 500)
obxTexto.setFont('Courier', 14)
for linha in frase:
    obxTexto.textLine(linha)

obxTexto.setFillGray(0.5)
libhasTexto = '''Este é un texto multiliña,
 que vai en un comentario e 
 o imos escribir con Python e 
 Reporlab.
'''

obxTexto.textLine(libhasTexto)
for tipoLetra in documento.getAvailableFonts():
    obxTexto.setFont(tipoLetra, 12)
    obxTexto.textLine(tipoLetra + ': ' + frase[2])

obxTexto.setFont('Helvetica', 14)

for linha in frase:
    obxTexto.textOut(linha)
    obxTexto.moveCursor(20, 15)

obxTexto.setWordSpace(8)
obxTexto.textLines(libhasTexto)

espazo = 0
for n, linea in enumerate(frase):
    obxTexto.setCharSpace(espazo)
    obxTexto.textLine(linea)
    espazo = n + 1

documento.drawText(obxTexto)
documento.showPage()
documento.save()
