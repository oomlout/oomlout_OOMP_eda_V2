
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D1P7060Q"
    hexID = "SZKDIODEC3D1P76Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D1P7060Q', 'kicadSymbolFootprint': 'Diode_SMD:D_QFN_3.3x3.3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/846/C3D1P7060Q.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '600V, 1.7A, SiC Schottky Diode, QFN', 'kicadSymbolki_fp_filters': 'D*QFN*3.3x3.3mm*P0.65mm*'}])
    newPart['name'].append('C3D1P7060Q')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

