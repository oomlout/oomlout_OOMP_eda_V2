
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM385M-ADJ"
    hexID = "SZKREFERENCEVOLTAGELM385MADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM285M-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM385M-ADJ', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm185-adj.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference', 'kicadSymbolki_description': 'Adjustable Micropower Voltage Reference Diodes, SO-8', 'kicadSymbolki_fp_filters': 'SOIC?8*3.9x4.9m*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : LM385M-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

