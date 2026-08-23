import sys
sys.path.append("src")

from banco import buscar_partidas_time

partidas_via_sql = buscar_partidas_time("Palmeiras")
print(len(partidas_via_sql))