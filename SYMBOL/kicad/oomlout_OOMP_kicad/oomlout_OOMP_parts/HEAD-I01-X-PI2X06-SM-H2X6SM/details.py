
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X06-SM-H2X6SM"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X6SMH2X6SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI2X06-SM-H2X6SM', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI2X06-SM-H2X6SM', 'kicadSymbolDatasheet': 'oom.lt/H2X6SM', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H2X6SM;Generic connector, double row, 02x06, odd/even pin numbering scheme (row 1 odd numbers, row 2 even numbers), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??_*'}])
    newPart['name'].append('HEAD-I01-X-PI2X06-SM-H2X6SM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

