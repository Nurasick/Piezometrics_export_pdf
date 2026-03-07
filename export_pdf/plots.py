from queries import get_channel_measurements, get_drillhole_info, get_node_measurements
import matplotlib.pyplot as plt
from io import BytesIO






# Plot the pressure and temerature data for each channel

def plot_channel_pressure(conn, drillhole_id, from_ts, to_ts):
    channel_data = get_channel_measurements(conn, drillhole_id, from_ts, to_ts)


    '''group data by channel'''
    channels = {}
    for ts,ch,pressure,temp in channel_data:
        if ch not in channels:
            channels[ch] = {'timestamps':[],'pressures':[],'temperatures':[]}
        channels[ch]['timestamps'].append(ts)
        channels[ch]['pressures'].append(pressure)
        channels[ch]['temperatures'].append(temp)

    channel_plots = {}

    for ch, data in channels.items():

        plt.figure(figsize=(14, 5))

        plt.plot(data['timestamps'], data['pressures'], label=f'Channel {ch} Pressure')

        plt.xlabel('Time')
        plt.ylabel('Pressure')
        plt.title(f'Pressure - Channel {ch} for Drillhole {drillhole_id}')
        plt.grid(True)
        plt.tight_layout()
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plt.close()
        channel_plots[ch] = buffer
    
    return channel_plots

def plot_channel_temperature(conn, drillhole_id,from_ts,to_ts):
    channel_data = get_channel_measurements(conn, drillhole_id, from_ts, to_ts)


    '''group data by channel'''
    channels = {}
    for ts,ch,pressure,temp in channel_data:
        if ch not in channels:
            channels[ch] = {'timestamps':[],'pressures':[],'temperatures':[]}
        channels[ch]['timestamps'].append(ts)
        channels[ch]['pressures'].append(pressure)
        channels[ch]['temperatures'].append(temp)


    channel_plots ={}
    

    for ch, data in channels.items():
        plt.figure(figsize=(14, 5))
        plt.plot(data['timestamps'], data['temperatures'], label=f'Channel {ch} Temperature')
        
        plt.xlabel('Time')
        plt.ylabel('Temperature')
        plt.title(f'Temperature - Channel {ch} for Drillhole {drillhole_id}')
        plt.grid(True)
        plt.tight_layout()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plt.close()
        channel_plots[ch] = buffer
    
    return channel_plots

def plot_atmospheric_pressure(conn, drillhole_id, from_ts, to_ts):
    node_data = get_node_measurements(conn,drillhole_id, from_ts, to_ts)
    if not node_data:
        plt.text(0.5, 0.5, "No data", ha='center', va='center')
        
        



    timestamps = []
    atm = []
    atm_sea = []

    for ts,p1,p2 in node_data:
        timestamps.append(ts)
        atm.append(p1)
        atm_sea.append(p2)

    plots = {}

    plt.figure(figsize=(14, 5))
    plt.plot(timestamps, atm, label='Atmospheric Pressure (mbar)')


    plt.xlabel('Time')
    plt.ylabel('Pressure (mbar)')
    plt.title(f'Atmospheric Pressure Measurements for Drillhole {drillhole_id}') 
    plt.grid(True)
    plt.tight_layout()

    '''Save png into buffer to later insert into pdf'''
    buffer = BytesIO()
    plt.savefig(buffer, format='png',dpi=300)
    buffer.seek(0)

    plt.close()

    plots['atm'] = buffer


    sea_level_exists = any(v is not None for v in atm_sea)

    plt.figure(figsize=(14,5))

    if sea_level_exists:
        plt.plot(timestamps, atm_sea)
    else:
        plt.text(
            0.5,
            0.5,
            "No Sea Level Data Available",
            ha="center",
            va="center",
            transform=plt.gca().transAxes
        )

    plt.xlabel("Time")
    plt.ylabel("Pressure (mbar)")
    plt.title("Atmospheric Pressure at Sea Level")
    plt.grid(True)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format="png", dpi=300)
    buffer.seek(0)
    plt.close()

    plots["atm_sea"] = buffer

    return plots