from math import ceil, sqrt

def leer_datos(ruta):
    datos = []
    with open(ruta, 'r') as f:
        i = 0
        for line in f.readlines():
            if i != 0:
                line = line.split(",")
                line[0], line[2], line[3], line[4] = int(line[0]), float(line[2]), int(line[3]), line[4][0]
                datos.append(line)
            i += 1
    return datos


def filtro_dep_x_num(datos, num_dep):
    datos_filtrados = []
    for d in datos:
        if d[0] == num_dep:
            datos_filtrados.append(d)
    return datos_filtrados


def promedio_terrenos(datos):
    return sum(datos) / len(datos)


def desviacion_estandar(datos):
    media = sum(datos) /  len(datos)
    return sqrt((sum(list(map(lambda x: (x - media) ** 2, datos)))) / (len(datos) - 1))


def main():
    archivo                 = leer_datos("data.csv")  
    depts                   = list(set(list(map(lambda x: int(x), input().split(' ')))))
    depts.sort()

    rango_antenas_previas   =  8400 
    
    for dep in depts:
        datos_departamentos = filtro_dep_x_num(archivo, dep)
        
        acumulador_antenas = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0
        }
        
        area_terreno, antenas_previas, tipo_ant_nueva = [d[2] for d in datos_departamentos], [d[3] for d in datos_departamentos], [d[4] for d in datos_departamentos]
        for i in range(len(area_terreno)):
            area, ant_previas, tipo_nueva = area_terreno[i], antenas_previas[i], tipo_ant_nueva[i]
            if tipo_nueva == 'a':
                acumulador_antenas[tipo_nueva] += max(0, ceil((area - (ant_previas * rango_antenas_previas))/33600))
            elif tipo_nueva == 'b':
                acumulador_antenas[tipo_nueva] += max(0, ceil((area - (ant_previas * rango_antenas_previas)) /48900))
            elif tipo_nueva == 'c':
                acumulador_antenas[tipo_nueva] += max(0, ceil((area - (ant_previas * rango_antenas_previas)) /17000)) 
            elif tipo_nueva == 'd' :
                acumulador_antenas[tipo_nueva] += max(0, ceil((area - (ant_previas * rango_antenas_previas)) /21000))
            elif tipo_nueva == 'e' :
                acumulador_antenas[tipo_nueva] += max(0, ceil((area - (ant_previas * rango_antenas_previas)) /42600))
        
        print(dep, datos_departamentos[0][1])
        print('terrain area')
        print('mean {:.2f}'.format(promedio_terrenos(area_terreno)))
        print('std {:.2f}'.format(desviacion_estandar(area_terreno)))
        print('min {:.2f}'.format(min(area_terreno)))
        print('max {:.2f}'.format(max(area_terreno)))
        print('total {:.2f}'.format(sum(area_terreno)))
        
        print('old antenna')
        print('mean {:.2f}'.format(promedio_terrenos(antenas_previas)))
        print('std {:.2f}'.format(desviacion_estandar(antenas_previas)))
        print('min {:.0f}'.format(min(antenas_previas)))
        print('max {:.0f}'.format(max(antenas_previas)))
        print('total {:.0f}'.format(sum(antenas_previas)))
        
        print('new antenna')
        print('a {:}'.format(acumulador_antenas['a']))
        print('b {:}'.format(acumulador_antenas['b']))
        print('c {:}'.format(acumulador_antenas['c']))
        print('d {:}'.format(acumulador_antenas['d']))
        print('e {:}'.format(acumulador_antenas['e']))


if __name__ == "__main__":
    main()