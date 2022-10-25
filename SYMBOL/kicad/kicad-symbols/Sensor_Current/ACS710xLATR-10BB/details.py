
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Current"
    oIndex = "ACS710xLATR-10BB"
    hexID = "SZKSENCURRENTACS71XLATR1BB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ACS710xLATR-6BB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACS710xLATR-10BB', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/ACS710-Datasheet.ashx?la=en', 'kicadSymbolki_keywords': 'hall effect current monitor sensor isolated', 'kicadSymbolki_description': '±12A Bidirectional, Hall-Effect Current Sensor, Latched Fault, +3.3V to +5.0V supply, 85mV/A @ +5.0V, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Sensor_Current : ACS710xLATR-10BB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

