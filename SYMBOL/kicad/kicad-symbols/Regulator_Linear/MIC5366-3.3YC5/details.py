
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5366-3.3YC5"
    hexID = "SZKREGULATORLINEARMIC536633YC5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC5365-3.3YC5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5366-3.3YC5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic5365.pdf', 'kicadSymbolki_keywords': 'Micrel LDO voltage regulator', 'kicadSymbolki_description': '150mA Low-dropout Voltage Regulator, Vout 3.3V, Output discharge circuit, Vin up to 5.5V, SC-70-5', 'kicadSymbolki_fp_filters': 'SOT*353*SC*70*'}])
    newPart['name'].append('MIC5366-3.3YC5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

