
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS780xLRTR-100B"
    hexID = "SZKSENCURRENTACS78XLRTR1B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS780xLRTR-050B', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS780xLRTR-100B', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_PSOF-7_4.8x6.4mm_P1.60mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS780-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±100A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 20mV/A, PSOF-7', 'kicadSymbolki_fp_filters': 'Allegro*PSOF*4.8x6.4mm*P1.60mm*'}])
    newPart['name'].append('Sensor_Current : ACS780xLRTR-100B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

