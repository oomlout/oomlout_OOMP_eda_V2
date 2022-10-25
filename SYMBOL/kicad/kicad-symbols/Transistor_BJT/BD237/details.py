
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BD237"
    hexID = "SZKTRANSISTORBJTBD237"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD139', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BD237', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-126-3_Vertical', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Micro%20Commercial%20PDFs/BD233,235,237.pdf', 'kicadSymbolki_keywords': 'Low Voltage Transistor', 'kicadSymbolki_description': '2A Ic, 80V Vce, Low Voltage Transistor, TO-126', 'kicadSymbolki_fp_filters': 'TO?126*'}])
    newPart['name'].append('Transistor_BJT : BD237')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

