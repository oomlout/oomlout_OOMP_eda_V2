
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM2931-ADJ_TO92"
    hexID = "SZKREGULATORLINEARLM2931ADJTO92"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2931-ADJ_TO92', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2931-n.pdf', 'kicadSymbolki_keywords': 'REGULATOR LDO Adjustable', 'kicadSymbolki_description': '100mA Low drop-out regulator, Adjustable Output, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Regulator_Linear : LM2931-ADJ_TO92')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

