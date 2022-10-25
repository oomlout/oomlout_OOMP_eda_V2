
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Z1SMAxxx"
    hexID = "SZKDIODEZ1SXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Z1SMAxxx', 'kicadSymbolFootprint': 'Diode_SMD:D_SMA', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/z1sma1.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '1000mW Zener Diode, SMA(DO-214AC)', 'kicadSymbolki_fp_filters': 'D?SMA*'}])
    newPart['name'].append('Diode : Z1SMAxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

