
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI2X05-RS-H2X5RS"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI2X5RSH2X5RS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI2X05-RS-H2X5RS', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI2X05-RS-H2X5RS', 'kicadSymbolDatasheet': 'oom.lt/H2X5RS', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H2X5RS;Generic connector, double row, 02x05, odd/even pin numbering scheme (row 1 odd numbers, row 2 even numbers), script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_2x??_*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI2X05-RS-H2X5RS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

