
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "CP2102N-Axx-xQFN24"
    hexID = "SZKINTERFACEUCP212NAXXXQFN24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CP2102N-Axx-xQFN24', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf', 'kicadSymbolki_keywords': 'USB UART bridge', 'kicadSymbolki_description': 'USB to UART master bridge, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : CP2102N-Axx-xQFN24')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

