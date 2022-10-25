
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MAX6325"
    hexID = "SZKREFERENCEVOLTAGEMAX6325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX6350', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX6325', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX6325-MAX6350.pdf', 'kicadSymbolki_keywords': 'precision voltage reference', 'kicadSymbolki_description': '0.5ppm/°C Low-Noise +2.5V Voltage Reference, SO-8/DIP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Reference_Voltage : MAX6325')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

