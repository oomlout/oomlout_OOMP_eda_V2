
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MAX872"
    hexID = "SZKREFERENCEVOLTAGEMAX872"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX874', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX872', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://pdfserv.maximintegrated.com/en/ds/MAX872-MAX874.pdf', 'kicadSymbolki_keywords': 'Low-Dropout Precision Voltage Reference', 'kicadSymbolki_description': '10µA Low-Dropout Precision Voltage Reference, SO-8/DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : MAX872')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

