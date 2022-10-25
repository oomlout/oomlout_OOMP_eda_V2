
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BF244C"
    hexID = "SZKTRANSISTORFETBF244C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BF244A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BF244C', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Fairchild%20PDFs/BF244x.pdf', 'kicadSymbolki_keywords': 'N-Channel FET Transistor Low Voltage', 'kicadSymbolki_description': '10mA Id, 30V Vgs, N-Channel FET Transistor, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*'}])
    newPart['name'].append('Transistor_FET : BF244C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

