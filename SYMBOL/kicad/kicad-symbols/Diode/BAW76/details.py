
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAW76"
    hexID = "SZKDIODEBAW76"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAW76', 'kicadSymbolFootprint': 'Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85551/baw76.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '50V 0.3A Small Signal Fast Switching Diode, DO-35', 'kicadSymbolki_fp_filters': 'D*DO?35*'}])
    newPart['name'].append('Diode : BAW76')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

