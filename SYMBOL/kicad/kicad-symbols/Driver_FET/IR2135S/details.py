
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2135S"
    hexID = "SZKDRIVERFETIR2135S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2133S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2135S', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IR2x33-IR2x35-DataSheet-v01_00-EN.pdf?fileId=5546d462533600a4015355c890ba169f', 'kicadSymbolki_keywords': '3 Phase Gate Driver', 'kicadSymbolki_description': '600V, Vout 12-20V, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : IR2135S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

