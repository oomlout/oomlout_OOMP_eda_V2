
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "AVR-ISP-10"
    hexID = "SZKCNAVRISP1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'AVR-ISP-10', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': ' ~', 'kicadSymbolki_keywords': 'AVR ISP Connector', 'kicadSymbolki_description': 'Atmel 10-pin ISP connector', 'kicadSymbolki_fp_filters': 'IDC?Header*2x05* Pin?Header*2x05*'}])
    newPart['name'].append('Connector : AVR-ISP-10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

