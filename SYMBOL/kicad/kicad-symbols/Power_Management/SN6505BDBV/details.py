
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "SN6505BDBV"
    hexID = "SZKPOWERMANAGEMENTSN655BDBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SN6505ADBV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN6505BDBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn6505b.pdf', 'kicadSymbolki_keywords': 'Transformer Drivers', 'kicadSymbolki_description': 'Low Noise, 1A, Transformer Drivers for Isolated Power Supplies, 420 kHz, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Management : SN6505BDBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

