
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "Diode_Bridge_Diotec_ABS"
    hexID = "FZKDIODESMDIODEBRIDGEDIOTECABS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_Diotec_ABS', 'description': 'SMD diode bridge ABS (Diotec), see https://diotec.com/tl_files/diotec/files/pdf/datasheets/abs2.pdf', 'tags': 'ABS MBLS', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Diotec_ABS.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : Diode_Bridge_Diotec_ABS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

