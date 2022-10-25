
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5356-JGYMME"
    hexID = "SZKREGULATORLINEARMIC5356JGYE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC5355-S4YMME', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5356-JGYMME', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP2.5x3mm_Mask1.73x2.36mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf', 'kicadSymbolki_keywords': 'Dual LDO 500mA MSOP-8', 'kicadSymbolki_description': 'Dual 500mA μCap Low Dropout Micropower Linear Regulator, 2.5V/1.8V, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : MIC5356-JGYMME')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

