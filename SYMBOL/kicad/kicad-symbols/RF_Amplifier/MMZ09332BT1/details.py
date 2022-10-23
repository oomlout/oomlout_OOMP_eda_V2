
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "MMZ09332BT1"
    hexID = "SZKRFAMPLIFIERZ9332BT1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MMZ09332BT1', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/MMZ09332B.pdf', 'kicadSymbolki_keywords': 'RF', 'kicadSymbolki_description': 'High Efficiency/Linearity Amplifier high linearity broadband amplifier, QFN-12', 'kicadSymbolki_fp_filters': 'QFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('MMZ09332BT1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

