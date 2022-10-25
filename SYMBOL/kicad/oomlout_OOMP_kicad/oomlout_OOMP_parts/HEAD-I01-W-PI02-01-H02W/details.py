
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-W-PI02-01-H02W"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1WPI21H2W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-W-PI02-01-H02W', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-W-PI02-01-H02W', 'kicadSymbolDatasheet': 'oom.lt/H02W', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H02W;Generic connector, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-W-PI02-01-H02W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

