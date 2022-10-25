
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM22678TJ-5"
    hexID = "SZKREGULATORSWITCHINGLM22678TJ5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM22678TJ-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM22678TJ-5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin8', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm22678.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Converter 5A', 'kicadSymbolki_description': '5A Step-Down Switching Voltage Regulater, 4.5-42V Input, 5V Output, 500kHz Switching Frequency, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Switching : LM22678TJ-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

