
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-L-PI02-01-H02L"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1LPI21H2L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-L-PI02-01-H02L', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-L-PI02-01-H02L', 'kicadSymbolDatasheet': 'oom.lt/H02L', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H02L;Generic connector, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-L-PI02-01-H02L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

