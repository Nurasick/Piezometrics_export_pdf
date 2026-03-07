#creating query functions to get need info
def get_drillhole_info(conn, drillhole_id):
    cursor = conn.cursor()
    query = "SELECT drillholeid, name,deposit_id,latitude,longitude " \
    "FROM drillholes " \
    "WHERE drillholeid = %s;"
    cursor.execute(query, (drillhole_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_node_measurements(conn,drillhole_id,from_ts, to_ts):
    cursor = conn.cursor()
    query = "SELECT timestamp, atm_pressure_mbar,atm_pressure_sea_level_mbar " \
    "FROM node_measurements " \
    "WHERE drillhole_id = %s " \
    "AND timestamp BETWEEN %s AND %s " \
    "ORDER BY timestamp;"

    cursor.execute(query,(drillhole_id, from_ts,to_ts))
    results = cursor.fetchall()
    cursor.close()
    return results

def get_channel_measurements(conn, drillhole_id,from_ts, to_ts):
    cursor = conn.cursor()
    query = "SELECT timestamp,channel_number,pressure,temperature_celsius " \
    "FROM channel_measurements " \
    "WHERE drillhole_id = %s " \
    "AND timestamp BETWEEN %s AND %s " \
    "ORDER BY timestamp;"

    cursor.execute(query,(drillhole_id,from_ts,to_ts))
    results = cursor.fetchall()
    cursor.close()
    return results
