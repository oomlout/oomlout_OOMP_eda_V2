
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "Si7141DP"
    hexID = "SZKTRANSISTORFETSI7141DP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Si7141DP', 'kicadSymbolFootprint': 'Package_SO:PowerPAK_SO-8_Single', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/65596/si7141dp.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '60A Id, 20V Vds, 1.9 mOhm Ron, PowerPAK-8', 'kicadSymbolki_fp_filters': 'PowerPAK*SO*Single*'}])
    newPart['name'].append('Si7141DP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

