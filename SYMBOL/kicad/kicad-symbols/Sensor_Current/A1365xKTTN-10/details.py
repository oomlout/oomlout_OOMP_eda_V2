
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "A1365xKTTN-10"
    hexID = "SZKSENCURRENTA1365XKTTN1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1365xKTTN-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1365xKTTN-10', 'kicadSymbolFootprint': 'Sensor_Current:Allegro_SIP-4', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1365-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': 'Programmable Linear Hall Effect Sensor, +6.4 to +14mV/G, SIP-4', 'kicadSymbolki_fp_filters': 'Allegro*SIP*'}])
    newPart['name'].append('A1365xKTTN-10')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

