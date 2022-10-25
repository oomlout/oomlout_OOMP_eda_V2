
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Mini-Circuits"
    oIndex = "Mini-Circuits_QQQ130_LandPattern_PL-236_ClockwisePinNumbering"
    hexID = "FZKRFMCIRCUITSQQQ13LANDPATTERNPL236CLWISEPINNUMBERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Mini-Circuits_QQQ130_LandPattern_PL-236_ClockwisePinNumbering', 'description': 'Footprint for Mini-Circuits case QQQ130 (https://ww2.minicircuits.com/case_style/QQQ130.pdf) following land pattern PL-236, including GND vias (https://ww2.minicircuits.com/pcb/98-pl236.pdf)', 'tags': 'Mini-Circuits PL-236', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_QQQ130.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('RF_Mini-Circuits : Mini-Circuits_QQQ130_LandPattern_PL-236_ClockwisePinNumbering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

