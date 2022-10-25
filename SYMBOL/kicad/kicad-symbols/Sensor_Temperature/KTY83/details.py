
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "KTY83"
    hexID = "SZKSENTEMPERATUREKTY83"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'KTY83', 'kicadSymbolFootprint': 'Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/KTY83_SER.pdf', 'kicadSymbolki_keywords': 'silicon temperature sensors diode', 'kicadSymbolki_description': 'KTY83 series silicon temperature sensors, polarized, SOD68', 'kicadSymbolki_fp_filters': '*DO?34*SOD68*'}])
    newPart['name'].append('Sensor_Temperature : KTY83')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

