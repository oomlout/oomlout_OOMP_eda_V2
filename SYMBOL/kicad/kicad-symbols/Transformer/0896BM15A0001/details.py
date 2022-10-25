
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "0896BM15A0001"
    hexID = "SZKTR896BM15A1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '0896BM15A0001', 'kicadSymbolFootprint': 'RF_Converter:Balun_Johanson_0896BM15A0001', 'kicadSymbolDatasheet': 'https://www.johansontechnology.com/datasheets/0896BM15A0001/0896BM15A0001.pdf', 'kicadSymbolki_keywords': 'balun rf transformer', 'kicadSymbolki_description': '863-928MHz 1:1 RF Transformer, Unbalanced to Balanced', 'kicadSymbolki_fp_filters': 'Balun*Johanson*0896BM15A0001*'}])
    newPart['name'].append('Transformer : 0896BM15A0001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

