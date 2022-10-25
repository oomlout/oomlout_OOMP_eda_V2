
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "HIP2101_DFN"
    hexID = "SZKDRIVERFETHIP211DFN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HIP2100_DFN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HIP2101_DFN', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_4x4mm_P0.5mm_EP2.66x3.38mm', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/hip2/hip2101.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Half Bridge Driver, TTL/CMOS inputs, Output Current 2.0A, 100V, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Driver_FET : HIP2101_DFN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

