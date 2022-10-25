
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STBR6012WY"
    hexID = "SZKDIODESTBR612WY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STBR3008WY', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STBR6012WY', 'kicadSymbolFootprint': 'Diode_THT:D_DO-247_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stbr6012-y.pdf', 'kicadSymbolki_keywords': 'AEC-Q101', 'kicadSymbolki_description': '1200V, 60A, General Purpose Rectifier Diode, DO-247', 'kicadSymbolki_fp_filters': 'D*DO*247*'}])
    newPart['name'].append('Diode : STBR6012WY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

