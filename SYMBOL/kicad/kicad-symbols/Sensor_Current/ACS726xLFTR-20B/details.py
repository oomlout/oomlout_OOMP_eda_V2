
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS726xLFTR-20B"
    hexID = "SZKSENCURRENTACS726XLFTR2B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS726xLFTR-20B', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS726-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±20A Bidirectional Hall-Effect Current Sensor, +3.3V supply, 100mV/A, QSOP-24', 'kicadSymbolki_fp_filters': 'Allegro*QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('ACS726xLFTR-20B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

