
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "KTY84"
    hexID = "SZKSENTEMPERATUREKTY84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'KTY83', 'kicadSymbolReference': 'TH', 'kicadSymbolValue': 'KTY84', 'kicadSymbolFootprint': 'Diode_THT:D_DO-34_SOD68_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'http://cache.nxp.com/documents/data_sheet/KTY84_SER.pdf?pspll=1', 'kicadSymbolki_keywords': 'silicon temperature sensor diode', 'kicadSymbolki_description': 'KTY84 series silicon temperature sensors, polarized, SOD68', 'kicadSymbolki_fp_filters': '*DO?34*SOD68*'}])
    newPart['name'].append('KTY84')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

