
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_S-PWSON-N10_ThermalVias"
    hexID = "FZKSONTEXASSPWSONN1THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PWSON-N10_ThermalVias', 'description': '3x3mm Body, 0.5mm Pitch, S-PWSON-N10, DSC, http://www.ti.com/lit/ds/symlink/tps63060.pdf', 'tags': '0.5 S-PWSON-N10 DSC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PWSON-N10.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Texas_S-PWSON-N10_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

