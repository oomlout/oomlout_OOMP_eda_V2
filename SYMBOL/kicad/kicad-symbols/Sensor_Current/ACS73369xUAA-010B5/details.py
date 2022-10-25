
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS73369xUAA-010B5"
    hexID = "SZKSENCURRENTACS73369XUAA1B5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1369xUA-10', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS73369xUAA-010B5', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_SIP-3', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS73369-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': 'Programmable Linear Hall Effect Sensor, +9 to +13.5mV/G, SIP-3', 'kicadSymbolki_fp_filters': 'Allegro*SIP*'}])
    newPart['name'].append('Sensor_Current : ACS73369xUAA-010B5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

