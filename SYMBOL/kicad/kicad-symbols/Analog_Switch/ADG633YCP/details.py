
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "ADG633YCP"
    hexID = "SZKANALOGSWITCHADG633YCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADG633YCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Triple SPDT CMOS Analog Switch, 52Ohm Ron, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*4x4mm*P0.65mm*EP2.1x2.1mm*'}])
    newPart['name'].append('ADG633YCP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

