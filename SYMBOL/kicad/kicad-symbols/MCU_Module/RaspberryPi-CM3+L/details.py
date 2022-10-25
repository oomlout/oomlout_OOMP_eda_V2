
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "RaspberryPi-CM3+L"
    hexID = "SZKMCUMORASPBERRYPICM3+L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RaspberryPi-CM3+L', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.raspberrypi.org/documentation/hardware/computemodule/datasheets/rpi_DATA_CM3plus_1p0.pdf', 'kicadSymbolki_keywords': 'raspberry pi compute module', 'kicadSymbolki_description': 'BCM2837B0 Broadcom 1.2 GHZ quad core, 1 GB RAM, industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('MCU_Module : RaspberryPi-CM3+L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

