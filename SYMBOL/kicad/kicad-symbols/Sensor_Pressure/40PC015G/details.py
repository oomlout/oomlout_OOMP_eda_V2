
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "40PC015G"
    hexID = "SZKSENPRESSURE4PC15G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '40PC015G', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.honeywellscportal.com//index.php?ci_id=138832', 'kicadSymbolki_keywords': 'gage gauge pressure sensor', 'kicadSymbolki_description': 'Gauge pressure sensor, 0 to 15PSI, 5V supply, 0.2% accuracy, integrated signal conditioning, excellent media compatibility'}])
    newPart['name'].append('Sensor_Pressure : 40PC015G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

