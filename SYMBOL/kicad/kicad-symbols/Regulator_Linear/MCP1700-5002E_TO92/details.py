
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1700-5002E_TO92"
    hexID = "SZKREGULATORLINEARMCP1752ETO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM79L05_TO92', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1700-5002E_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20001826D.pdf', 'kicadSymbolki_keywords': 'regulator linear ldo', 'kicadSymbolki_description': '250mA Low Quiscent Current LDO, 5.0V output, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('MCP1700-5002E_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

