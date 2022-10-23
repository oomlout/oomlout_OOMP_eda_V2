
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "Si512A_2.5x3.2mm"
    hexID = "SZKOCSSI512A25X32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si512A_2.5x3.2mm', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Silicon_Labs_LGA-6_2.5x3.2mm_P1.25mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si512-13.pdf', 'kicadSymbolki_keywords': 'Dual frequency crystal oscillator', 'kicadSymbolki_description': 'Dual frequency crystal oscillator (XO) 100 kHz to 250 MHz, Single-ended CMOS output', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Silicon*Labs*LGA*2.5x3.2mm*P1.25mm*'}])
    newPart['name'].append('Si512A_2.5x3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

