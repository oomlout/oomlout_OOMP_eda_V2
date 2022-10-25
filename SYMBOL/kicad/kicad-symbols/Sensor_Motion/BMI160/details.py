
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "BMI160"
    hexID = "SZKSENMOTIONBMI16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BMI160', 'kicadSymbolFootprint': 'Package_LGA:Bosch_LGA-14_3x2.5mm_P0.5mm', 'kicadSymbolDatasheet': 'https://ae-bst.resource.bosch.com/media/_tech/media/datasheets/BST-BMI160-DS000.pdf', 'kicadSymbolki_keywords': 'Bosh IMU small low power inertial measurement unit', 'kicadSymbolki_description': 'Small, low power inertial measurement unit, LGA-14', 'kicadSymbolki_fp_filters': 'Bosch*LGA*3x2.5mm*P0.5mm*'}])
    newPart['name'].append('Sensor_Motion : BMI160')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

