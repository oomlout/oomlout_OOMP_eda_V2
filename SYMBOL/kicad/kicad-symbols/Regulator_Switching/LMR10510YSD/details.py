
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR10510YSD"
    hexID = "SZKREGULATORSWITCHINGLMR151YSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR10510YSD', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_3x3mm_P0.95mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr10510.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Down Buck Voltage Regulator', 'kicadSymbolki_description': '1A, 5.5V Step-Down Voltage Regulator, 3MHz Frequency, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*EP*3x3mm*P0.95mm*'}])
    newPart['name'].append('LMR10510YSD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

