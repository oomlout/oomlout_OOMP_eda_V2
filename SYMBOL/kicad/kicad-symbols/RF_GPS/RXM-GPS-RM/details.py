
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "RXM-GPS-RM"
    hexID = "SZKGPSRXMGPSRM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RXM-GPS-RM', 'kicadSymbolFootprint': 'RF_GPS:Linx_RXM-GPS', 'kicadSymbolDatasheet': 'https://linxtechnologies.com/wp/wp-content/uploads/rxm-gps-rm.pdf', 'kicadSymbolki_keywords': 'gps low-power', 'kicadSymbolki_description': 'Module GPS Low Power, 14mA tracking, 22 channels', 'kicadSymbolki_fp_filters': 'Linx*RXM?GPS*'}])
    newPart['name'].append('RF_GPS : RXM-GPS-RM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

