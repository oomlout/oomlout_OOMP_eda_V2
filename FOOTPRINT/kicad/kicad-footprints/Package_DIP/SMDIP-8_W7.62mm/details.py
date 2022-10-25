
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "SMDIP-8_W7.62mm"
    hexID = "FZKDIPSMIP8W762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SMDIP-8_W7.62mm', 'description': '8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils)', 'tags': 'SMD DIP DIL PDIP SMDIP 2.54mm 7.62mm 300mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/SMDIP-8_W7.62mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : SMDIP-8_W7.62mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

