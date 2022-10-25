
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "8237"
    hexID = "SZKINTERFACE8237"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8237', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'https://pdos.csail.mit.edu/6.828/2012/readings/hardware/8237A.pdf', 'kicadSymbolki_keywords': '8237 DMA', 'kicadSymbolki_description': 'Programmable DMA Controller, PDIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* PDIP*W15.24mm*'}])
    newPart['name'].append('Interface : 8237')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

