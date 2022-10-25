
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS2890DS"
    hexID = "SZKDRIVERFETIRS289DS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2890DS', 'kicadSymbolFootprint': 'Package_SO:SOIC-14_3.9x8.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRS2890DS-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aad6fbc8a4bf4', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Driver with Overcurrent Protection, 600V, 220/480mA, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : IRS2890DS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

