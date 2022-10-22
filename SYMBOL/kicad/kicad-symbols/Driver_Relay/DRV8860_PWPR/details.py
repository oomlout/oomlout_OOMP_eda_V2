
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Relay"
    oIndex = "DRV8860_PWPR"
    hexID = "SZKDRIVERRELAYDRV886PWPR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8860_PWPR', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/drv8860.pdf', 'kicadSymbolki_keywords': 'Relay Driver', 'kicadSymbolki_description': '8-Channel Serial Interface Low-Side Driver', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('DRV8860_PWPR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

