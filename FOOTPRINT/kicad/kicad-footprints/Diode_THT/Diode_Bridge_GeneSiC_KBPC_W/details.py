
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_GeneSiC_KBPC_W"
    hexID = "FZKDDIODEBRIDGEGENESICKBPCW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_GeneSiC_KBPC_W', 'description': 'Single phase, Bridge Rectifier, 28.55x28.55mm, case KBPC_W(WP), https://www.diodemodule.com/bridge-rectifier/kbpc/kbpc15005w.pdf', 'tags': 'diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_GeneSiC_KBPC_W.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_GeneSiC_KBPC_W')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

