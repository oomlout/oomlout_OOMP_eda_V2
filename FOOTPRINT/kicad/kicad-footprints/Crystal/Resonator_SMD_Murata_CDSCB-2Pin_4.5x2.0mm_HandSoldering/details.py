
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm_HandSoldering"
    hexID = "FZKXRSCDSCB2PIN45X2HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm_HandSoldering', 'description': 'SMD Resomator/Filter Murata CDSCB, http://cdn-reichelt.de/documents/datenblatt/B400/SFECV-107.pdf, hand-soldering, 4.5x2.0mm^2 package', 'tags': 'SMD SMT ceramic resonator filter filter hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Resonator_SMD_Murata_CDSCB-2Pin_4.5x2.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

