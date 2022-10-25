
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "KTY85"
    hexID = "SZKSENTEMPERATUREKTY85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'KTY85', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/other/SC17_GENERAL_TEMP_1996_3.pdf', 'kicadSymbolki_keywords': 'silicon temperature sensor diode', 'kicadSymbolki_description': 'KTY85 series silicon temperature sensors, polarized, SOD80', 'kicadSymbolki_fp_filters': 'SOD80*'}])
    newPart['name'].append('Sensor_Temperature : KTY85')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

