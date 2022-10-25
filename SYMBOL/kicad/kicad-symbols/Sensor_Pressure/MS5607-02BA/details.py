
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MS5607-02BA"
    hexID = "SZKSENPRESSUREMS5672BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MS5607-02BA', 'kicadSymbolFootprint': 'Package_LGA:LGA-8_3x5mm_P1.25mm', 'kicadSymbolDatasheet': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FMS5607-02BA03%7FB2%7Fpdf%7FEnglish%7FENG_DS_MS5607-02BA03_B2.pdf%7FCAT-BLPS0035', 'kicadSymbolki_keywords': 'pressure SPI I2C', 'kicadSymbolki_description': 'Barometric pressure sensor, 20cm resolution, 10 to 1200 mbar, I2C and SPI interface up to 20MHz, LGA-8', 'kicadSymbolki_fp_filters': 'LGA*3x5mm*P1.25mm*'}])
    newPart['name'].append('Sensor_Pressure : MS5607-02BA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

