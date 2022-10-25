
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS770xCB-150B-PFF"
    hexID = "SZKSENCURRENTACS77XCB15BPFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS756xCB-050B-PFF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS770xCB-150B-PFF', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_CB_PFF', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±50A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 13.3mV/A, CB-5 PFF', 'kicadSymbolki_fp_filters': 'Allegro*CB*PFF*'}])
    newPart['name'].append('Sensor_Current : ACS770xCB-150B-PFF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

