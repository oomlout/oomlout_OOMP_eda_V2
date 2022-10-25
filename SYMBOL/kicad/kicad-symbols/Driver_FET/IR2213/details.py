
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2213"
    hexID = "SZKDRIVERFETIR2213"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2010', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2213', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IR2213-DS-v00_02-EN.pdf?fileId=5546d462533600a4015355c9621716d8', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'High and Low Side Driver, 1200V, 1.7/2.0A, PDIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IR2213')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

