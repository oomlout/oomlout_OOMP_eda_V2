
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_VSON-HR-8_1.5x2mm_P0.5mm"
    hexID = "FZKDFNTEXASVSONHR815X2P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_VSON-HR-8_1.5x2mm_P0.5mm', 'description': 'Texas  VSON-HR, 8 Pin (http://www.ti.com/lit/ds/symlink/tps62823.pdf#page=29), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Texas VSON-HR NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_VSON-HR-8_1.5x2mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_VSON-HR-8_1.5x2mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

