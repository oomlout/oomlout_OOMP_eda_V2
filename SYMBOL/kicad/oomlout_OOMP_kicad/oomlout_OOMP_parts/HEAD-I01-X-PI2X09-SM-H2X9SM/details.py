
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X09-SM-H2X9SM"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X9SMH2X9SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI2X09-SM-H2X9SM', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI2X09-SM-H2X9SM', 'kicadSymbolDatasheet': 'oom.lt/H2X9SM', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H2X9SM;Generic connector, double row, 02x09, odd/even pin numbering scheme (row 1 odd numbers, row 2 even numbers), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??_*'}])
    newPart['name'].append('HEAD-I01-X-PI2X09-SM-H2X9SM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

