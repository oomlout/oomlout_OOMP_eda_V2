
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TL497A"
    hexID = "SZKREGULATORSWITCHINGTL497A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TL497', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL497A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl497a.pdf', 'kicadSymbolki_keywords': 'buck regulator', 'kicadSymbolki_description': '500mA step up/step down switching regulator', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x9.0mm*P1.27mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : TL497A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

