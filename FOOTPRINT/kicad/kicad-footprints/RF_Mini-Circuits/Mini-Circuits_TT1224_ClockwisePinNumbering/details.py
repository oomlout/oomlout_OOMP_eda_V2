
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_TT1224_ClockwisePinNumbering"
    hexID = "FZKRFMCIRCUITSTT1224CLWISEPINNUMBERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_TT1224_ClockwisePinNumbering', 'description': 'Footprint for Mini-Circuits case TT1224 (https://ww2.minicircuits.com/case_style/TT1224.pdf) following land-pattern PL-258, including GND-vias (https://www.minicircuits.com/pcb/98-pl258.pdf)', 'tags': 'Mini-Circuits TT1224', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_TT1224.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_TT1224_ClockwisePinNumbering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

