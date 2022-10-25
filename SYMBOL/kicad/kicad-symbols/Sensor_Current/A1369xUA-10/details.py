
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "A1369xUA-10"
    hexID = "SZKSENCURRENTA1369XUA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1369xUA-10', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_SIP-3', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1369-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': 'Programmable Linear Hall Effect Sensor, -8.5 to -12.5mV/G, SIP-3', 'kicadSymbolki_fp_filters': 'Allegro*SIP*'}])
    newPart['name'].append('Sensor_Current : A1369xUA-10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

