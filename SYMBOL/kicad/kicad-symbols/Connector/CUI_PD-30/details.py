
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "CUI_PD-30"
    hexID = "SZKCNCUIPD3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'CUI_PD-30', 'kicadSymbolFootprint': 'Connector:CUI_PD-30', 'kicadSymbolDatasheet': 'http://www.cui.com/product/resource/pd-30.pdf', 'kicadSymbolki_keywords': 'connector 3-pin PD-30 power DIN', 'kicadSymbolki_description': '3 pin connector, PD-30', 'kicadSymbolki_fp_filters': 'CUI*PD*30*'}])
    newPart['name'].append('Connector : CUI_PD-30')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

