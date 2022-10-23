
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "ZETA-915-SO"
    hexID = "SZKRFAMFMZETA915SO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZETA-433-SO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ZETA-915-SO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.rfsolutions.co.uk/downloads/1456219226DS-ZETA.pdf', 'kicadSymbolki_keywords': 'RF TRANSCEIVER MODULE', 'kicadSymbolki_description': 'FM ZETA TRANSCEIVER MODULE, OPTIMISED FOR 915MHZ', 'kicadSymbolki_fp_filters': 'ZETA?433?SO?SMD* ZETA?433?SO?THT*'}])
    newPart['name'].append('ZETA-915-SO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

