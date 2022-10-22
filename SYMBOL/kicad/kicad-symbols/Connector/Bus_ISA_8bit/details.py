
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Bus_ISA_8bit"
    hexID = "SZKCNBUSISA8BIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Bus_ISA_8bit', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://en.wikipedia.org/wiki/Industry_Standard_Architecture', 'kicadSymbolki_keywords': 'ISA', 'kicadSymbolki_description': '8-bit ISA-PC bus connector'}])
    newPart['name'].append('Bus_ISA_8bit')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

