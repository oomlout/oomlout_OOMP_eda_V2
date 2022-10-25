
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "LM5109BSD"
    hexID = "SZKDRIVERFETLM519BSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5109ASD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5109BSD', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_4x4mm_P0.8mm_EP2.6x3mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5109b.pdf', 'kicadSymbolki_keywords': 'Half-Bridge Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Gate Driver, Output Current 1.0A, 100V, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('Driver_FET : LM5109BSD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

