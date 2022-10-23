
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MS5611-01BA"
    hexID = "SZKSENPRESSUREMS56111BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MS5607-02BA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MS5611-01BA', 'kicadSymbolFootprint': 'Package_LGA:LGA-8_3x5mm_P1.25mm', 'kicadSymbolDatasheet': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=MS5611-01BA03&DocType=Data+Sheet&DocLang=English', 'kicadSymbolki_keywords': 'pressure SPI I2C', 'kicadSymbolki_description': 'Barometric pressure sensor, 10cm resolution, 10 to 1200 mbar, I2C and SPI interface up to 20MHz, LGA-8', 'kicadSymbolki_fp_filters': 'LGA*3x5mm*P1.25mm*'}])
    newPart['name'].append('MS5611-01BA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

