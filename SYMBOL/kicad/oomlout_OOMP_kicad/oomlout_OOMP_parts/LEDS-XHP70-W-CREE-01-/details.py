
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "LEDS-XHP70-W-CREE-01-"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSLSXHP7WCREE1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LEDS-XHP70-W-CREE-01-', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:LEDS-XHP70-W-CREE-01-', 'kicadSymbolDatasheet': 'oom.lt/', 'kicadSymbolki_keywords': 'LED diode', 'kicadSymbolki_description': 'hexID: ;Light emitting diode', 'kicadSymbolki_fp_filters': 'LED* LED_SMD:* LED_THT:*'}])
    newPart['name'].append('LEDS-XHP70-W-CREE-01-')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

