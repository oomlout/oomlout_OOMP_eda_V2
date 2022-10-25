
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2235"
    hexID = "SZKDRIVERFETIR2235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2133', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2235', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IR2x33-IR2x35-DataSheet-v01_00-EN.pdf?fileId=5546d462533600a4015355c890ba169f', 'kicadSymbolki_keywords': '3 Phase Gate Driver', 'kicadSymbolki_description': '1200V, Vout 12-20V, PDIP-28', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Driver_FET : IR2235')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

