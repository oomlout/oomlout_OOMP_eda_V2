
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "MIC4426"
    hexID = "SZKDRIVERFETMIC4426"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC4426', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/el72/el7202-12-22.pdf', 'kicadSymbolki_keywords': 'Driver, Dual MOSFET', 'kicadSymbolki_description': 'Dual 1.5A-Peak Low-Side MOSFET Driver, DIP-8/SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* MSOP*P0.65mm*'}])
    newPart['name'].append('Driver_FET : MIC4426')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

