
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAS40-04"
    hexID = "SZKDIODEBAS44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAS40-04', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85701/bas40v.pdf', 'kicadSymbolki_keywords': 'Schottky, Diode', 'kicadSymbolki_description': '40V 0.2A Dual Small Signal Schottky Diodes', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Diode : BAS40-04')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

