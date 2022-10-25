
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Harting"
    oIndex = "Harting_har-flexicon_14110713010xxx_1x07-MP_P2.54mm_Horizontal"
    hexID = "FZKCNHARTINGHARTINGHARFLEXICON14117131XXX1X7MPP254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Harting_har-flexicon_14110713010xxx_1x07-MP_P2.54mm_Horizontal', 'description': 'Harting har-flexicon series connector, 14110713010xxx (https://b2b.harting.com/files/download/PRD/PDF_TS/1411XX13010XXX_100228421DRW063C.pdf), generated with kicad-footprint-generator', 'tags': 'connector Harting har-flexicon horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Harting.3dshapes/Harting_har-flexicon_14110713010xxx_1x07-MP_P2.54mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Harting : Harting_har-flexicon_14110713010xxx_1x07-MP_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

