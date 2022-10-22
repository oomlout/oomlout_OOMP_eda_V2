
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "A4953_LJ"
    hexID = "SZKDRIVERMOTORA4953LJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A4950E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A4953_LJ', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm', 'kicadSymbolDatasheet': 'www.allegromicro.com/~/media/Files/Datasheets/A4952-3-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'Full-bridge h-bridge', 'kicadSymbolki_description': 'Full-Bridge, DMOS PWM, Motor Driver, 40V, 2A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC-*1EP*'}])
    newPart['name'].append('A4953_LJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

