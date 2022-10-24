
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm"
    hexID = "FZKSOHTSS161EP44X5P65EP3X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm', 'description': 'HTSSOP, 16 Pin (https://www.st.com/resource/en/datasheet/stp08cp05.pdf#page=20), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HTSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

