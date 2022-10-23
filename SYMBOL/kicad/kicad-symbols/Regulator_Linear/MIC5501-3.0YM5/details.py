
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5501-3.0YM5"
    hexID = "SZKREGULATORLINEARMIC5513YM5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC5504-3.3YM5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5501-3.0YM5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MIC550X.pdf', 'kicadSymbolki_keywords': 'Micrel LDO voltage regulator', 'kicadSymbolki_description': '300mA Low-dropout Voltage Regulator, Vout 3.0V, Vin up to 5.5V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23?5*'}])
    newPart['name'].append('MIC5501-3.0YM5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

