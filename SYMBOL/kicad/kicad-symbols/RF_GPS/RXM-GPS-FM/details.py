
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "RXM-GPS-FM"
    hexID = "SZKGPSRXMGPSFM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RXM-GPS-RM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RXM-GPS-FM', 'kicadSymbolFootprint': 'RF_GPS:Linx_RXM-GPS', 'kicadSymbolDatasheet': 'https://linxtechnologies.com/wp/wp-content/uploads/rxm-gps-fm.pdf', 'kicadSymbolki_keywords': 'gps low-power', 'kicadSymbolki_description': 'Module GPS Low Power, 14mA tracking, 22 channels', 'kicadSymbolki_fp_filters': 'Linx*RXM?GPS*'}])
    newPart['name'].append('RF_GPS : RXM-GPS-FM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

