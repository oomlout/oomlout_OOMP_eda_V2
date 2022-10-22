
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "TLV7031DBV"
    hexID = "SZKCOMPARATORTLV731DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP6561-OT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV7031DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tlv7031.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single, 1.6V-6.5V, 315nA Quiescent, Push-Pull Output, Comparator, SOT-23-5/SC-70', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('TLV7031DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

