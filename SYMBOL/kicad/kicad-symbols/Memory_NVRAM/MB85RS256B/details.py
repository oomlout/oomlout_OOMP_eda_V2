
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_NVRAM"
    oIndex = "MB85RS256B"
    hexID = "SZKMEMORYNVRAMMB85RS256B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MB85RS16', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MB85RS256B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.fujitsu.com/downloads/MICRO/fsa/pdf/products/memory/fram/MB85RS16-DS501-00014-6v0-E.pdf', 'kicadSymbolki_keywords': 'FRAM SPI 3.3V', 'kicadSymbolki_description': 'FRAM memory with SPI interface, SOIC-8 SON-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x5.05mm*P1.27mm* *SON*2x3mm*P0.50mm*'}])
    newPart['name'].append('MB85RS256B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

