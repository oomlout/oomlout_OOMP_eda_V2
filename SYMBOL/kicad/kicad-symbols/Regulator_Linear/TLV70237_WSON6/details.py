
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV70237_WSON6"
    hexID = "SZKREGULATORLINEARTLV7237WSON6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV70012_WSON6', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV70237_WSON6', 'kicadSymbolFootprint': 'Package_SON:WSON-6_1.5x1.5mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv702.pdf', 'kicadSymbolki_keywords': '300mA LDO Regulator Fixed Positive', 'kicadSymbolki_description': '300mA Low Dropout Voltage Regulator, Fixed Output 3.7V, WSON6', 'kicadSymbolki_fp_filters': 'WSON*'}])
    newPart['name'].append('TLV70237_WSON6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

