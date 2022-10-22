
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TERS-05-G-PI02-01-ST502G"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTERS5GPI21ST52G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'TERS-05-G-PI02-01-ST502G', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:TERS-05-G-PI02-01-ST502G', 'kicadSymbolDatasheet': 'oom.lt/ST502G', 'kicadSymbolki_keywords': 'screw terminal', 'kicadSymbolki_description': 'hexID: ST502G;Generic screw terminal, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'TerminalBlock*:*'}])
    newPart['name'].append('TERS-05-G-PI02-01-ST502G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

