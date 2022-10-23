
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "LEA-M8S"
    hexID = "SZKGPSLEAM8S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LEA-M8S', 'kicadSymbolFootprint': 'RF_GPS:ublox_LEA', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/LEA-M8S-FW3_DataSheet_%28UBX-16010205%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module LEA M8, VCC 2.7V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*LEA*'}])
    newPart['name'].append('LEA-M8S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

