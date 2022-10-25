
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1825S"
    hexID = "SZKREGULATORLINEARMCP1825S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1825S', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22056b.pdf', 'kicadSymbolki_keywords': 'regulator linear ldo', 'kicadSymbolki_description': '500mA, Low-Voltage, Low Quiescent Current LDO Regulator, SOT-223, TO-220, TO-263', 'kicadSymbolki_fp_filters': 'SOT?223*TabPin2* TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : MCP1825S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

