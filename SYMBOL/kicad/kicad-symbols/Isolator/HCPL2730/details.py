
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "HCPL2730"
    hexID = "SZKISOLATORHCPL273"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HCPL2731', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HCPL2730', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/HCPL2731-D.pdf', 'kicadSymbolki_keywords': 'darlington optocoupler', 'kicadSymbolki_description': 'Low Input Current high Gain Split Darlington Optocouplers', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SMDIP*W9.53mm*'}])
    newPart['name'].append('HCPL2730')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

