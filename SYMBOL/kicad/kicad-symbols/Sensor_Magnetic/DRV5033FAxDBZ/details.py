
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "DRV5033FAxDBZ"
    hexID = "SZKSENMAGNETICDRV533FAXDBZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DRV5055A1xDBZxQ1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV5033FAxDBZ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/drv5033.pdf', 'kicadSymbolki_keywords': 'Digital Omnipolar Switch Hall Effect Sensor', 'kicadSymbolki_description': '±3.5 / ±2 mT, 20-kHz, 2-38V, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('DRV5033FAxDBZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

