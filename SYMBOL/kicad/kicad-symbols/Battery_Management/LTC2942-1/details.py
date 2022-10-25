
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC2942-1"
    hexID = "SZKBATMANAGEMENTLTC29421"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC2942', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC2942-1', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6-1EP_3x2mm_P0.5mm_EP1.65x1.35mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/29421f.pdf', 'kicadSymbolki_keywords': 'Fuel gauge coulomb counter I2C', 'kicadSymbolki_description': '1A Battery Gas Gauge with Internal Sense Resistor and Temperature/Voltage Measurement, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : LTC2942-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

