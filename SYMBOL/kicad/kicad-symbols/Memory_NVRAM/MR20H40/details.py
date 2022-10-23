
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_NVRAM"
    oIndex = "MR20H40"
    hexID = "SZKMEMORYNVRAMMR2H4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MR20H40', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.everspin.com/file/217/download', 'kicadSymbolki_keywords': 'MRAM SPI EEPROM 3.3V', 'kicadSymbolki_description': '4Mb MRAM memory with SPI interface, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*6x5mm*P1.27mm*'}])
    newPart['name'].append('MR20H40')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

