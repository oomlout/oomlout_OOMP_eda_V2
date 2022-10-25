
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR21064"
    hexID = "SZKDRIVERFETIR2164"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR21064', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir2106.pdf?fileId=5546d462533600a4015355c7cfc51673', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'High and Low Side Driver, 600V, 200/350mA, PDIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IR21064')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

