
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "AD9984AKST"
    hexID = "SZKVIDEOAD9984AKST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9984AKST', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_14x14mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.analog.com/media/en/technical-documentation/data-sheets/AD9984A.pdf', 'kicadSymbolki_keywords': '10bit video display interface', 'kicadSymbolki_description': 'High Performance 10-Bit Display Interface 140/170MSPS LQFP', 'kicadSymbolki_fp_filters': 'LQFP*'}])
    newPart['name'].append('AD9984AKST')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

