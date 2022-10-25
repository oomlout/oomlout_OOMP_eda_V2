
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2304"
    hexID = "SZKDRIVERFETIR234"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2304', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir2304.pdf?fileId=5546d462533600a4015355c9954a16e0', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Driver, 600V, 60/130mA, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IR2304')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

