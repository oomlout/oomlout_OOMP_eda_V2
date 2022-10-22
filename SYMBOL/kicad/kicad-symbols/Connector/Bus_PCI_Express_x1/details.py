
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Bus_PCI_Express_x1"
    hexID = "SZKCNBUSPCIEXPRESSX1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Bus_PCI_Express_x1', 'kicadSymbolFootprint': 'Connector_PCBEdge:BUS_PCIexpress_x1', 'kicadSymbolDatasheet': 'http://www.ritrontek.com/uploadfile/2016/1026/20161026105231124.pdf#page=63', 'kicadSymbolki_keywords': 'pcie', 'kicadSymbolki_description': 'PCI Express bus connector x1', 'kicadSymbolki_fp_filters': '*PCIexpress*'}])
    newPart['name'].append('Bus_PCI_Express_x1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

