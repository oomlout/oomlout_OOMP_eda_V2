
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_AnalogDevices"
    oIndex = "ADAU1702"
    hexID = "SZKDSPANALOGDEVICESADAU172"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADAU1701', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADAU1702', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADAU1702.pdf', 'kicadSymbolki_keywords': 'sigmadsp audio adc dac', 'kicadSymbolki_description': 'SigmaDSP 28-/56-Bit Audio Processor with Two ADCs and Four DACs, 25 MIPS, 512kword Program RAM, 512kword Data RAM, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('ADAU1702')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

