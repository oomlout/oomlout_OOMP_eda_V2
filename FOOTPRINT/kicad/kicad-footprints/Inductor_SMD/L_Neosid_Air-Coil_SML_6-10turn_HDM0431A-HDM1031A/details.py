
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_Air-Coil_SML_6-10turn_HDM0431A-HDM1031A"
    hexID = "FZKINDUCTORSMLNEOSIDAIRCOILSML61TURNHDM431AHDM131A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_Air-Coil_SML_6-10turn_HDM0431A-HDM1031A', 'description': 'Neosid, Air-Coil, SML, 6-10turn, HDM0431A-HDM1031A,', 'tags': 'Neosid Air-Coil SML 6-10turn HDM0431A-HDM1031A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_Air-Coil_SML_6-10turn_HDM0431A-HDM1031A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_Air-Coil_SML_6-10turn_HDM0431A-HDM1031A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

