
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS711xLCTR-25AB"
    hexID = "SZKSENCURRENTACS711XLCTR25AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS711xLCTR-12AB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS711xLCTR-25AB', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/Media/Files/Datasheets/ACS711-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±25A, Bidirectional, Hall-Effect Current Sensor, +3.3V supply, 55mV/A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS711xLCTR-25AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

