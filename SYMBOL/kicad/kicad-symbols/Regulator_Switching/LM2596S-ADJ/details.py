
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2596S-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2596SADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2596S-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2596S-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2596.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator Adjustable 3A', 'kicadSymbolki_description': 'Adjustable 3A Step-Down Voltage Regulator, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Switching : LM2596S-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

