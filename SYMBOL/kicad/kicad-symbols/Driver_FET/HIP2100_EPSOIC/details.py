
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HIP2100_EPSOIC"
    hexID = "SZKDRIVERFETHIP21EPSOIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HIP2100_EPSOIC', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.514x3.2mm', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/hip2/hip2100.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Half Bridge Driver, Output Current 2.0A, 100V, EPSOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : HIP2100_EPSOIC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

