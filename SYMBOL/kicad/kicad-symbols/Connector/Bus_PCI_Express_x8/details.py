
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Bus_PCI_Express_x8"
    hexID = "SZKCNBUSPCIEXPRESSX8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Bus_PCI_Express_x8', 'kicadSymbolFootprint': 'Connector_PCBEdge:BUS_PCIexpress_x8', 'kicadSymbolDatasheet': 'http://www.ritrontek.com/uploadfile/2016/1026/20161026105231124.pdf#page=63', 'kicadSymbolki_keywords': 'pcie', 'kicadSymbolki_description': 'PCI Express bus connector x8', 'kicadSymbolki_fp_filters': '*PCIexpress*'}])
    newPart['name'].append('Connector : Bus_PCI_Express_x8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

