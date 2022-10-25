
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS712xLCTR-20A"
    hexID = "SZKSENCURRENTACS712XLCTR2A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS712xLCTR-05B', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS712xLCTR-20A', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS712-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±20A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 100mV/A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9m*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS712xLCTR-20A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

