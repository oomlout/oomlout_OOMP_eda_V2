
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS711xEXLT-15AB"
    hexID = "SZKSENCURRENTACS711XEXLT15AB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS711xEXLT-15AB', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_QFN-12-10-1EP_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/Media/Files/Datasheets/ACS711-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±15A Bidirectional Hall-Effect Current Sensor, +3.3V supply, 90mV/A, QFN-12', 'kicadSymbolki_fp_filters': 'Allegro*QFN*EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Current : ACS711xEXLT-15AB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

