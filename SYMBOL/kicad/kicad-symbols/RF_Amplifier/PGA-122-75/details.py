
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "PGA-122-75"
    hexID = "SZKRFAMPLIFIERPGA12275"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPF5189Z', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PGA-122-75', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/PGA-122-75+.pdf', 'kicadSymbolki_keywords': 'RF amplifier', 'kicadSymbolki_description': '5-1500MHz +15.5dB CATV Amplifier, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('RF_Amplifier : PGA-122-75')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

