
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS7091G"
    hexID = "SZKPOWERMANAGEMENTAUIPS791G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AUIPS6041G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS7091G', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips7091.pdf?fileId=5546d462533600a4015355a7c0d21322', 'kicadSymbolki_keywords': 'high side switch', 'kicadSymbolki_description': 'Intelligent Power High Side Switch, 70V, 5A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : AUIPS7091G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

