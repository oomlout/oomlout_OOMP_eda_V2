
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TMC2100-LA"
    hexID = "SZKDRIVERMOTORTMC21LA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMC2100-LA', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.1mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2100_datasheet_Rev1.08.pdf', 'kicadSymbolki_keywords': 'Driver stepper motor', 'kicadSymbolki_description': 'Standalone driver for two-phase bipolar stepper motor, 2.0A, 4.75-46V, QFN-36', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x6mm*P0.5mm*'}])
    newPart['name'].append('TMC2100-LA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

