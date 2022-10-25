
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS733xLATR-65AB"
    hexID = "SZKSENCURRENTACS733XLATR65AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS732xLATR-40AB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS733xLATR-65AB', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS732-ACS733-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±65A Unidirectional Hall-Effect Current Sensor, +3.3V supply, 20mV/A, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS733xLATR-65AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

