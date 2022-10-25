
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS758xCB-150B-PSS"
    hexID = "SZKSENCURRENTACS758XCB15BPSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS758xCB-150B-PSS', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_CB_PSS', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±150A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 13.3mV/A, CB-5 PSS', 'kicadSymbolki_fp_filters': 'Allegro*CB*PSS*'}])
    newPart['name'].append('Sensor_Current : ACS758xCB-150B-PSS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

