
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_Coded_SH-7030"
    hexID = "SZKSWITCHSWCODEDSH73"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SW_Coded_SH-7010', 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_Coded_SH-7030', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nidec-copal-electronics.com/e/catalog/switch/sh-7000.pdf', 'kicadSymbolki_keywords': 'rotary bcd Complementary', 'kicadSymbolki_description': 'Rotary switch, 4-bit encoding, 10 positions, Complementary code', 'kicadSymbolki_fp_filters': 'Nidec*Copal*SH*7010*'}])
    newPart['name'].append('SW_Coded_SH-7030')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

