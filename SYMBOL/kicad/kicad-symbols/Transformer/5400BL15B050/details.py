
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "5400BL15B050"
    hexID = "SZKTR54BL15B5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '5400BL15B050', 'kicadSymbolFootprint': 'RF_Converter:Balun_Johanson_5400BL15B050E', 'kicadSymbolDatasheet': 'https://www.johansontechnology.com/datasheets/5400BL15B050/5400BL15B050.pdf', 'kicadSymbolki_keywords': 'balun rf transformer', 'kicadSymbolki_description': '4.9-5.9GHz 1:1 RF Transformer, Unbalanced to Balanced', 'kicadSymbolki_fp_filters': 'Balun*Johanson*5400BL15B050E*'}])
    newPart['name'].append('Transformer : 5400BL15B050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

