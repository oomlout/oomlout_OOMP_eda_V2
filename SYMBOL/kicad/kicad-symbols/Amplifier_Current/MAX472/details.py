
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "MAX472"
    hexID = "SZKAMPLIFIERCURRENTMAX472"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX472', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pdfserv.maximintegrated.com/en/ds/MAX471-MAX472.pdf', 'kicadSymbolki_keywords': 'current sense amplifier', 'kicadSymbolki_description': 'Precision, High-Side, Current-Sense Amplifiers, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Current : MAX472')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

