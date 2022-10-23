
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BUZ11"
    hexID = "SZKTRANSISTORFETBUZ11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BUZ11', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Fairchild%20PDFs/BUZ11.pdf', 'kicadSymbolki_keywords': 'N-Channel Power MOSFET', 'kicadSymbolki_description': '30A Id, 50V Vds, N-Channel Power MOSFET, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('BUZ11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

