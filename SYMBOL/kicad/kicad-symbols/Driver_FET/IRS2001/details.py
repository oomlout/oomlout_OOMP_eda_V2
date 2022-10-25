
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS2001"
    hexID = "SZKDRIVERFETIRS21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2101', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2001', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2001pbf.pdf?fileId=5546d462533600a401535675a760277e', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'High and Low Side Driver, 200V, 200/420mA, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IRS2001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

