
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS780xLRTR-050B"
    hexID = "SZKSENCURRENTACS78XLRTR5B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS780xLRTR-050B', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_PSOF-7_4.8x6.4mm_P1.60mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS780-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±50A Bidirectional Hall-Effect Current Sensor, +5.0V supply, 40mV/A, PSOF-7', 'kicadSymbolki_fp_filters': 'Allegro*PSOF*4.8x6.4mm*P1.60mm*'}])
    newPart['name'].append('ACS780xLRTR-050B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

