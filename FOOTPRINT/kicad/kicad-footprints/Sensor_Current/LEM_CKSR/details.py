
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Current"
    oIndex = "LEM_CKSR"
    hexID = "FZKSENCURRENTLEMCKSR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LEM_CKSR', 'description': 'LEM CKSR 6/15/25/50/75-NP Current Transducer, https://www.lem.com/sites/default/files/products_datasheets/cksr_75-np.pdf', 'tags': 'current transducer LEM', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Current.3dshapes/LEM_CKSR.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Current : LEM_CKSR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

