from db import get_db_connection
from queries import get_channel_measurements, get_drillhole_info, get_node_measurements
from plots import plot_channel_pressure, plot_channel_temperature, plot_atmospheric_pressure
from pdf_builder import create_pdf
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Generate PDF for drillholes')
    parser.add_argument('--drillholes', nargs='+', required=True, help='List of drillhole IDs')
    parser.add_argument('--from', dest='from_ts', required=True, help='Start timestamp (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--to', dest='to_ts', required=True, help='End timestamp (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--output',required=True, help='Output PDF file name')

    args = parser.parse_args()

    drillholes = args.drillholes
    from_ts = args.from_ts
    to_ts = args.to_ts
    output_file = args.output

    conn = get_db_connection()

    drillhole_sections = []

    for dh_id in drillholes:
        info_row = get_drillhole_info(conn, dh_id)
        if not info_row:
            print(f"Drillhole ID {dh_id} not found in the database.")
            continue
        drillhole_info = {
            'drillhole_id' : info_row[0],
            'name' : info_row[1],
            'deposit_id' : info_row[2],
            'latitude' : info_row[3],
            'longitude' : info_row[4]
        }

        pressure_img = plot_channel_pressure(conn, dh_id, from_ts, to_ts)
        temperature_img = plot_channel_temperature(conn, dh_id, from_ts, to_ts)
        atmospheric_img = plot_atmospheric_pressure(conn, dh_id, from_ts, to_ts)

        drillhole_sections.append({
            'drillhole_info' : drillhole_info,
            'pressure_img' : pressure_img,
            'temperature_img' : temperature_img,
            'atmospheric_img' : atmospheric_img
        })

    title_info = {
        'title' : 'Drillhole Measurements Report',
        'from' : from_ts,
        'to' : to_ts,
        'drillholes' : drillholes
    }


    create_pdf(title_info,drillhole_sections, output_file)
    print(f"PDF report generated: {output_file}")

    conn.close()

if __name__ =="__main__":
    main()


