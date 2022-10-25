
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X06-SHRO-H2X6SH"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X6SHROH2X6SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI2X06-SHRO-H2X6SH', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI2X06-SHRO-H2X6SH', 'kicadSymbolDatasheet': 'oom.lt/H2X6SH', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H2X6SH;Generic connector, double row, 02x06, odd/even pin numbering scheme (row 1 odd numbers, row 2 even numbers), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??_*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI2X06-SHRO-H2X6SH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

