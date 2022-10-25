
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "LEA-M8T"
    hexID = "SZKGPSLEAM8T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LEA-M8T', 'kicadSymbolFootprint': 'RF_GPS:ublox_LEA', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/NEO-LEA-M8T-FW3_DataSheet_%28UBX-15025193%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module LEA M8, VCC 2.7V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*LEA*'}])
    newPart['name'].append('RF_GPS : LEA-M8T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

