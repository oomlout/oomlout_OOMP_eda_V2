
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Hirose_FH41-30S-0.5SH_1x30_1MP_1SH_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCHIROSEFH413S5SH1X31MP1SHP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_FH41-30S-0.5SH_1x30_1MP_1SH_P0.5mm_Horizontal', 'description': 'Hirose FH41, FFC/FPC connector, FH41-30S-0.5SH, 30 Pins per row (https://www.hirose.com/fr/product/document?clcode=CL0580-2218-5-05&productname=FH41-30S-0.5SH(05)&series=FH41&documenttype=2DDrawing&lang=fr&documentid=0001001704)', 'tags': 'connector Hirose FH41 horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Hirose_FH41-30S-0.5SH_1x30_1MP_1SH_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Hirose_FH41-30S-0.5SH_1x30_1MP_1SH_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

