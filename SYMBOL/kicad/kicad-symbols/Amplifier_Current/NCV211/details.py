
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "NCV211"
    hexID = "SZKAMPLIFIERCURRENTNCV211"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS210', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCV211', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCS210R-D.PDF', 'kicadSymbolki_keywords': 'Current shunt monitor', 'kicadSymbolki_description': 'Current-Shunt Monitor, Voltage Output, Bi-Directional Zero-Drift, 500V/V Gain, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Amplifier_Current : NCV211')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

