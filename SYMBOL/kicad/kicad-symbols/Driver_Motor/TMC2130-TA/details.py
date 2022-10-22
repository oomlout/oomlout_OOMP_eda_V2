
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TMC2130-TA"
    hexID = "SZKDRIVERMOTORTMC213TA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMC2130-TA', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm', 'kicadSymbolDatasheet': 'http://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2130_datasheet.pdf', 'kicadSymbolki_keywords': 'stepper motor driver', 'kicadSymbolki_description': 'Driver for two-phase bipolar stepper motor, 2.0A, SPI, 4.75-46V, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('TMC2130-TA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

