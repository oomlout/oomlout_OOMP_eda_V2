
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Motion"
    oIndex = "InvenSense_QFN-24_3x3mm_P0.4mm_NoMask"
    hexID = "FZKSENMOTIONINVENSENSEQFN243X3P4NOMASK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'InvenSense_QFN-24_3x3mm_P0.4mm_NoMask', 'description': '24-Lead Plastic QFN (3mm x 3mm); Pitch 0.4mm; EP 1.7x1.54mm; for InvenSense motion sensors; Mask removed below exposed pad; keepout area marked (Package see: https://store.invensense.com/datasheets/invensense/MPU9250REV1.0.pdf; See also https://www.invensense.com/wp-content/uploads/2015/02/InvenSense-MEMS-Handling.pdf)', 'tags': 'QFN 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-24_3x3mm_P0.4mm_EP1.7x1.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Motion : InvenSense_QFN-24_3x3mm_P0.4mm_NoMask')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

