
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "CP2102N-Axx-xQFN20"
    hexID = "SZKINTERFACEUCP212NAXXXQFN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CP2102N-Axx-xQFN20', 'kicadSymbolFootprint': 'Package_DFN_QFN:SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/cp2102n-datasheet.pdf', 'kicadSymbolki_keywords': 'USB UART bridge', 'kicadSymbolki_description': 'USB to UART master bridge, QFN-20', 'kicadSymbolki_fp_filters': 'SiliconLabs*QFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('CP2102N-Axx-xQFN20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

