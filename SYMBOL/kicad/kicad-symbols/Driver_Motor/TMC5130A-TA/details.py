
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "TMC5130A-TA"
    hexID = "SZKDRIVERMOTORTMC513ATA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMC5130A-TA', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48-1EP_7x7mm_P0.5mm_EP5x5mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC5130_datasheet_Rev1.17.pdf', 'kicadSymbolki_keywords': 'Standalone driver stepper motor', 'kicadSymbolki_description': 'Power Driver For Stepper Motors, 2.0A, 4.75-46V, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('TMC5130A-TA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

