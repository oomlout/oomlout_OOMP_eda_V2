
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_DSC0010J_ThermalVias"
    hexID = "FZKSONTEXASDSC1JTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DSC0010J_ThermalVias', 'description': '3x3mm Body, 0.5mm Pitch, DSC0010J, WSON, http://www.ti.com/lit/ds/symlink/tps61201.pdf', 'tags': '0.5 DSC0010J WSON', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-DSC0010J.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Package_SON : Texas_DSC0010J_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

