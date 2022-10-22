
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STBR3012WY"
    hexID = "SZKDIODESTBR312WY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STBR3008WY', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STBR3012WY', 'kicadSymbolFootprint': 'Diode_THT:D_DO-247_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stbr3012-y.pdf', 'kicadSymbolki_keywords': 'AEC-Q101', 'kicadSymbolki_description': '1200V, 30A, General Purpose Rectifier Diode, DO-247', 'kicadSymbolki_fp_filters': 'D*DO*247*'}])
    newPart['name'].append('STBR3012WY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

