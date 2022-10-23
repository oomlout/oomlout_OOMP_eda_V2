
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Coded_SH-7050"
    hexID = "SZKSWITCHSWCODEDSH75"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Coded_SH-7050', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf', 'kicadSymbolki_keywords': 'rotary hex Real', 'kicadSymbolki_description': 'Rotary switch, 4-bit encoding, 16 positions, Real code', 'kicadSymbolki_fp_filters': 'Nidec*Copal*SH*7010*'}])
    newPart['name'].append('SW_Coded_SH-7050')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

