
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "NCS20071XV"
    hexID = "SZKAMPLIFIEROPERATIONALNCS271XV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS20071XV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-553', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCS20071-D.PDF', 'kicadSymbolki_keywords': 'OpAmp Rail-to-rail Output Single vfa', 'kicadSymbolki_description': 'Single, 2.8V/µs, Rail-to-Rail Output, SOT-553', 'kicadSymbolki_fp_filters': 'SOT?553*'}])
    newPart['name'].append('Amplifier_Operational : NCS20071XV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

