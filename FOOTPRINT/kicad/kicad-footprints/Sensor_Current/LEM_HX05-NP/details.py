
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "LEM_HX05-NP"
    hexID = "FZKSENCURRENTLEMHX5NP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEM_HX05-NP', 'description': 'LEM HX05-NP hall effect current transducer (https://www.lem.com/sites/default/files/products_datasheets/hx%205_15-np_e%20v10.pdf)', 'tags': 'hall current', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_HX05-NP.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Current : LEM_HX05-NP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

