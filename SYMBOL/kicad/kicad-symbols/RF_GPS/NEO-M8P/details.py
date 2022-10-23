
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "NEO-M8P"
    hexID = "SZKGPSNEOM8P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NEO-M8P', 'kicadSymbolFootprint': 'RF_GPS:ublox_NEO', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/NEO-M8P_DataSheet_%28UBX-15016656%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS RTK module', 'kicadSymbolki_description': 'GNSS RTK Module NEO M8, VCC 2.7V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*NEO*'}])
    newPart['name'].append('NEO-M8P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

