
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS709xLFTR-10BB"
    hexID = "SZKSENCURRENTACS79XLFTR1BB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS709xLFTR-6BB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS709xLFTR-10BB', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS709-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±24A Bidirectional, Hall-Effect Current Sensor, +3.3V to +5.0V supply, 85mV/A @ +3.3V, QSOP-24', 'kicadSymbolki_fp_filters': 'Allegro*QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('ACS709xLFTR-10BB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

