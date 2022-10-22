
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "DZ2S039X0L"
    hexID = "SZKDIODEDZ2S39XL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DZ2S039X0L', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-523', 'kicadSymbolDatasheet': 'https://industrial.panasonic.com/content/data/SC/ds/ds4/DZ2S03900L_E.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '150mW Silicon Planar Zener Diode, 3.9V, SOD-523', 'kicadSymbolki_fp_filters': 'D?SOD?523*'}])
    newPart['name'].append('DZ2S039X0L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

