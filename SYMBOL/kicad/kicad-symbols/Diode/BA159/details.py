
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BA159"
    hexID = "SZKDIODEBA159"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BA159', 'kicadSymbolFootprint': 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/88536/ba157.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '1000V 1A Fast recovery Rectifier Diode, DO-41', 'kicadSymbolki_fp_filters': 'D*DO?41*'}])
    newPart['name'].append('Diode : BA159')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

