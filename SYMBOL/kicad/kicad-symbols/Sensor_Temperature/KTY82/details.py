
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "KTY82"
    hexID = "SZKSENTEMPERATUREKTY82"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'KTY82', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/KTY82_SER.pdf', 'kicadSymbolki_keywords': 'silicon temperature sensors', 'kicadSymbolki_description': 'KTY82 series silicon temperature sensors, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Sensor_Temperature : KTY82')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

