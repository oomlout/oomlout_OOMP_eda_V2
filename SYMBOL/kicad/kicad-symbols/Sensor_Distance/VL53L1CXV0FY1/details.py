
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Distance"
    oIndex = "VL53L1CXV0FY1"
    hexID = "SZKSENDISTANCEVL53L1CXVFY1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VL53L1CXV0FY1', 'kicadSymbolFootprint': 'Sensor_Distance:ST_VL53L1x', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/vl53l1x.pdf', 'kicadSymbolki_keywords': 'VL53L1x ToF', 'kicadSymbolki_description': '4m distance ranging ToF sensor', 'kicadSymbolki_fp_filters': 'ST*VL53L1x*'}])
    newPart['name'].append('VL53L1CXV0FY1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

