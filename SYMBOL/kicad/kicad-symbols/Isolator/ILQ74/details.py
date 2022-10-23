
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ILQ74"
    hexID = "SZKISOLATORILQ74"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ILQ74', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/83640/ild74.pdf', 'kicadSymbolki_keywords': 'NPN DC Dual Optocoupler', 'kicadSymbolki_description': 'Quad Optocoupler, NPN Phototransistor Output, TTL compatible, DIP16/SMD16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W9.53mm*Clearance8mm*'}])
    newPart['name'].append('ILQ74')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

