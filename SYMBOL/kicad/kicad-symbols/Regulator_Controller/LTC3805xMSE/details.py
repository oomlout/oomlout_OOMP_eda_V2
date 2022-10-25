
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LTC3805xMSE"
    hexID = "SZKREGULATORCONTROLLERLTC385XMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3805xMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3805fg.pdf', 'kicadSymbolki_keywords': 'flyback dc-dc switcher switching', 'kicadSymbolki_description': 'Adjustable Frequency current Mode Flyback DC/DC controller, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*10*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Controller : LTC3805xMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

