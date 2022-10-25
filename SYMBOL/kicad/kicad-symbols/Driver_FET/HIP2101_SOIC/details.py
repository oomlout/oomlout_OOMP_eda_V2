
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HIP2101_SOIC"
    hexID = "SZKDRIVERFETHIP211SOIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HIP2100_SOIC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HIP2101_SOIC', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/hip2/hip2101.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Half Bridge Driver, TTL/CMOS inputs, Output Current 2.0A, 100V, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : HIP2101_SOIC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

