
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "ZYxxx"
    hexID = "SZKDIODEZYXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZYxxx', 'kicadSymbolFootprint': 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/zy1', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '2000mW Zener Diode, DO-41', 'kicadSymbolki_fp_filters': 'D*DO?41*'}])
    newPart['name'].append('Diode : ZYxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

