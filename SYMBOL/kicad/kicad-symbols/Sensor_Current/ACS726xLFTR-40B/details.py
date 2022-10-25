
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS726xLFTR-40B"
    hexID = "SZKSENCURRENTACS726XLFTR4B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS726xLFTR-20B', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS726xLFTR-40B', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS726-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±40A Bidirectional Hall-Effect Current Sensor, +3.3V supply, 50mV/A, QSOP-24', 'kicadSymbolki_fp_filters': 'Allegro*QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Sensor_Current : ACS726xLFTR-40B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

