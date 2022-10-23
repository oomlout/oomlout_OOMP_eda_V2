
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Hirose_FH12-40S-0.5SH_1x40-1MP_P0.50mm_Horizontal"
    hexID = "FZKCNFFCFPCHIROSEFH124S5SH1X41MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_FH12-40S-0.5SH_1x40-1MP_P0.50mm_Horizontal', 'description': 'Hirose FH12, FFC/FPC connector, FH12-40S-0.5SH, 40 Pins per row (https://www.hirose.com/product/en/products/FH12/FH12-24S-0.5SH(55)/), generated with kicad-footprint-generator', 'tags': 'connector Hirose FH12 horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Hirose_FH12-40S-0.5SH_1x40-1MP_P0.50mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Hirose_FH12-40S-0.5SH_1x40-1MP_P0.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

