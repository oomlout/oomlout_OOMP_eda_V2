
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD4S014"
    hexID = "SZKPOWERPROTECTIONTPD4S14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD4S014', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PWSON-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd4s014.pdf', 'kicadSymbolki_keywords': 'USB  Port Protection', 'kicadSymbolki_description': 'USB Charger Port Protection Including ESD Protection for All Lines and Overvoltage Protection on VBUS', 'kicadSymbolki_fp_filters': 'Package?SON:Texas?S?PWSON?N10*'}])
    newPart['name'].append('TPD4S014')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

