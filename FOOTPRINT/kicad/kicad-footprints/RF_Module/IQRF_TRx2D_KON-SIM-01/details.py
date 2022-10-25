
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "IQRF_TRx2D_KON-SIM-01"
    hexID = "FZKRFMOIQRFTRX2DKONSIM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'IQRF_TRx2D_KON-SIM-01', 'description': '8 pin SIM connector for IQRF TR-x2D(C)(T) modules, http://iqrf.org/weben/downloads.php?id=104', 'tags': 'IQRF_KON-SIM-01 IQRF_TRx2D IQRF_TRx2DC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/IQRF_TRx2D_KON-SIM-01.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Module : IQRF_TRx2D_KON-SIM-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

