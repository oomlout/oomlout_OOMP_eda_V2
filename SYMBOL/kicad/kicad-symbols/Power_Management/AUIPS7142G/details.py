
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AUIPS7142G"
    hexID = "SZKPOWERMANAGEMENTAUIPS7142G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AUIPS7142G', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/auips7142g.pdf?fileId=5546d462533600a4015355a7ef451330', 'kicadSymbolki_keywords': 'dual high side switch', 'kicadSymbolki_description': 'Dual Channels Current Sense High Side Switch, 65V, 20A, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Power_Management : AUIPS7142G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

