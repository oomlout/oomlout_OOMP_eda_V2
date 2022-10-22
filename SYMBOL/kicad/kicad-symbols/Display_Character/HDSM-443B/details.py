
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSM-443B"
    hexID = "SZKDICHARACTERHDSM443B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSM-443B', 'kicadSymbolFootprint': 'Display:HDSM-441B_HDSM-443B', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1589EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double 7 segment Blue LED common cathode SMD mount', 'kicadSymbolki_fp_filters': '*HDSM*441B*'}])
    newPart['name'].append('HDSM-443B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

