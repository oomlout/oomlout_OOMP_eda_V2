
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "PTN78020H_EUK-7"
    hexID = "SZKCONPTN782HEUK7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PTN78020W_EUK-7', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PTN78020H_EUK-7', 'kicadSymbolFootprint': 'Module:Texas_EUK_R-PDSS-T7_THT', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ptn78020w.pdf', 'kicadSymbolki_keywords': 'texas dc-dc converter step down buck', 'kicadSymbolki_description': '6A non-isolated switching regulator power module, 7-36V input voltage, 11.85-22V output voltage, EUK-7', 'kicadSymbolki_fp_filters': 'Texas*EUK*R?PDSS?T7*'}])
    newPart['name'].append('PTN78020H_EUK-7')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

