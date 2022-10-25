
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1541-TO"
    hexID = "SZKREFERENCEVOLTAGEMCP1541TO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1525-TO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1541-TO', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/21653b.pdf', 'kicadSymbolki_keywords': 'Voltage Reference 4.096V', 'kicadSymbolki_description': '4.096V Voltage Reference, TO-92', 'kicadSymbolki_fp_filters': 'TO*92*'}])
    newPart['name'].append('Reference_Voltage : MCP1541-TO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

