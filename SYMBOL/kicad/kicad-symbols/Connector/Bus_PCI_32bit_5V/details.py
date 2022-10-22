
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Bus_PCI_32bit_5V"
    hexID = "SZKCNBUSPCI32BIT5V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Bus_PCI_32bit_5V', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pinouts.ru/Slots/PCI_pinout.shtml', 'kicadSymbolki_keywords': 'PCI 5V', 'kicadSymbolki_description': 'PCI bus connector for 5V cards'}])
    newPart['name'].append('Bus_PCI_32bit_5V')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

