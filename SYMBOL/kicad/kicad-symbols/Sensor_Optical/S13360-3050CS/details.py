
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "S13360-3050CS"
    hexID = "SZKSENOPTICALS133635CS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'S13360-3025CS', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'S13360-3050CS', 'kicadSymbolFootprint': 'OptoDevice:Hamamatsu_S13360-30CS', 'kicadSymbolDatasheet': 'http://www.hamamatsu.com/resources/pdf/ssd/s13360_series_kapd1052e.pdf', 'kicadSymbolki_keywords': 'opto SiPM MPPC hamamatsu SPAD', 'kicadSymbolki_description': 'Multi-Pixel Photon Counter with 50µm pixel pitch', 'kicadSymbolki_fp_filters': 'Hamamatsu*S13360*30CS*'}])
    newPart['name'].append('S13360-3050CS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

