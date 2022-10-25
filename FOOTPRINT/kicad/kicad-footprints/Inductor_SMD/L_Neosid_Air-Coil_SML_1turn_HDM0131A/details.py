
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_Air-Coil_SML_1turn_HDM0131A"
    hexID = "FZKINDUCTORSMLNEOSIDAIRCOILSML1TURNHDM131A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_Air-Coil_SML_1turn_HDM0131A', 'description': 'Neosid, Air-Coil, SML, 1turn, HDM0131A,', 'tags': 'Neosid Air-Coil SML 1turn HDM0131A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_Air-Coil_SML_1turn_HDM0131A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_Air-Coil_SML_1turn_HDM0131A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

