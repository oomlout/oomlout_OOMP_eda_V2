
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM285Z-ADJ"
    hexID = "SZKREFERENCEVOLTAGELM285ZADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM285Z-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm185-adj.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference', 'kicadSymbolki_description': 'Adjustable Micropower Voltage Reference Diodes, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Reference_Voltage : LM285Z-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

