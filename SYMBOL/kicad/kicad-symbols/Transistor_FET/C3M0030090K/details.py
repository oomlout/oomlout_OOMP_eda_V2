
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C3M0030090K"
    hexID = "SZKTRANSISTORFETC3M39K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C3M0030090K', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-4_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/1185/C3M0030090K.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '63A Id, 900V Vds, 30mOhm, N-Channel SiC MOSFET, TO-247-4', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Transistor_FET : C3M0030090K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

