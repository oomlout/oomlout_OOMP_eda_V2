
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STBR3008WY"
    hexID = "SZKDIODESTBR38WY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STBR3008WY', 'kicadSymbolFootprint': 'Diode_THT:D_DO-247_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stbr3008-y.pdf', 'kicadSymbolki_keywords': 'AEC-Q101', 'kicadSymbolki_description': '800V, 30A, General Purpose Rectifier Diode, DO-247', 'kicadSymbolki_fp_filters': 'D*DO*247*'}])
    newPart['name'].append('STBR3008WY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

