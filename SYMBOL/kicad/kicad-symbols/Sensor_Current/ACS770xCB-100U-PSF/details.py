
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS770xCB-100U-PSF"
    hexID = "SZKSENCURRENTACS77XCB1UPSF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS758xCB-100B-PSF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS770xCB-100U-PSF', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_CB_PSF', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '100A Unidirectional Hall-Effect Current Sensor, +5.0V supply, 40mV/A, CB-5 PSF', 'kicadSymbolki_fp_filters': 'Allegro*CB*PSF*'}])
    newPart['name'].append('ACS770xCB-100U-PSF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

