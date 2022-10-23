
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "MV317"
    hexID = "SZKOCSMV317"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MV317', 'kicadSymbolFootprint': 'Oscillator:Oscillator_OCXO_Morion_MV317', 'kicadSymbolDatasheet': 'https://www.morion-us.com/catalog_pdf/mv317.pdf', 'kicadSymbolki_keywords': 'OCXO', 'kicadSymbolki_description': '60, 80, 100, 120 & 122.76 MHz OCXO, Morion MV317', 'kicadSymbolki_fp_filters': 'Oscillator*OCXO*Morion*MV317*'}])
    newPart['name'].append('MV317')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

