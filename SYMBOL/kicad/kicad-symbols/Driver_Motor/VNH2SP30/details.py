
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "VNH2SP30"
    hexID = "SZKDRIVERMOTORVNH2SP3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VNH2SP30', 'kicadSymbolFootprint': 'Package_SO:ST_MultiPowerSO-30', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/group2/66/b8/f5/2c/9a/66/41/c7/CD00043711/files/CD00043711.pdf/jcr:content/translations/en.CD00043711.pdf', 'kicadSymbolki_keywords': 'full-bridge h-bridge', 'kicadSymbolki_description': 'Full Bridge Motor Driver, 41V, 30A, -40 to 150C', 'kicadSymbolki_fp_filters': 'ST*MultiPowerSO*'}])
    newPart['name'].append('Driver_Motor : VNH2SP30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

