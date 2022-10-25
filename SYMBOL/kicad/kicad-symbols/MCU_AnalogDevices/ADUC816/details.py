
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_AnalogDevices"
    oIndex = "ADUC816"
    hexID = "SZKMCUANALOGDEVICESADUC816"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADUC816', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/ADUC816.pdf', 'kicadSymbolki_keywords': '8051 CORE MCU ADC DAC', 'kicadSymbolki_description': '8KB Flash, 256B SRAM, 640B EEPROM, 16-bit ADC, 12-bit DAC, MQFP-52', 'kicadSymbolki_fp_filters': 'MQFP*'}])
    newPart['name'].append('MCU_AnalogDevices : ADUC816')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

