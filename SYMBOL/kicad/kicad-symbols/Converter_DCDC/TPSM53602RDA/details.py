
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "TPSM53602RDA"
    hexID = "SZKCONTPSM5362RDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPSM53602RDA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tpsm53602.pdf', 'kicadSymbolki_keywords': 'step down DCDC converter regulator', 'kicadSymbolki_description': ' 36-V, 2A input, stepdown, DC/DC converter, Texas B3QFN-14', 'kicadSymbolki_fp_filters': 'Texas*B3QFN*1EP*5x5.5mm*P0.65mm*'}])
    newPart['name'].append('TPSM53602RDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

