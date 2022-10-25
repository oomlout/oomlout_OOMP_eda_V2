
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS21864"
    hexID = "SZKDRIVERFETIRS21864"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR21814', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS21864', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2186pbf.pdf?fileId=5546d462533600a40153567716c427ed', 'kicadSymbolki_keywords': 'gate driver', 'kicadSymbolki_description': 'High and Low Side Driver, 600V, 4A, PDIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IRS21864')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

