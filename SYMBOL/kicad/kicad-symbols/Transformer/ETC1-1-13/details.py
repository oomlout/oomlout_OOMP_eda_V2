
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "ETC1-1-13"
    hexID = "SZKTRETC1113"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'ETC1-1-13', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_MACOM_SM-22', 'kicadSymbolDatasheet': 'https://cdn.macom.com/datasheets/ETC1-1-13.pdf', 'kicadSymbolki_keywords': 'MACOM RF Transformer', 'kicadSymbolki_description': '4.5-4000MHz 1:1 RF Transformer, Balanced Transmission Line, SM-22', 'kicadSymbolki_fp_filters': 'Transformer*MACOM*SM?22*'}])
    newPart['name'].append('ETC1-1-13')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

