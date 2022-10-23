
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Audio"
    oIndex = "MP45DT02"
    hexID = "SZKSENAUDIOMP45DT2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'MK', 'kicadSymbolValue': 'MP45DT02', 'kicadSymbolFootprint': 'Sensor_Audio:ST_HLGA-6_3.76x4.72mm_P1.65mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00025467.pdf', 'kicadSymbolki_keywords': 'MEMS Microphone', 'kicadSymbolki_description': 'MEMS Omnidirectional Digital Microphone, HLGA-6', 'kicadSymbolki_fp_filters': 'ST*HLGA*3.76x4.72mm*P1.65mm*'}])
    newPart['name'].append('MP45DT02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

