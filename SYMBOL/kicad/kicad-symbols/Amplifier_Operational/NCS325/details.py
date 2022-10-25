
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS325"
    hexID = "SZKAMPLIFIEROPERATIONALNCS325"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS325', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCS325-D.PDF', 'kicadSymbolki_keywords': 'single opamp low-power', 'kicadSymbolki_description': 'Single operational amplifier, 50uV Offset, 0.25uV/C, 35uA Zero-Drift, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Operational : NCS325')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

