
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N53xxB"
    hexID = "SZKDIODE1N53XXB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N53xxB', 'kicadSymbolFootprint': 'Diode_THT:D_DO-201_P15.24mm_Horizontal', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/1n5345b.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '5000mW Zener Diode, DO-201', 'kicadSymbolki_fp_filters': 'D*DO?201*'}])
    newPart['name'].append('Diode : 1N53xxB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

