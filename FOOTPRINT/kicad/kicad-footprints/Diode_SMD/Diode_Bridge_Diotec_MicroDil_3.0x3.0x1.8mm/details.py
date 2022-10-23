
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm"
    hexID = "FZKDIODESMDIODEBRIDGEDIOTECMDIL3X3X18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm', 'description': 'SMD package Diotec Diotec MicroDil, body 3.0x3.0x1.8mm (e.g. diode bridge), see https://diotec.com/tl_files/diotec/files/pdf/datasheets/mys40.pdf', 'tags': 'Diotec MicroDil diode bridge', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : Diode_Bridge_Diotec_MicroDil_3.0x3.0x1.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

