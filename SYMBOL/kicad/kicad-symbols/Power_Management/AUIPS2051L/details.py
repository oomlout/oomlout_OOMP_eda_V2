
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS2051L"
    hexID = "SZKPOWERMANAGEMENTAUIPS251L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS1051L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS2051L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-AUIPS2052G-DS-v01_00-EN.pdf?fileId=5546d4625a888733015aae0b6fb04c51', 'kicadSymbolki_keywords': 'low side switch', 'kicadSymbolki_description': 'Intelligent Power Low Side Switch, 70V, 1.8A, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Power_Management : AUIPS2051L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

