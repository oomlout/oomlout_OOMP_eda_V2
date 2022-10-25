
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2576T-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2576TADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVT-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2576T-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2576.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 3A Adjustable', 'kicadSymbolki_description': 'Adjustable Output Voltage, 3A SIMPLE SWITCHER® Step-Down Voltage Regulator, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Regulator_Switching : LM2576T-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

