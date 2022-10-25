
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5356-MMYML"
    hexID = "SZKREGULATORLINEARMIC5356YML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5356-MMYML', 'kicadSymbolFootprint': 'Package_DFN_QFN:MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf', 'kicadSymbolki_keywords': 'Dual LDO 500mA DFN-8', 'kicadSymbolki_description': 'Dual 500mA μCap Low Dropout Micropower Linear Regulator, 2.8V/2.8V, DFN-8', 'kicadSymbolki_fp_filters': 'MLF*3x3mm*P0.65mm*EP1.55x2.3mm*'}])
    newPart['name'].append('Regulator_Linear : MIC5356-MMYML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

