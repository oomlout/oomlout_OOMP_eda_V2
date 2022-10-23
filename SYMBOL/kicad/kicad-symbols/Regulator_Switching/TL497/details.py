
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TL497"
    hexID = "SZKREGULATORSWITCHINGTL497"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL497', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl497a.pdf', 'kicadSymbolki_keywords': 'buck regulator', 'kicadSymbolki_description': '500mA step up/step down/inverting switching voltage regulator, SIP-14/SOIC-14(W)', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x9.0mm*P1.27mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('TL497')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

