
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp"
    hexID = "FZKDDDO34SOD68P254VERTICALANODEUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp', 'description': 'Diode, DO-34_SOD68 series, Axial, Vertical, pin pitch=2.54mm, , length*diameter=3.04*1.6mm^2, , https://www.nxp.com/docs/en/data-sheet/KTY83_SER.pdf', 'tags': 'Diode DO-34_SOD68 series Axial Vertical pin pitch 2.54mm  length 3.04mm diameter 1.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : D_DO-34_SOD68_P2.54mm_Vertical_AnodeUp')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

