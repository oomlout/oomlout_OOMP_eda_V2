
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X01-SHRO-H2X1SH"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X1SHROH2X1SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI2X01-SHRO-H2X1SH', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI2X01-SHRO-H2X1SH', 'kicadSymbolDatasheet': 'oom.lt/H2X1SH', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H2X1SH;Generic connector, double row, 02x01, row letter first pin numbering scheme (pin number consists of a letter for the row and a number for the pin index in this row. a1, ..., aN; b1, ..., bN), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??_*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI2X01-SHRO-H2X1SH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

