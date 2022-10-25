
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C3M0075120K"
    hexID = "SZKTRANSISTORFETC3M7512K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0030090K', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C3M0075120K', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-4_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/959/c3m0075120k.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '30A Id, 1200V Vds, 75mOhm, N-Channel SiC MOSFET, TO-247-4', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Transistor_FET : C3M0075120K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

