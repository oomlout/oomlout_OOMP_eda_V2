
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Relay_THT"
    oIndex = "Relay_DPST_Fujitsu_FTR-F1A"
    hexID = "FZKRELRELAYDPSTFUJITSUFTRF1A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Relay_DPST_Fujitsu_FTR-F1A', 'description': 'https://www.fujitsu.com/downloads/MICRO/fcai/relays/ftr-f1.pdf', 'tags': 'relay dpst fujitsu tht', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Relay_THT.3dshapes/Relay_DPST_Fujitsu_FTR-F1A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Relay_THT : Relay_DPST_Fujitsu_FTR-F1A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

