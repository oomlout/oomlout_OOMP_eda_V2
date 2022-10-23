
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "CSD25302Q2"
    hexID = "SZKTRANSISTORFETCSD2532Q2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'CSD25302Q2', 'kicadSymbolFootprint': 'Package_SON:Texas_DQK', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/slps234b/slps234b.pdf', 'kicadSymbolki_keywords': 'NexFET Power MOSFET P-MOS', 'kicadSymbolki_description': '5A Id, 20V Vds, NexFET P-Channel Power MOSFET, 39mOhm Ron, SON-6', 'kicadSymbolki_fp_filters': 'Texas*DQK*'}])
    newPart['name'].append('CSD25302Q2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

