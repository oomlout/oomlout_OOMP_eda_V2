
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2SC1815"
    hexID = "SZKTRANSISTORBJT2SC1815"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2SC1815', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Toshiba%20PDFs/2SC1815.pdf', 'kicadSymbolki_keywords': 'Low Noise Audio NPN Transistor', 'kicadSymbolki_description': '0.15A Ic, 50V Vce, Low Noise Audio NPN Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_BJT : 2SC1815')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

