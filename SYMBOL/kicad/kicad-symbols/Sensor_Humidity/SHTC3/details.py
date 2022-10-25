
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "SHTC3"
    hexID = "SZKSENHUMIDITYSHTC3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SHTC1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SHTC3', 'kicadSymbolFootprint': 'Sensor_Humidity:Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm', 'kicadSymbolDatasheet': 'https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHTC3_Datasheet.pdf', 'kicadSymbolki_keywords': 'Sensirion environment environmental measurement digital', 'kicadSymbolki_description': 'Humidity and Temperature Sensor, +/-2%RH, +/-0.2degC, I2C, 1.62-3.6V, DFN-4', 'kicadSymbolki_fp_filters': 'Sensirion*DFN*1EP*2x2mm*P1mm*EP0.7x1.6mm*'}])
    newPart['name'].append('Sensor_Humidity : SHTC3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

