
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "LT6106"
    hexID = "SZKAMPLIFIERCURRENTLT616"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT6106', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6106fb.pdf', 'kicadSymbolki_keywords': 'current sense', 'kicadSymbolki_description': '36V Low Cost, High Side Current Sense, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Amplifier_Current : LT6106')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

