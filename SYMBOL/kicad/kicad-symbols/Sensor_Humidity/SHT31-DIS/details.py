
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "SHT31-DIS"
    hexID = "SZKSENHUMIDITYSHT31DIS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SHT31-DIS', 'kicadSymbolFootprint': 'Sensor_Humidity:Sensirion_DFN-8-1EP_2.5x2.5mm_P0.5mm_EP1.1x1.7mm', 'kicadSymbolDatasheet': 'https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Datasheets/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf', 'kicadSymbolki_keywords': 'digital temperature humidity i2c', 'kicadSymbolki_description': 'I²C humidity and temperature sensor, ±2%RH, ±0.2°C, DFN-8', 'kicadSymbolki_fp_filters': 'Sensirion*DFN*1EP*2.5x2.5mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Humidity : SHT31-DIS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

