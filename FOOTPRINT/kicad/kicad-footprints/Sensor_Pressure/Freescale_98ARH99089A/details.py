
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Pressure"
    oIndex = "Freescale_98ARH99089A"
    hexID = "FZKSENPRESSUREFREESCALE98ARH9989A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Freescale_98ARH99089A', 'description': 'https://www.nxp.com/docs/en/data-sheet/MPXH6250A.pdf', 'tags': 'sensor pressure ssop 98ARH99089A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Pressure.3dshapes/Freescale_98ARH99089A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Sensor_Pressure : Freescale_98ARH99089A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

