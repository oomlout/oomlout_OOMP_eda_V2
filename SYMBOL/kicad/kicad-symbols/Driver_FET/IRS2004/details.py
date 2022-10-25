
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS2004"
    hexID = "SZKDRIVERFETIRS24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2104', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2004', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/irs2004pbf.pdf?fileId=5546d462533600a401535675b86b2782', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Driver, 200V, 290/600mA, PDIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Driver_FET : IRS2004')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

