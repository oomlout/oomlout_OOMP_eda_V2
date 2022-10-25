
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "SIM28ML"
    hexID = "SZKGPSSIM28ML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SIM28ML', 'kicadSymbolFootprint': 'RF_GPS:SIM28ML', 'kicadSymbolDatasheet': 'https://simcom.ee/documents/SIM28ML/SIM28ML_Hardware%20Design_V1.01.pdf', 'kicadSymbolki_keywords': 'GPS A-GPS receiver', 'kicadSymbolki_description': 'Standalone GPS/A-GPS receiver module, built-in LNA, -165dBm sensitivity, 2.8-4.3V, SMD', 'kicadSymbolki_fp_filters': 'SIM28ML*'}])
    newPart['name'].append('RF_GPS : SIM28ML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

