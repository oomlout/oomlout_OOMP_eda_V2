
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_PTSM-0,5-6-HV-2.5-SMD_1x06-1MP_P2.50mm_Vertical"
    hexID = "FZKTBPHOENIXTBPHOENIXPTSM56HV25SM1X61MPP25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_PTSM-0,5-6-HV-2.5-SMD_1x06-1MP_P2.50mm_Vertical', 'description': 'PhoenixContact PTSM0,5 6 HV 2,5mm vertical SMD spring clamp terminal block connector http://www.phoenixcontact.com/us/products/1778735/pdf', 'tags': '2.5mm vertical SMD spring clamp terminal block connector ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PTSM-0,5-6-HV-2.5-SMD_1x06-1MP_P2.50mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_PTSM-0,5-6-HV-2.5-SMD_1x06-1MP_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

