
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TERS-35D-G-PI02-01-ST302G"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTERS35DGPI21ST32G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'TERS-35D-G-PI02-01-ST302G', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:TERS-35D-G-PI02-01-ST302G', 'kicadSymbolDatasheet': 'oom.lt/ST302G', 'kicadSymbolki_keywords': 'screw terminal', 'kicadSymbolki_description': 'hexID: ST302G;Generic screw terminal, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'TerminalBlock*:*'}])
    newPart['name'].append('oomlout_OOMP_parts : TERS-35D-G-PI02-01-ST302G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

