
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "68C681"
    hexID = "SZKINTERFACEUART68C681"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '68C681', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.elektronik.ropla.eu/pdf/stock/exa/xr68c681.pdf', 'kicadSymbolki_keywords': 'UART serial', 'kicadSymbolki_description': 'CMOS Dual Channel UART'}])
    newPart['name'].append('Interface_UART : 68C681')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

