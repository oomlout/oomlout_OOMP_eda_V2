
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "C3M0120100K"
    hexID = "SZKTRANSISTORFETC3M121K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3M0030090K', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'C3M0120100K', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-4_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/962/C3M0120100K.pdf', 'kicadSymbolki_keywords': 'N-Channel SiC MOSFET', 'kicadSymbolki_description': '22A Id, 1000V Vds, 120mOhm, N-Channel SiC MOSFET, TO-247-4', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('C3M0120100K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

