
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "TLV5627CPW"
    hexID = "SZKANALOGDACTLV5627CPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV5627CD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV5627CPW', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv5627.pdf', 'kicadSymbolki_keywords': 'DAC 4CH 8bit', 'kicadSymbolki_description': '4-Channel DAC, 8bit, w/ Power Down, TSSOP-16'}])
    newPart['name'].append('TLV5627CPW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

