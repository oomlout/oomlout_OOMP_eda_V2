
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "PHA-23HLN"
    hexID = "SZKRFAMPLIFIERPHA23HLN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPF5189Z', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PHA-23HLN', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/PHA-23HLN+.pdf', 'kicadSymbolki_keywords': 'RF amplifier', 'kicadSymbolki_description': '30-2000MHz +21.3dB Low Noise Amplifier, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('RF_Amplifier : PHA-23HLN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

