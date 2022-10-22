
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "PTN78060H_EUW-7"
    hexID = "SZKCONPTN786HEUW7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PTN78060W_EUW-7', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PTN78060H_EUW-7', 'kicadSymbolFootprint': 'Module:Texas_EUW_R-PDSS-T7_THT', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ptn78060w.pdf', 'kicadSymbolki_keywords': 'texas dc-dc converter step down buck', 'kicadSymbolki_description': '3A non-isolated switching regulator power module, 7-36V input voltage, 11.85-22V output voltage, EUW-7', 'kicadSymbolki_fp_filters': 'Texas*EUW*R?PDSS?T7*'}])
    newPart['name'].append('PTN78060H_EUW-7')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

