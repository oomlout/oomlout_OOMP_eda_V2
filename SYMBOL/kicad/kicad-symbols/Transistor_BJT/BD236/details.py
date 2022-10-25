
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD236"
    hexID = "SZKTRANSISTORBJTBD236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD140', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD236', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'http://www.electronica-pt.com/datasheets/bd/BD234.pdf', 'kicadSymbolki_keywords': 'Low Voltage Transistor', 'kicadSymbolki_description': '60V Vce, 2A, Low Voltage Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BD236')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

