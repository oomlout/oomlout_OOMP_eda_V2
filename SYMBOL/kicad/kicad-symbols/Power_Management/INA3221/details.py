
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "INA3221"
    hexID = "SZKPOWERMANAGEMENTINA3221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA3221', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RGV_S-PVQFN-N16_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina3221.pdf', 'kicadSymbolki_keywords': 'Shunt and Bus voltage monitor', 'kicadSymbolki_description': 'Triple-Channel High-Side Shunt and Bus Voltage Monitor with I2C and SMBUS Compatible Interface, QFN-16', 'kicadSymbolki_fp_filters': 'Texas*RGV*S?PVQFN*'}])
    newPart['name'].append('Power_Management : INA3221')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

