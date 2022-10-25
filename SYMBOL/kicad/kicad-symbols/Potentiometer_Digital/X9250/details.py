
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "X9250"
    hexID = "SZKPOTENTIOMETERDIGITALX925"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'X9250', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.intersil.com/content/dam/Intersil/documents/x925/x9250.pdf', 'kicadSymbolki_keywords': 'potentiometer resistor variable digital', 'kicadSymbolki_description': 'Quad 100k Digital Potentiometer, 256 steps, TSSOP-24/SOIC-24', 'kicadSymbolki_fp_filters': 'SOIC*7.5x15.4mm*P1.27mm* TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Potentiometer_Digital : X9250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

