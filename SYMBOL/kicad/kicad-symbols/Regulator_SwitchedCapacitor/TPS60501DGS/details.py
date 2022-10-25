
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "TPS60501DGS"
    hexID = "SZKREGULATORSWITCHEDCAPACITORTPS651DGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS60500DGS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS60501DGS', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps60503.pdf', 'kicadSymbolki_keywords': 'Regulator Step-Down Charge Pump TPS Texas Instruments Ti', 'kicadSymbolki_description': '250mA High-Efficiency Step-Down Charge Pump Regulator, 3.3V Output Voltage, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : TPS60501DGS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

