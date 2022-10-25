
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "EL7222CN"
    hexID = "SZKDRIVERFETEL7222CN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EL7222CN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/el72/el7202-12-22.pdf', 'kicadSymbolki_keywords': 'Driver, Dual MOSFET', 'kicadSymbolki_description': 'High Speed, Dual Channel Power MOSFET Driver, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*P1.27mm*'}])
    newPart['name'].append('Driver_FET : EL7222CN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

