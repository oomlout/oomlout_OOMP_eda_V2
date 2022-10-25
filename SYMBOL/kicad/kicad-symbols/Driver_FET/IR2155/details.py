
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2155"
    hexID = "SZKDRIVERFETIR2155"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2153', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2155', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir2155.pdf?fileId=5546d462533600a4015355c8dec316b6', 'kicadSymbolki_keywords': 'Oscillating Gate Driver', 'kicadSymbolki_description': 'Self-Oscillating Half-Bridge Driver, 600V, 250/500mA, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IR2155')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

