
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.2x5mm"
    hexID = "FZKSOHTSS241EP44X78P65EP32X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.2x5mm', 'description': 'HTSSOP, 24 Pin (https://www.st.com/resource/en/datasheet/stp16cp05.pdf#page=25), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'HTSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.2x5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.2x5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

