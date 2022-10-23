
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TLV62084DSGx"
    hexID = "SZKREGULATORSWITCHINGTLV6284DSGX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV62080DSGx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV62084DSGx', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv62080.pdf', 'kicadSymbolki_keywords': 'Synchronous Buck', 'kicadSymbolki_description': 'High-efficiency Step-down Converter', 'kicadSymbolki_fp_filters': '*WSON?8?1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('TLV62084DSGx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

