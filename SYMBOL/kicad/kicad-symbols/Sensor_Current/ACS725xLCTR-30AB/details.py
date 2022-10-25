
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS725xLCTR-30AB"
    hexID = "SZKSENCURRENTACS725XLCTR3AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS712xLCTR-05B', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS725xLCTR-30AB', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS725-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±30A Bidirectional Hall-Effect Current Sensor, +3.3V supply, 44mV/A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9m*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS725xLCTR-30AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

