
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "GVA-63"
    hexID = "SZKRFAMPLIFIERGVA63"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPF5189Z', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'GVA-63', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/GVA-63+.pdf', 'kicadSymbolki_keywords': 'RF amplifier', 'kicadSymbolki_description': '10-6000MHz +20dB Gain Block, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('RF_Amplifier : GVA-63')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

