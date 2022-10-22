
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TLV9001IDCK"
    hexID = "SZKAMPLIFIEROPERATIONALTLV91IDCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV172IDCK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV9001IDCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tlv9001.pdf', 'kicadSymbolki_keywords': 'op amp operational amplifier', 'kicadSymbolki_description': 'Low-power, Rail-to-Rail, 1MHz Operational Amplifier, SOT-353', 'kicadSymbolki_fp_filters': 'SOT*353*SC*70*'}])
    newPart['name'].append('TLV9001IDCK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

