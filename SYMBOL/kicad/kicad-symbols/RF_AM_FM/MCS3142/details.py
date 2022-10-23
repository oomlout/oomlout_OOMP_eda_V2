
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "MCS3142"
    hexID = "SZKRFAMFMMCS3142"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCS3142', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/40001747A.pdf', 'kicadSymbolki_keywords': 'KEELOQ classic ultimate keyless entry keyfob ISM', 'kicadSymbolki_description': 'Microchip KEELOQ classic / ultimate encoder - keyfob IC sending button state, serial and authentiation as PWM/manchester encoded AM/FM signal in ISM bands', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm?P0.65mm*'}])
    newPart['name'].append('MCS3142')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

