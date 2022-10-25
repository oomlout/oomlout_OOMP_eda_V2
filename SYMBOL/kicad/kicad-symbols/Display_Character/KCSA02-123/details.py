
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "KCSA02-123"
    hexID = "SZKDICHARACTERKCSA2123"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KCSA02-123', 'kicadSymbolFootprint': 'Display_7Segment:KCSC02-123', 'kicadSymbolDatasheet': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/KCSA02-123(Ver.9A).pdf', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'One digit 7 segment green LED, common anode', 'kicadSymbolki_fp_filters': 'KCSC02?123*'}])
    newPart['name'].append('Display_Character : KCSA02-123')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

