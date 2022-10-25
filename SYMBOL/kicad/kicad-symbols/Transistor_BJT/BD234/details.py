
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD234"
    hexID = "SZKTRANSISTORBJTBD234"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD140', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD234', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'http://www.electronica-pt.com/datasheets/bd/BD234.pdf', 'kicadSymbolki_keywords': 'Low Voltage Transistor', 'kicadSymbolki_description': '2A Ic, 45V Vce, Low Voltage Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BD234')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

