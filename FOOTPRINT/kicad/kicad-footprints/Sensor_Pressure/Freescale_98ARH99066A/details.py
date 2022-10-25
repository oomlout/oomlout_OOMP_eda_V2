
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Pressure"
    oIndex = "Freescale_98ARH99066A"
    hexID = "FZKSENPRESSUREFREESCALE98ARH9966A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Freescale_98ARH99066A', 'description': 'https://www.nxp.com/docs/en/data-sheet/MPXH6250A.pdf', 'tags': 'sensor pressure ssop 98ARH99066A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Pressure.3dshapes/Freescale_98ARH99066A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Pressure : Freescale_98ARH99066A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

