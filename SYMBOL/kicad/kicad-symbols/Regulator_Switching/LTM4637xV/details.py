
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTM4637xV"
    hexID = "SZKREGULATORSWITCHINGLTM4637XV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTM4637xV', 'kicadSymbolFootprint': 'Package_LGA:Linear_LGA-133_15.0x15.0mm_Layout12x12_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4637fc.pdf', 'kicadSymbolki_keywords': 'uModule DCDC', 'kicadSymbolki_description': '20A DC/DC µModule Step-Down Regulator, LGA-133', 'kicadSymbolki_fp_filters': 'Linear*LGA*15.0x15.0mm*Layout12x12*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LTM4637xV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

