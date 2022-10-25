
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IRS2008S"
    hexID = "SZKDRIVERFETIRS28S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR25602S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IRS2008S', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IRS2008S-DS-v01_00-EN.pdf?fileId=5546d46259d9a4bf015a3e76b6361c1a', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': '200-V Half-Bridge Driver With Shutdown Input, 200V, 290/600mA, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : IRS2008S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

