
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "TD1205"
    hexID = "SZKRFMOTD125"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TD1205', 'kicadSymbolFootprint': 'RF_Module:TD1205', 'kicadSymbolDatasheet': 'https://github.com/Telecom-Design/Documentation_TD_RF_Module/blob/master/TD1205%20Datasheet.pdf', 'kicadSymbolki_keywords': 'IOT SIGFOX GPS', 'kicadSymbolki_description': 'High-Performance, Low-Current SIGFOX™ Gateway And GPS Receiver With Integrated Antennas', 'kicadSymbolki_fp_filters': 'TD1205*'}])
    newPart['name'].append('RF_Module : TD1205')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

