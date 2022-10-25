
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "TS5A3159DCK"
    hexID = "SZKANALOGSWITCHTS5A3159DCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NC7SB3157P6X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TS5A3159DCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ts5a3159.pdf', 'kicadSymbolki_keywords': 'Analog Switch SPDT', 'kicadSymbolki_description': 'Single SPDT Analog Switch, 1.65-V to 5.5-V Single-Supply Operation, 1Ohm Ron, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Analog_Switch : TS5A3159DCK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

