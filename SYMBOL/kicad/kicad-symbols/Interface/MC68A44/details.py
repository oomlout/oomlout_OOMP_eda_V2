
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "MC68A44"
    hexID = "SZKINTERFACEMC68A44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC6844', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68A44', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheets/560/501527_DS.pdf', 'kicadSymbolki_keywords': 'Direct Memory Access Controller', 'kicadSymbolki_description': 'Direct Memory Access Controller 1.5MHz, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Interface : MC68A44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

