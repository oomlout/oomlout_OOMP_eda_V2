
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS724xLCTR-10AB"
    hexID = "SZKSENCURRENTACS724XLCTR1AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS712xLCTR-05B', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS724xLCTR-10AB', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS724-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±10A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 200mV/A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9m*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS724xLCTR-10AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

