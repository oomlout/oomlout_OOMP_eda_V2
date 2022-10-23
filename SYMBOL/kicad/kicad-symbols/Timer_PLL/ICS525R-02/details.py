
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "ICS525R-02"
    hexID = "SZKTIMERPLLICS525R2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ICS525-01R', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICS525R-02', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_3.9x9.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.idt.com/document/dst/525-01-02-datasheet', 'kicadSymbolki_keywords': 'Configurable clock', 'kicadSymbolki_description': 'User configurable clock up to 200 MHz, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*3.9x9.9mm*P0.635mm*'}])
    newPart['name'].append('ICS525R-02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

