
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "ICL7667"
    hexID = "SZKDRIVERFETICL7667"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICL7667', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/icl7/icl7667.pdf', 'kicadSymbolki_keywords': 'MOSFET driver array', 'kicadSymbolki_description': 'Dual Power MOSFET Driver, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : ICL7667')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

