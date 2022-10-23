
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Hirose"
    oIndex = "Hirose_DF52-4S-0.8H_1x04-1MP_P0.80mm_Horizontal"
    hexID = "FZKCNHIROSEHIROSEDF524S8H1X41MPP8HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Hirose_DF52-4S-0.8H_1x04-1MP_P0.80mm_Horizontal', 'description': 'Hirose  series connector, DF52-4S-0.8H (https://www.hirose.com/product/en/products/DF52/DF52-3S-0.8H%2821%29/), generated with kicad-footprint-generator', 'tags': 'connector Hirose  top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Hirose.3dshapes/Hirose_DF52-4S-0.8H_1x04-1MP_P0.80mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Hirose : Hirose_DF52-4S-0.8H_1x04-1MP_P0.80mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

