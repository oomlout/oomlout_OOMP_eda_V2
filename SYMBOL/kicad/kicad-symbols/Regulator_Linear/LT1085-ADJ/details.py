
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1085-ADJ"
    hexID = "SZKREGULATORLINEARLT185ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1084-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1085-ADJ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/108345fh.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator Adjustable 3.0A Positive LDO', 'kicadSymbolki_description': '3.0A 25V LDO Linear Regulator, Adjustable Output, TO-220/TO-263', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('Regulator_Linear : LT1085-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

