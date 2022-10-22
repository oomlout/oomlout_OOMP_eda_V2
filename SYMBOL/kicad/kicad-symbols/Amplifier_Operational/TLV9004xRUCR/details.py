
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TLV9004xRUCR"
    hexID = "SZKAMPLIFIEROPERATIONALTLV94XRUCR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV9004xRUCR', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PX2QFN-14', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv9004.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': 'Low-Power, Quad-Operational Amplifiers, Texas S-PX2QFN-14', 'kicadSymbolki_fp_filters': 'Texas*S*PX2QFN*'}])
    newPart['name'].append('TLV9004xRUCR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

