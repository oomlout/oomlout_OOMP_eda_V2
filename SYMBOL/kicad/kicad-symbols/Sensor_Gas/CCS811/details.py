
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Gas"
    oIndex = "CCS811"
    hexID = "SZKSENGASCCS811"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CCS811', 'kicadSymbolFootprint': 'Package_LGA:AMS_LGA-10-1EP_2.7x4mm_P0.6mm', 'kicadSymbolDatasheet': 'http://ams.com/eng/Products/Environmental-Sensors/Air-Quality-Sensors/CCS811', 'kicadSymbolki_keywords': 'metal oxide gas sensor MOX volatile organix comounds VOC I2C', 'kicadSymbolki_description': 'Ultra-low power digital gas sensor for monitoring indoor air quality', 'kicadSymbolki_fp_filters': 'AMS?LGA*EP*2.7x4mm*P0.6mm*'}])
    newPart['name'].append('CCS811')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

