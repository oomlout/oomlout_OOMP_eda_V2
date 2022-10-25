
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MAX5438"
    hexID = "SZKPOTENTIOMETERDIGITALMAX5438"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5436', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5438', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX5436-MAX5439.pdf', 'kicadSymbolki_keywords': 'digital potentiometer resistor variable', 'kicadSymbolki_description': 'Low-Drift Digital Potentiometer'}])
    newPart['name'].append('Potentiometer_Digital : MAX5438')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

