
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ25601"
    hexID = "SZKBATMANAGEMENTBQ2561"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ25601', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PWQFN-N24_EP2.7x2.7mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq25601.pdf', 'kicadSymbolki_keywords': 'LiPO charger', 'kicadSymbolki_description': 'I2C Controlled 3A Single-Cell Battery Charger for High Input Voltage and Narrow Voltage DC Power Path Management, WQFN-32', 'kicadSymbolki_fp_filters': 'Texas*S?PWQFN?N*EP*'}])
    newPart['name'].append('Battery_Management : BQ25601')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

