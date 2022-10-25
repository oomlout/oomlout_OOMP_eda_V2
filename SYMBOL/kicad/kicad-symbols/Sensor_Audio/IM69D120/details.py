
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Audio"
    oIndex = "IM69D120"
    hexID = "SZKSENAUDIOIM69D12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'MK', 'kicadSymbolValue': 'IM69D120', 'kicadSymbolFootprint': 'Sensor_Audio:Infineon_PG-LLGA-5-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IM69D120-DS-v01_00-EN.pdf?fileId=5546d462602a9dc801607a0e41a01a2b', 'kicadSymbolki_keywords': 'mems microphone', 'kicadSymbolki_description': 'High performance digital XENSIV MEMS microphone, -26 dBFS Sensitivity, LLGA-5', 'kicadSymbolki_fp_filters': 'Infineon*PG*LLGA*'}])
    newPart['name'].append('Sensor_Audio : IM69D120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

