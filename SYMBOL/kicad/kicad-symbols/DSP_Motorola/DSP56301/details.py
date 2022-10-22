
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Motorola"
    oIndex = "DSP56301"
    hexID = "SZKDSPMOTOROLADSP5631"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSP56301', 'kicadSymbolFootprint': 'Package_QFP:PQFP-208_28x28mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/DSP56301DS.pdf', 'kicadSymbolki_keywords': 'DSP PCI', 'kicadSymbolki_description': '24-Bit Digital Signal Processor with PCI bus interface', 'kicadSymbolki_fp_filters': 'PQFP*28x28mm*P0.5mm*'}])
    newPart['name'].append('DSP56301')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

