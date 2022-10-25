
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "SMDIP-14_W11.48mm"
    hexID = "FZKDIPSMIP14W1148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMDIP-14_W11.48mm', 'description': '14-lead surface-mounted (SMD) DIP package, row spacing 11.48 mm (451 mils)', 'tags': 'SMD DIP DIL PDIP SMDIP 2.54mm 11.48mm 451mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/SMDIP-14_W11.48mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : SMDIP-14_W11.48mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

