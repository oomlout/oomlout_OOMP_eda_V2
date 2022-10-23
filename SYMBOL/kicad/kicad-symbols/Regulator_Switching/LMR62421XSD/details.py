
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR62421XSD"
    hexID = "SZKREGULATORSWITCHINGLMR62421XSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR62421XSD', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_3x3mm_P0.95mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr62421.pdf', 'kicadSymbolki_keywords': 'Miniature Step-Up Boost SEPIC Voltage Regulator', 'kicadSymbolki_description': '2.1A, 24Vout Step-Up Voltage Regulator, 1.6MHz Frequency, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*EP*3x3mm*P0.95mm*'}])
    newPart['name'].append('LMR62421XSD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

