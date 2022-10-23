
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF13C_CL535-0402-2-51_1x02-1MP_P1.25mm_Vertical"
    hexID = "FZKCNHIROSEHIROSEDF13CCL535422511X21MPP125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF13C_CL535-0402-2-51_1x02-1MP_P1.25mm_Vertical', 'description': 'Hirose DF13C SMD, CL535-0402-2-51, 2 Pins per row (https://www.hirose.com/product/en/products/DF13/DF13C-10P-1.25V%2851%29/), generated with kicad-footprint-generator', 'tags': 'connector Hirose DF13C vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF13C_CL535-0402-2-51_1x02-1MP_P1.25mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF13C_CL535-0402-2-51_1x02-1MP_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

