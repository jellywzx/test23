import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis',
        'variable': [
            '100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind',
            '10m_u_component_of_wind', '10m_v_component_of_neutral_wind', '10m_v_component_of_wind',
            '10m_wind_speed', 'instantaneous_10m_wind_gust', 'significant_height_of_combined_wind_waves_and_swell',
            'significant_height_of_total_swell', 'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition',
            'significant_wave_height_of_second_swell_partition', 'significant_wave_height_of_third_swell_partition',
        ],
        'year': [
            '2020', '2021',
        ],
        'month': '01',
        'time': '00:00',
        'format': 'netcdf',
    },
    'download.nc')