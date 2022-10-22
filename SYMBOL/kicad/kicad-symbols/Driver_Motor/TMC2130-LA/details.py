
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TMC2130-LA"
    hexID = "SZKDRIVERMOTORTMC213LA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMC2130-LA', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.1mm', 'kicadSymbolDatasheet': 'http://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2130_datasheet.pdf', 'kicadSymbolki_keywords': 'stepper motor driver', 'kicadSymbolki_description': 'Driver for two-phase bipolar stepper motor, 2.0A, SPI, 4.75-46V, QFN-36', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x6mm*P0.5mm*'}])
    newPart['name'].append('TMC2130-LA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

