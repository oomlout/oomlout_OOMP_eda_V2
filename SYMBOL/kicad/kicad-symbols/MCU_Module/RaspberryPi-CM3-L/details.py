
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "RaspberryPi-CM3-L"
    hexID = "SZKMCUMORASPBERRYPICM3L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RaspberryPi-CM3+L', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RaspberryPi-CM3-L', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.raspberrypi.org/documentation/hardware/computemodule/datasheets/rpi_DATA_CM_1p0.pdf', 'kicadSymbolki_keywords': 'raspberry pi compute module', 'kicadSymbolki_description': 'BCM2837 Broadcom 1.2 GHZ quad core, 1 GB RAM, industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('RaspberryPi-CM3-L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

