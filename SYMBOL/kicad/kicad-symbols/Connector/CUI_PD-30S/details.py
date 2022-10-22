
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "CUI_PD-30S"
    hexID = "SZKCNCUIPD3S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'CUI_PD-30S', 'kicadSymbolFootprint': 'Connector:CUI_PD-30S', 'kicadSymbolDatasheet': 'http://www.cui.com/product/resource/pd-30.pdf', 'kicadSymbolki_keywords': 'connector 3-pin PD-30S power DIN', 'kicadSymbolki_description': '3 pin connector, PD-30S', 'kicadSymbolki_fp_filters': 'CUI*PD*30S*'}])
    newPart['name'].append('CUI_PD-30S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

