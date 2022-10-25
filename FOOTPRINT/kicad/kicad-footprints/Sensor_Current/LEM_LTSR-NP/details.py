
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "LEM_LTSR-NP"
    hexID = "FZKSENCURRENTLEMLTSRNP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEM_LTSR-NP', 'description': 'LEM current transducer LEM_LTSR-NP 5V supply voltage series https://www.lem.com/sites/default/files/products_datasheets/ltsr_6-np.pdf', 'tags': 'Current transducer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_LTSR-NP.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Current : LEM_LTSR-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

