
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MRA4003T3G"
    hexID = "SZKDIODEMRA43T3G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MRA4003T3G', 'kicadSymbolFootprint': 'Diode_SMD:D_SMA', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/MRA4003T3-D.PDF', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '300V, 1A, General Purpose Rectifier Diode, SMA(DO-214AC)', 'kicadSymbolki_fp_filters': 'D*SMA*'}])
    newPart['name'].append('Diode : MRA4003T3G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

