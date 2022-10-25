
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_Phoenix"
    oIndex = "TerminalBlock_Phoenix_PTSM-0,5-8-2,5-V-SMD_1x08-1MP_P2.50mm_Vertical"
    hexID = "FZKTBPHOENIXTBPHOENIXPTSM5825VSM1X81MPP25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_Phoenix_PTSM-0,5-8-2,5-V-SMD_1x08-1MP_P2.50mm_Vertical', 'description': 'PhoenixContact PTSM0,5 8 2,5mm vertical SMD spring clamp terminal block connector http://www.phoenixcontact.com/us/products/1814760/pdf', 'tags': 'PhoenixContact PTSM0.5 8 2.5mm vertical SMD spring clamp terminal block connector ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PTSM-0,5-8-2,5-V-SMD_1x08-1MP_P2.50mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_Phoenix : TerminalBlock_Phoenix_PTSM-0,5-8-2,5-V-SMD_1x08-1MP_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

