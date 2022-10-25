
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS5A3166DCKR"
    hexID = "SZKANALOGSWITCHTS5A3166DCKR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS5A3166DCKR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': ' http://www.ti.com/lit/ds/symlink/ts5a3166.pdf', 'kicadSymbolki_keywords': 'Analog Switch SPST', 'kicadSymbolki_description': 'Single SPST Analog Switch, 5-V/3.3-V, normally OFF, 0.9Ohm Ron, SC-70', 'kicadSymbolki_fp_filters': '*SC?70?5*'}])
    newPart['name'].append('Analog_Switch : TS5A3166DCKR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

