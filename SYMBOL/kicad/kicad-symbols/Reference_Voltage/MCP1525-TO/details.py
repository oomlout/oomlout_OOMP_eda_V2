
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1525-TO"
    hexID = "SZKREFERENCEVOLTAGEMCP1525TO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1525-TO', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21653b.pdf', 'kicadSymbolki_keywords': 'Voltage Reference 2.5V', 'kicadSymbolki_description': '2.5V Voltage Reference, TO-92', 'kicadSymbolki_fp_filters': 'TO*92*'}])
    newPart['name'].append('Reference_Voltage : MCP1525-TO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

