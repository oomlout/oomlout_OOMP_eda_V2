
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Motion"
    oIndex = "InvenSense_QFN-24_4x4mm_P0.5mm"
    hexID = "FZKSENMOTIONINVENSENSEQFN244X4P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'InvenSense_QFN-24_4x4mm_P0.5mm', 'description': '24-Lead Plastic QFN (4mm x 4mm); Pitch 0.5mm; EP 2.7x2.6mm; for InvenSense motion sensors; keepout area marked (Package see: https://store.invensense.com/datasheets/invensense/MPU-6050_DataSheet_V3%204.pdf; See also https://www.invensense.com/wp-content/uploads/2015/02/InvenSense-MEMS-Handling.pdf)', 'tags': 'QFN 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Motion : InvenSense_QFN-24_4x4mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

