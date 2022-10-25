
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Tactile_SPST_Angled_PTS645Vx31-2LFS"
    hexID = "FZKBSWTACTILESPSTANGLPTS645VX312LFS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Tactile_SPST_Angled_PTS645Vx31-2LFS', 'description': 'tactile switch SPST right angle, PTS645VL31-2 LFS', 'tags': 'tactile switch SPST angled PTS645VL31-2 LFS C&K Button', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Tactile_SPST_Angled_PTS645Vx31-2LFS.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_Tactile_SPST_Angled_PTS645Vx31-2LFS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

