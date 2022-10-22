
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TMC2160"
    hexID = "SZKDRIVERMOTORTMC216"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMC2160', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm', 'kicadSymbolDatasheet': 'https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2160A-datasheet_Rev1.06.pdf', 'kicadSymbolki_keywords': 'Standalone driver stepper motor', 'kicadSymbolki_description': 'Standalone driver for two-phase bipolar stepper motor, 8-60V, external FETs, TQFP48', 'kicadSymbolki_fp_filters': 'TQFP*1EP?7x7mm*P0.5mm*'}])
    newPart['name'].append('TMC2160')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

