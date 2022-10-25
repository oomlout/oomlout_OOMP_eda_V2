
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HIP4080A"
    hexID = "SZKDRIVERFETHIP48A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HIP4080A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/hip4/hip4080a.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Full Bridge FET Driver, Input Comparator, 2.5A, 80V, DIP-20/SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : HIP4080A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

