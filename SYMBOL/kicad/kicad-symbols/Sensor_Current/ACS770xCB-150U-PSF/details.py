
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS770xCB-150U-PSF"
    hexID = "SZKSENCURRENTACS77XCB15UPSF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS758xCB-100B-PSF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS770xCB-150U-PSF', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_CB_PSF', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS758-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '50A Unidirectional Hall-Effect Current Sensor, +5.0V supply, 26.7mV/A, CB-5 PSF', 'kicadSymbolki_fp_filters': 'Allegro*CB*PSF*'}])
    newPart['name'].append('Sensor_Current : ACS770xCB-150U-PSF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

