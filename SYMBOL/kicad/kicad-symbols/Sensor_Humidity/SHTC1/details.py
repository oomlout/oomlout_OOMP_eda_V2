
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Humidity"
    oIndex = "SHTC1"
    hexID = "SZKSENHUMIDITYSHTC1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SHTC1', 'kicadSymbolFootprint': 'Sensor_Humidity:Sensirion_DFN-4-1EP_2x2mm_P1mm_EP0.7x1.6mm', 'kicadSymbolDatasheet': 'https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHTC1_Datasheet.pdf', 'kicadSymbolki_keywords': 'Sensirion environment environmental measurement digital', 'kicadSymbolki_description': 'Humidity and Temperature Sensor, +/-3%RH, +/-0.3degC, I2C, 1.62-1.98V, DFN-4', 'kicadSymbolki_fp_filters': 'Sensirion*DFN*1EP*2x2mm*P1mm*EP0.7x1.6mm*'}])
    newPart['name'].append('SHTC1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

