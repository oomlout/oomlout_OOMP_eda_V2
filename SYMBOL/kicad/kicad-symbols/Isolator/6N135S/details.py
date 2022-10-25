
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "6N135S"
    hexID = "SZKISOLATOR6N135S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '6N135S', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-8_W9.53mm', 'kicadSymbolDatasheet': 'https://optoelectronics.liteon.com/upload/download/DS70-2008-0032/6N135-L%206N136-L%20series.pdf', 'kicadSymbolki_keywords': 'High Speed Optocoupler', 'kicadSymbolki_description': 'High Speed Optocoupler, TTL Compatible, CTR 18%, SMDIP8', 'kicadSymbolki_fp_filters': 'SMDIP*W9.53mm*'}])
    newPart['name'].append('Isolator : 6N135S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

