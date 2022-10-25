
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "HDSM-541B"
    hexID = "SZKDICHARACTERHDSM541B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HDSM-541B', 'kicadSymbolFootprint': 'Display:HDSM-441B_HDSM-443B', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1588EN', 'kicadSymbolki_keywords': 'display LED 7-segment', 'kicadSymbolki_description': 'Double 7 segment Blue LED common anode SMD mount', 'kicadSymbolki_fp_filters': 'HDSM?441B?HDSM?443B*'}])
    newPart['name'].append('Display_Character : HDSM-541B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

