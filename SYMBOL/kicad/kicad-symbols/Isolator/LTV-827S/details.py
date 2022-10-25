
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-827S"
    hexID = "SZKISOLATORLTV827S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-827S', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-8_W9.53mm', 'kicadSymbolDatasheet': 'http://www.us.liteon.com/downloads/LTV-817-827-847.PDF', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 35V, CTR 50%, SMDIP-8', 'kicadSymbolki_fp_filters': 'SMDIP*W9.53mm*'}])
    newPart['name'].append('Isolator : LTV-827S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

