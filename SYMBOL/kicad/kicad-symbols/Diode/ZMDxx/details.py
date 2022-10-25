
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "ZMDxx"
    hexID = "SZKDIODEZMDXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZMDxx', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'http://diotec.com/tl_files/diotec/files/pdf/datasheets/zmd1', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '1000mW Zener Diode, MiniMELF', 'kicadSymbolki_fp_filters': 'D*MiniMELF*'}])
    newPart['name'].append('Diode : ZMDxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

