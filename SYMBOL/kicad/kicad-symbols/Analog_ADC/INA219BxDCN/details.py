
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "INA219BxDCN"
    hexID = "SZKANALOGADCINA219BXDCN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA219AxDCN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA219BxDCN', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-8', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina219.pdf', 'kicadSymbolki_keywords': 'ADC I2C 16-Bit Oversampling Current Shunt', 'kicadSymbolki_description': 'Zero-Drift, HighAccuracy, Bidirectional Current/Power Monitor (0-26V) With I2C Interface, SOT-23-8', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Analog_ADC : INA219BxDCN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

