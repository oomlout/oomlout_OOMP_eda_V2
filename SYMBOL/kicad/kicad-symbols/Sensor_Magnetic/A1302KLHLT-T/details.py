
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "A1302KLHLT-T"
    hexID = "SZKSENMAGNETICA132KLHLTT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A1301KLHLT-T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A1302KLHLT-T', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23W', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A1301-2-Datasheet.ashx', 'kicadSymbolki_keywords': 'hall switch', 'kicadSymbolki_description': 'Linear Hall Effect Sensor, SOT-23W', 'kicadSymbolki_fp_filters': 'SOT?23W*'}])
    newPart['name'].append('A1302KLHLT-T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

