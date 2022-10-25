
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NID60S24-12"
    hexID = "SZKREGULATORSWITCHINGNID6S2412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NID60S24-05', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NID60S24-12', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_MeanWell_NID60_THT', 'kicadSymbolDatasheet': 'http://www.meanwell.com/78ddf876-a86c-4a52-8a41-4ee24dd9913d', 'kicadSymbolki_keywords': 'Step-Down Converter Module DC/DC', 'kicadSymbolki_description': '4A/48W Step Down Converter Module, fixed 12V Output Voltage, 250kHz, 20-53V Input Voltage', 'kicadSymbolki_fp_filters': 'Converter*DCDC*MeanWell*NID60*'}])
    newPart['name'].append('Regulator_Switching : NID60S24-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

