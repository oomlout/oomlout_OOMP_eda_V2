
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HIP2101_QFN"
    hexID = "SZKDRIVERFETHIP211QFN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HIP2100_QFN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HIP2101_QFN', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/hip2/hip2101.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Half Bridge Driver, TTL/CMOS inputs, Output Current 2.0A, 100V, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.8mm*'}])
    newPart['name'].append('Driver_FET : HIP2101_QFN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

