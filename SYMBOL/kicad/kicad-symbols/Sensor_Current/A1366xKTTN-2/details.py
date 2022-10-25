
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "A1366xKTTN-2"
    hexID = "SZKSENCURRENTA1366XKTTN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1363xKTTN-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1366xKTTN-2', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_SIP-4', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1366-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': 'Programmable Linear Hall Effect Sensor, +2.5mV/G, SIP-4', 'kicadSymbolki_fp_filters': 'Allegro*SIP*'}])
    newPart['name'].append('Sensor_Current : A1366xKTTN-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

