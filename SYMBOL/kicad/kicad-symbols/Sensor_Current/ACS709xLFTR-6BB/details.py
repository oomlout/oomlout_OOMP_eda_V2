
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS709xLFTR-6BB"
    hexID = "SZKSENCURRENTACS79XLFTR6BB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS709xLFTR-6BB', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS709-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±15A Bidirectional, Hall-Effect Current Sensor, +3.3V to +5.0V supply, 90mV/A @ +3.3V, QSOP-24', 'kicadSymbolki_fp_filters': 'Allegro*QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Sensor_Current : ACS709xLFTR-6BB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

