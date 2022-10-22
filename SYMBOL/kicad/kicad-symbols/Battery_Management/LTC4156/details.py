
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4156"
    hexID = "SZKBATMANAGEMENTLTC4156"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4156', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x5mm_P0.5mm_EP2.65x3.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4156fa.pdf', 'kicadSymbolki_keywords': 'lifepo charger PMIC USB', 'kicadSymbolki_description': 'Dual-Input Power Manager / 3.5A LiFePO4 Battery Charger with I2C Control and USB OTG, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x5mm*P0.5mm*'}])
    newPart['name'].append('LTC4156')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

