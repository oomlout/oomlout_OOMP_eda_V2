
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74AHC2G00"
    hexID = "SZK74XGXX74AHC2G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC2G00', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHC2G00', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74AHC_AHCT2G00.pdf', 'kicadSymbolki_keywords': 'Dual Gate NAND LVC CMOS', 'kicadSymbolki_description': 'Dual NAND Gate, High-speed Si-gate CMOS', 'kicadSymbolki_fp_filters': 'SSOP* VSSOP*'}])
    newPart['name'].append('74AHC2G00')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

