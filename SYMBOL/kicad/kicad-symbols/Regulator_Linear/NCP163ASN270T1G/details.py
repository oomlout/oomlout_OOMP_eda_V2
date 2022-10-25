
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP163ASN270T1G"
    hexID = "SZKREGULATORLINEARNCP163ASN27T1G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCP163ASN150T1G', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP163ASN270T1G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/ncp163-d.pdf', 'kicadSymbolki_keywords': 'LDO regulator voltage', 'kicadSymbolki_description': '250mA low-noise LDO, 2.2V-5.5V input, 2.7V output, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : NCP163ASN270T1G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

