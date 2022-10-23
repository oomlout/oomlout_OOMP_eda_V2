
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX15062B"
    hexID = "SZKREGULATORSWITCHINGMAX1562B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX15062A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX15062B', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8_2x2mm_P0.5mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX15062.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc switching regulator', 'kicadSymbolki_description': '60V, 300mA, synchronous step-down dc-dc converter, 5.0V fixed output voltage, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*2x2mm*P0.5mm*'}])
    newPart['name'].append('MAX15062B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

