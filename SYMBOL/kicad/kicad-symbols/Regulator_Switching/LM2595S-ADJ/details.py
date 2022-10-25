
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2595S-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2595SADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2595S-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2595S-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/lm2595.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 1A Adjustable', 'kicadSymbolki_description': 'Adjustable Output 1A Step-Down Voltage Regulator, TO-263-5', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Switching : LM2595S-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

