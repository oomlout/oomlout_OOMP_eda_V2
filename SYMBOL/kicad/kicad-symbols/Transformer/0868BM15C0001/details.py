
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "0868BM15C0001"
    hexID = "SZKTR868BM15C1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '0896BM15A0001', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '0868BM15C0001', 'kicadSymbolFootprint': 'RF_Converter:Balun_Johanson_0896BM15A0001', 'kicadSymbolDatasheet': 'https://www.johansontechnology.com/datasheets/0868BM15C0001/0868BM15C0001.pdf', 'kicadSymbolki_keywords': 'balun rf transformer', 'kicadSymbolki_description': '863-873MHz 1:1 RF Transformer, Unbalanced to Balanced, with integrated DC blocking capacitor', 'kicadSymbolki_fp_filters': 'Balun*Johanson*0896BM15A0001*'}])
    newPart['name'].append('Transformer : 0868BM15C0001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

