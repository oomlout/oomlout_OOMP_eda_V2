
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_NVRAM"
    oIndex = "FM18W08-SG"
    hexID = "SZKMEMORYNVRAMFM18W8SG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FM18W08-SG', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/file/136521/download', 'kicadSymbolki_keywords': 'FRAM 5V Parallel', 'kicadSymbolki_description': '256k FRAM nonvolatile memory, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('Memory_NVRAM : FM18W08-SG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

