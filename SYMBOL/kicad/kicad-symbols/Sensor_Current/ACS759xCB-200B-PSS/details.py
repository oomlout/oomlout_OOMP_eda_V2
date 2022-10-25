
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS759xCB-200B-PSS"
    hexID = "SZKSENCURRENTACS759XCB2BPSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS758xCB-150B-PSS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS759xCB-200B-PSS', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_CB_PSS', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS759-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±200A Bidirectional Hall-Effect Current Sensor, +3.3V supply, 6.6mV/A, CB-5 PSS', 'kicadSymbolki_fp_filters': 'Allegro*CB*PSS*'}])
    newPart['name'].append('Sensor_Current : ACS759xCB-200B-PSS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

