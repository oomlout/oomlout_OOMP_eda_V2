
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "NEO-8Q"
    hexID = "SZKGPSNEO8Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NEO-M8N', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NEO-8Q', 'kicadSymbolFootprint': 'RF_GPS:ublox_NEO', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/NEO-8Q_DataSheet_%28UBX-15031913%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module NEO 8, VCC 1.65V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*NEO*'}])
    newPart['name'].append('NEO-8Q')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

