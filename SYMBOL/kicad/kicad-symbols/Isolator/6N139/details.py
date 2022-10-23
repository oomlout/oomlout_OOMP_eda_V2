
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "6N139"
    hexID = "SZKISOLATOR6N139"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '6N138', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '6N139', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/HCPL2731-D.pdf', 'kicadSymbolki_keywords': 'darlington optocoupler', 'kicadSymbolki_description': 'Low Input Current high Gain Split Darlington Optocouplers, -0.5V to 18V VDD, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SMDIP*W9.53mm*'}])
    newPart['name'].append('6N139')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

