
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTM4637xY"
    hexID = "SZKREGULATORSWITCHINGLTM4637XY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTM4637xY', 'kicadSymbolFootprint': 'Package_BGA:Linear_BGA-133_15.0x15.0mm_Layout12x12_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf', 'kicadSymbolki_keywords': 'uModule DCDC', 'kicadSymbolki_description': '20A DC/DC µModule Step-Down Regulator, BGA-133', 'kicadSymbolki_fp_filters': 'Linear*BGA*15.0x15.0mm*Layout12x12*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LTM4637xY')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

