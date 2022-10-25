
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BZX384xxxx"
    hexID = "SZKDIODEBZX384XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BZX384xxxx', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/85764/bzx384.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '300mW Zener Diode, SOD-323', 'kicadSymbolki_fp_filters': 'D*SOD*323*'}])
    newPart['name'].append('Diode : BZX384xxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

