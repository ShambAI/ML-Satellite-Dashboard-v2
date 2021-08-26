# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import numpy as np
import geojson
import folium
from django import template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from branca.element import MacroElement
from jinja2 import Template
from shapely.geometry import shape
from shapely import geometry

# generic base view
from django.views.generic import TemplateView

# folium
from folium import plugins
import pandas as pd
from folium.plugins import MarkerCluster
import ee

service_account = 'cajulab@benin-cajulab-web-application.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'privatekey.json')
ee.Initialize(credentials)


# def mmy_home():
#     m = folium.Map(location=[9.0, 2.4], zoom_start=7,)
#     plugins.Fullscreen(position='topright', title='Full Screen',
#                        title_cancel='Exit Full Screen', force_separate_button=False).add_to(m)

#     dtstats_df1 = pd.DataFrame()
#     for dist1 in dist_stats1['features']:
#         df1 = pd.DataFrame([dist1['properties']],
#                            columns=dist1['properties'].keys())
#         dtstats_df1 = pd.concat([dtstats_df1, df1], axis=0)

#     # Reorder columns in dataframe, sort by state name and reset index
#     dtstats_df1 = dtstats_df1[['Country', 'Districts', 'Cashew_Yield']]
#     dtstats_df1 = dtstats_df1.sort_values(
#         by=['Districts']).reset_index(drop=True)

#     # change state names from upper case to title case!!
#     dtstats_df1['Districts'] = dtstats_df1['Districts'].str.title()

#     dist_stats = alldept.eq(1).multiply(ee.Image.pixelArea()).reduceRegions(
#         collection=benin_adm2,
#         reducer=ee.Reducer.sum(),
#         scale=30,
#     )
#     dist_stats = dist_stats.select(['NAME_0', 'NAME_1', 'NAME_2', 'sum'], [
#                                    'Country', 'Districts', 'Communes', 'Cashew_Yield'], retainGeometry=True).getInfo()

#     dtstats_df = pd.DataFrame()
#     for dist in dist_stats['features']:
#         df = pd.DataFrame([dist['properties']],
#                           columns=dist['properties'].keys())
#         dtstats_df = pd.concat([dtstats_df, df], axis=0)

#     # Reorder columns in dataframe, sort by state name and reset index
#     dtstats_df = dtstats_df[['Country',
#                              'Districts', 'Communes', 'Cashew_Yield']]
#     dtstats_df = dtstats_df.sort_values(
#         by=['Districts']).reset_index(drop=True)

#     # change state names from upper case to title case!!
#     dtstats_df['Districts'] = dtstats_df['Districts'].str.title()

#     m = folium.Map(
#         location=[9.0, 2.4],
#         zoom_start=7,
#     )
#     m.add_to(figure)

#     plugins.Fullscreen(position='topright', title='Full Screen',
#                        title_cancel='Exit Full Screen', force_separate_button=False).add_to(m)

#     marker_cluster = MarkerCluster(
#         name="Benin-Nursery Information").add_to(m)

#     for i in range(len(ben_nursery)):
#         folium.Marker(
#             location=[ben_nursery[i:i+1]['Latitude'].values[0], ben_nursery[i:i+1]['Longitude'].values[0]],
#             rise_on_hover=True,
#             rise_offset=250,
#             icon=folium.Icon(color="red", icon="leaf"),
#             popup=
#             '''
#                 <h4 style="font-family: 'Trebuchet MS', sans-serif">Commune Name: <b>{}</b></h4>
#                 <h5 style="font-family: 'Trebuchet MS', sans-serif">Nursery Owner: <i>{}</i></h5>
#                 <h5 style="font-family: 'Trebuchet MS', sans-serif">Nursery Area (ha): <b>{}</b></h5>
#                 <h5 style="font-family: 'Trebuchet MS', sans-serif">Number of Plants: <b>{}</b></h5>
#                 <a href="https://www.technoserve.org/our-work/agriculture/cashew/?_ga=2.159985149.1109250972.1626437600-1387218312.1616379774"target="_blank">click link to website</a>
#                 <img src="https://gumlet.assettype.com/deshdoot/import/2019/12/tripXOXO-e1558439144643.jpg?w=1200&h=750&auto=format%2Ccompress&fit=max" width="200" height="70">
#             '''
#             .format(ben_nursery[i:i+1].Commune.values[0], ben_nursery[i:i+1].Owner.values[0], ben_nursery[i:i+1]['Area (ha)'].values[0], ben_nursery[i:i+1]['Numebr of Plants'].values[0])).add_to(marker_cluster)

#     def add_ee_layer(self, ee_image_object, vis_params, name):
#         map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
#         folium.raster_layers.TileLayer(
#             tiles=map_id_dict['tile_fetcher'].url_format,
#             attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
#             name=name,
#             overlay=True,
#             control=True
#         ).add_to(self)

#     folium.Map.add_ee_layer = add_ee_layer
#     m.add_ee_layer(alldept, {
#                         'min': 0, 'max': 4, 'palette': "black, green, white, gray"}, 'Benin-Caju Prediction')

#     # json_layer_ben = folium.GeoJson(data=benin_adm1_json, name='Benin States JSON')

#     def highlight_function(feature):
#         return {"fillColor": "#ffaf00", "color": "green", "weight": 3, "dashArray": "1, 1"}

class my_home():
    # Define a method for displaying Earth Engine image tiles on a folium map.

    def __init__(self):
        self.figure = folium.Figure()
        self.m = ""
        self.value2 = ""
        self.name = ""

    def get_context_data(self, **kwargs):

                # figure = folium.Figure()
        benin_adm0 = ee.FeatureCollection("users/ashamba/BEN_adm0")
        benin_adm1 = ee.FeatureCollection("users/ashamba/BEN_adm1")
        benin_adm2 = ee.FeatureCollection("users/ashamba/BEN_adm2")

        alldept = ee.Image('users/ashamba/allDepartments_v0')
        RGB = ee.Image('users/ashamba/RGB')

        ben_yield = pd.read_excel("./Data/Yield data_YEARS_master.xlsx", skiprows=1,engine='openpyxl',)
        ben_yield = ben_yield.interpolate()
        ben_yield['Departement'] = ben_yield['Departement'].str.title()
        ben_yield['Commune'] = ben_yield['Commune'].str.title()
        ben_yield['Arrondissement'] = ben_yield['Arrondissement'].str.title()
        ben_yield['Village'] = ben_yield['Village'].str.title()
        ben_yield['Surname'] = ben_yield['Surname'].str.title()
        ben_yield['Given Name'] = ben_yield['Given Name'].str.title()
        ben_yield.loc[(ben_yield.Commune == 'Bante'), 'Commune'] = 'Bantè'
        ben_yield.loc[(ben_yield.Commune == 'Dassa'), 'Commune'] = 'Dassa-Zoumè'
        ben_yield.loc[(ben_yield.Commune == 'Save'), 'Commune'] = 'Savè'
        ben_yield.loc[(ben_yield.Commune == 'Glazoue'), 'Commune'] = 'Glazoué'
        ben_yield.loc[(ben_yield.Commune == 'Ndali'), 'Commune'] = "N'Dali"
        ben_yield.loc[(ben_yield.Commune == 'Ouesse'), 'Commune'] = 'Ouèssè'

        ben_nursery = pd.read_excel("./Data/Nurseries.xlsx",engine='openpyxl',)

        ben_nursery['Commune'] = ben_nursery['Commune'].str.title()
        ben_nursery['Owner'] = ben_nursery['Owner'].str.title()

        #Drop nan columns
        ben_nursery.drop(["Date","Provenance","Regarnissage", "Altitude", "Partenaire"], axis = 1, inplace = True)
        ben_nursery.dropna(inplace=True)

        with open("ben_adm0.json", errors="ignore") as f:
            benin_adm0_json = geojson.load(f)

        with open("ben_adm1.json") as f:
            benin_adm1_json = geojson.load(f)

        with open("ben_adm2.json") as f:
            benin_adm2_json = geojson.load(f)

        dist_stats1 = alldept.eq(1).reduceRegions(
                                        collection = benin_adm1,
                                        reducer = ee.Reducer.sum(),
                                        scale = 30
                                        )
        dist_stats1 = dist_stats1.select(['NAME_0','NAME_1', 'sum'], ['Country', 'Districts','Cashew_Yield'], retainGeometry=True).getInfo()

        dtstats_df1 = pd.DataFrame()
        for dist1 in dist_stats1['features']:
            df1 = pd.DataFrame([dist1['properties']], columns=dist1['properties'].keys())
            dtstats_df1 = pd.concat([dtstats_df1, df1], axis=0)

        # Reorder columns in dataframe, sort by state name and reset index
        dtstats_df1 = dtstats_df1[['Country', 'Districts', 'Cashew_Yield']]
        dtstats_df1 = dtstats_df1.sort_values(by=['Districts']).reset_index(drop=True)

        # change state names from upper case to title case!!
        dtstats_df1['Districts'] = dtstats_df1['Districts'].str.title()

        dist_stats = alldept.eq(1).multiply(ee.Image.pixelArea()).reduceRegions(
                                            collection = benin_adm2,
                                            reducer = ee.Reducer.sum(),
                                            scale = 30,
                                            )
        dist_stats = dist_stats.select(['NAME_0','NAME_1', 'NAME_2', 'sum'], ['Country', 'Districts', 'Communes','Cashew_Yield'], retainGeometry=True).getInfo()

        dtstats_df = pd.DataFrame()
        for dist in dist_stats['features']:
            df = pd.DataFrame([dist['properties']], columns=dist['properties'].keys())
            dtstats_df = pd.concat([dtstats_df, df], axis=0)

        # Reorder columns in dataframe, sort by state name and reset index
        dtstats_df = dtstats_df[['Country', 'Districts', 'Communes', 'Cashew_Yield']]
        dtstats_df = dtstats_df.sort_values(by=['Districts']).reset_index(drop=True)

        # change state names from upper case to title case!!
        dtstats_df['Districts'] = dtstats_df['Districts'].str.title()


        basemaps = {
                    'Google Maps': folium.TileLayer(
                        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                        attr = 'Google',
                        name = 'Maps',
                        max_zoom =20,
                        overlay = True,
                        control = False
                    ),
                    'Google Satellite': folium.TileLayer(
                        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                        attr = 'Google',
                        name = 'Satellite',
                        max_zoom = 20,
                        overlay = True,
                        show=False,
                        control = True
                    ),
                    'Google Terrain': folium.TileLayer(
                        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                        attr = 'Google',
                        name = 'Google Terrain',
                        overlay = True,
                        control = True
                    ),
                    'Google Satellite Hybrid': folium.TileLayer(
                        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                        attr = 'Google',
                        name = 'Google Satellite',
                        overlay = True,
                        control = True
                    ),
                    'Esri Satellite': folium.TileLayer(
                        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                        attr = 'Esri',
                        name = 'Esri Satellite',
                        overlay = True,
                        control = True
                    )
                }




        m = folium.Map(
            location=[9.0, 2.4],
            zoom_start=8,
            tiles = None
        )

        m.add_child(basemaps['Google Maps'])
        m.add_child(basemaps['Google Satellite'])

        plugins.Fullscreen(position='topright', title='Full Screen', title_cancel='Exit Full Screen', force_separate_button=False).add_to(m)

        def highlight_function(feature):
            return {"fillColor": "#ffaf00", "color": "green", "weight": 3, "dashArray": "1, 1"}

        plantation_cluster = MarkerCluster(name="Benin Plantations").add_to(m)

        for i in range(1,13):
            with open(f"geojson_data/{i}.geojson") as f:
                plantation_json = geojson.load(f)

            plant_geojson  = folium.GeoJson(data=plantation_json,
                                            name='Benin-Adm0 Department',
                                            zoom_on_click = True)
        #                                     highlight_function = highlight_function)
            plant_geojson.add_to(plantation_cluster)

            features = plantation_json["features"][0]
            s = shape(features["geometry"])
            centre = s.centroid
            folium.Marker(location= [centre.y, centre.x],
                        rise_on_hover=True,
                        rise_offset = 250,
                        icon = folium.Icon(color="lightblue", icon="info-sign"),
                        popup='''
                        <div style="border: 3px solid #808080">
                        <img src="https://i0.wp.com/cdn.vanguardngr.com/wp-content/uploads/2015/07/Cashew-fruit.jpg?resize=350%2C200&ssl=1" width="150" height="100">
                        <h5>Plantation Owner: <b>Boniface</b></h5>
                        <h5>Plantation Area (ha): <b>Unknown</b></h5>
                        <h5>Number of Trees: <b>Unknown</b></h5>
                        <a href="https://www.technoserve.org/our-work/agriculture/cashew/?_ga=2.159985149.1109250972.1626437600-1387218312.1616379774"target="_blank">click link to website</a>
                        </div>''').add_to(plantation_cluster)

        marker_cluster = MarkerCluster(name="Nursery Information").add_to(m)

        for i in range(len(ben_nursery)):
            folium.Marker(location= [ben_nursery[i:i+1]['Latitude'].values[0], ben_nursery[i:i+1]['Longitude'].values[0]],
                        rise_on_hover=True,
                        rise_offset = 250,
                        icon = folium.Icon(color="red", icon="leaf"),
                        popup='''
                        <div style="border: 3px solid #808080">
                        <h4 style="font-family: 'Trebuchet MS', sans-serif">Commune Name: <b>{}</b></h4>
                        <h5 style="font-family: 'Trebuchet MS', sans-serif">Nursery Owner: <i>{}</i></h5>
                        <h5 style="font-family: 'Trebuchet MS', sans-serif">Nursery Area (ha): <b>{}</b></h5>
                        <h5 style="font-family: 'Trebuchet MS', sans-serif">Number of Plants: <b>{}</b></h5>
                        <a href="https://www.technoserve.org/our-work/agriculture/cashew/?_ga=2.159985149.1109250972.1626437600-1387218312.1616379774"target="_blank">click link to website</a>
                        <img src="https://gumlet.assettype.com/deshdoot/import/2019/12/tripXOXO-e1558439144643.jpg?w=1200&h=750&auto=format%2Ccompress&fit=max" width="200" height="70">
                        </div>'''.format(ben_nursery[i:i+1].Commune.values[0], ben_nursery[i:i+1].Owner.values[0], ben_nursery[i:i+1]['Area (ha)'].values[0], ben_nursery[i:i+1]['Numebr of Plants'].values[0])).add_to(marker_cluster)

            
        drone1 = 'drone1/drone1.png'
        drone2 = 'drone2/drone2.png'

        feature_group = folium.map.FeatureGroup(name='Drone Images')
        if not os.path.isfile(drone1):
            print(f"Could not find {drone1}")
        else:
            img = folium.raster_layers.ImageOverlay(
                name="SW1",
                image=drone1,
                bounds=[[9.45941126, 2.63917854], [9.45440760, 2.64878300]],
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
            )

            folium.Popup("I am an image 1").add_to(img)
            feature_group.add_child(img)
            
        if not os.path.isfile(drone2):
            print(f"Could not find {drone2}")
        else:
            img2 = folium.raster_layers.ImageOverlay(
                name="SW2",
                image=drone2,
                bounds=[[9.89726770, 3.16071852], [9.89477856, 3.16551109]],
                opacity=1.0,
                interactive=True,
                cross_origin=False,
                zindex=1,
            )

            folium.Popup("I am an image 2").add_to(img2)
            feature_group.add_child(img2)
            feature_group.add_to(m)
            
        feature_group2 = folium.map.FeatureGroup(name='Tree Tops')    
        for i in range(1,3):
            with open(f"drone{i}/Tree Crowns.geojson") as f:
                crown_json = geojson.load(f)
            crown_geojson  = folium.GeoJson(data=crown_json,
                                            name='Tree Tops',
                                            zoom_on_click = True)
            feature_group2.add_child(crown_geojson)
        feature_group2.add_to(m)
            

        def add_ee_layer(self, ee_image_object, vis_params, name):
            map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
            folium.raster_layers.TileLayer(
                tiles=map_id_dict['tile_fetcher'].url_format,
                attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
                name=name,
                overlay=True,
                control=True
            ).add_to(self)

        folium.Map.add_ee_layer = add_ee_layer   

        zones = alldept.eq(1)
        zones = zones.updateMask(zones.neq(0));

        m.add_ee_layer(zones, {'palette': "red"}, 'Satellite Prediction')



        layer3 = folium.FeatureGroup(name='No Boundary', show=False, overlay = False)
        layer3.add_to(m)

        layer0 = folium.FeatureGroup(name='Benin Republic', show=False, overlay = False)


        temp_geojson0  = folium.GeoJson(data=benin_adm0_json,
            name='Benin-Adm0 Department',
            highlight_function = highlight_function)


        for feature in temp_geojson0.data['features']:
            # GEOJSON layer consisting of a single feature

            y0 = dtstats_df1[dtstats_df1['Country']=='Benin']['Districts']
            # getting values against each value of y

            pred_ben_data = []
            pred_ground_ben_data = [['Departments', 'Satellite Prediction', 'Ground Data Estimate']]
            for y in y0:
                x_new = round(sum(ben_yield[ben_yield['Departement']==y]['2020 estimated surface (ha)'].dropna()),2)
                x = round(sum(dtstats_df[dtstats_df['Districts']==y].Cashew_Yield)/10000,2)
                pred_ben_data.append([y, x])
                pred_ground_ben_data.append([y, x, x_new*100])

            temp_layer0 = folium.GeoJson(feature,  zoom_on_click = True, highlight_function = highlight_function)

            name = 'Benin Republic'
            surface_area = round(sum(ben_yield['2020 estimated surface (ha)'].dropna())*100,2)
            total_yield = round(sum(ben_yield['2020 total yield (kg)'].dropna()),2)
            yield_ha = round(sum(ben_yield['2020 yield per ha (kg)'].dropna()),2)
            yield_tree = round(sum(ben_yield['2020 yield per tree (kg)'].dropna()),2)
            num_tree = int(sum(ben_yield['Number of trees'].dropna()))
            sick_tree = int(sum(ben_yield['Number of sick trees'].dropna()))
            out_prod_tree = int(sum(ben_yield['Number of trees out of production'].dropna()))
            dead_tree = int(sum(ben_yield['Number of dead trees'].dropna()))
            tree_ha_pred = round(sum(dtstats_df[dtstats_df['Country']=='Benin'].Cashew_Yield)/10000,2)

            html4 = '''
                    <html>
                        <head>
                            <style>
                            table {{
                            border-collapse: collapse;
                            width: 100%;
                            }}


                            table th {{
                            background-color: #004b55;
                            text-align: left;
                            color: #FFF;
                            padding: 4px 30px 4px 8px;
                            }}


                            table td {{
                            border: 1px solid #e3e3e3;
                            padding: 4px 8px;
                            }}


                            table tr:nth-child(odd) td{{
                            background-color: #e7edf0;
                            }}
                            </style>
                            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
                            <script type="text/javascript">
                            // Load Charts and the corechart and barchart packages.
                            google.charts.load('current', {{'packages':['corechart']}});
                            google.charts.load('current', {{'packages':['bar']}});

                            // Draw the pie chart and bar chart when Charts is loaded.
                            google.charts.setOnLoadCallback(drawChart);

                            function drawChart() {{

                                var pie_data = new google.visualization.DataTable();
                                pie_data.addColumn('string', 'Commune');
                                pie_data.addColumn('number', 'Cashew Tree Cover (ha)');
                                pie_data.addRows({1});

                                var piechart_options = {{title:'Pie Chart: Departments Cashew Tree Cover Statistics In {0}',
                                                            is3D: true,
                                                        }};
                                var piechart = new google.visualization.PieChart(document.getElementById('piechart_div'));
                                piechart.draw(pie_data, piechart_options);

                                var data = new google.visualization.arrayToDataTable({2});

                                var options = {{
                                    chart: {{
                                        title: 'Cashew Tree Cover Relative Statistics in {0}',
                                    }},
                                    bars: 'horizontal', // Required for Material Bar Charts.
                                    colors: ['#02a8b1', '#242526'],
                                    is3D: true,

                                    axes: {{
                                            x: {{
                                            0: {{label: 'Cashew Tree Cover (ha)'}}, // Bottom x-axis.
                                            }}
                                        }}
                                        }};

                                var chart = new google.charts.Bar(document.getElementById('dual_x_div'));
                                chart.draw(data, options);


                                var data_donut = google.visualization.arrayToDataTable([
                                ['Tree Type', 'Number of Trees'],
                                ['Active Trees',      {14}],
                                ['Sick Trees',      {11}],
                                ['Dead Trees',     {13}],
                                ['Out of Production Trees',      {12}],
                                ]);

                                var options_donut = {{
                                title: 'Cashew Trees Status in {0}',
                                pieHole: 0.5,
                                colors: ['007f00', '#02a8b1', '9e1a1a', '#242526'],
                                }};

                                var chart_donut = new google.visualization.PieChart(document.getElementById('donutchart'));
                                chart_donut.draw(data_donut, options_donut);

                                }};
                            </script>
                        </head>
                        <body>
                            <h2>{0}</h2>
                            <h4>{0} is ranked <b>{7}</b> in the world in terms of total cashew yield.</h4>
                            <table>
                            <tr>
                                <th></th>
                                <th>Satellite Est</th>
                                <th>TNS Survey</th>
                                <th>Port Data</th>
                            </tr>
                            <tr>
                                <td>Total Cashew Yield (kg)</td>
                                <td></td>
                                <td>{3}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Cashew Tree Cover (ha)</td>
                                <td>{4}</td>
                                <td>{5}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield/Hectare (kg/ha)</td>
                                <td></td>
                                <td>{8}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield per Tree (kg/tree)</td>
                                <td></td>
                                <td>{9}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Number of Trees</td>
                                <td></td>
                                <td>{10}</td>
                                <td></td>
                            </tr>
                            </table>
                            <h5>
                            *Disclaimer: The data shown above are just for presentation purpose, they do not represent the real cashew statistics in Benin republic.
                            </h5>
                            <table>
                                <td><div id="piechart_div" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>
                            <table>
                                <td><div id="dual_x_div" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>
                            <table>
                                <td><div id="donutchart" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>

                        </body>
                        </html>'''.format(name, pred_ben_data, pred_ground_ben_data, total_yield, tree_ha_pred, surface_area, abs(round(surface_area - tree_ha_pred,2)), '6th',
                            yield_ha, yield_tree, num_tree, sick_tree, out_prod_tree, dead_tree, num_tree- sick_tree- out_prod_tree- dead_tree)



            iframe = folium.IFrame(html=html4, width=450, height=380)

            folium.Popup(iframe, max_width=2000).add_to(temp_layer0)

            # consolidate individual features back into the main layer



        # m.add_child(json_layer_ben)

            temp_layer0.add_to(layer0)

        layer0.add_to(m)

        layer = folium.FeatureGroup(name='Benin Departments', show=False, overlay = False)


        temp_geojson  = folium.GeoJson(data=benin_adm1_json,
            name='Benin-Adm1 Department',
            highlight_function = highlight_function)


        for feature in temp_geojson.data['features']:
            # GEOJSON layer consisting of a single feature
            name = feature["properties"]["NAME_1"]

            y1 = dtstats_df[dtstats_df['Districts']==name]['Communes']

            # getting values against each value of y

            x1 = dtstats_df[dtstats_df['Districts']==name]['Cashew_Yield']/10000

            z1 = zip(y1,x1)

            c_y1 = dtstats_df1[dtstats_df1['Country']=='Benin']['Districts']
            z_list = []
            for c_y in c_y1:
                c_x = round(sum(ben_yield[ben_yield['Departement']==c_y]['2020 total yield (kg)'].dropna()),2)
                z_list.append((c_y, c_x))

            sorted_by_second = sorted(z_list, reverse = True, key=lambda tup: tup[1])
            list1, _ = zip(*sorted_by_second)
            position = list1.index(name)
            my_dict = {'0': "highest", '1': "2nd", '2': "3rd", '3': "4th", '4': "5th", '5': "6th", '6': "7th", '7': "8th", '8': "9th", '9': "10th", '10': "11th", '11':"lowest"}

            pred_dept_data = []
            pred_ground_dept_data = [['Communes', 'Satellite Prediction', 'Ground Data Estimate']]
            for (y,x) in z1:
                x_new = round(sum(ben_yield[ben_yield['Commune']==y]['2020 estimated surface (ha)'].dropna()),2)    
                pred_dept_data.append([y, x])
                pred_ground_dept_data.append([y, x, x_new*100])

            temp_layer1 = folium.GeoJson(feature, zoom_on_click = True, highlight_function = highlight_function)

            tree_ha_pred_dept = round(sum(dtstats_df[dtstats_df['Districts']==name].Cashew_Yield)/10000,2)
            surface_areaD = round(sum(ben_yield[ben_yield['Departement']==name]['2020 estimated surface (ha)'].dropna())*100,2)
            total_yieldD = round(sum(ben_yield[ben_yield['Departement']==name]['2020 total yield (kg)'].dropna()),2)
            yield_haD = round(sum(ben_yield[ben_yield['Departement']==name]['2020 yield per ha (kg)'].dropna()),2)
            yield_treeD = round(sum(ben_yield[ben_yield['Departement']==name]['2020 yield per tree (kg)'].dropna()),2)
            num_treeD = int(sum(ben_yield[ben_yield['Departement']==name]['Number of trees'].dropna()))
            sick_treeD = int(sum(ben_yield[ben_yield['Departement']==name]['Number of sick trees'].dropna()))
            out_prod_treeD = int(sum(ben_yield[ben_yield['Departement']==name]['Number of trees out of production'].dropna()))
            dead_treeD = int(sum(ben_yield[ben_yield['Departement']==name]['Number of dead trees'].dropna()))


            html3 = '''
                    <html>
                        <head>
                        <style>
                            table {{
                            font-family: arial, sans-serif;
                            border-collapse: collapse;
                            width: 100%;
                            }}


                            table th {{
                            background-color: #004b55;
                            text-align: left;
                            color: #FFF;
                            padding: 4px 30px 4px 8px;
                            }}


                            table td {{
                            border: 1px solid #e3e3e3;
                            padding: 4px 8px;
                            }}


                            table tr:nth-child(odd) td{{
                            background-color: #e7edf0;
                            }}
                            </style>
                            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
                            <script type="text/javascript">
                            // Load Charts and the corechart and barchart packages.
                            google.charts.load('current', {{'packages':['corechart']}});
                            google.charts.load('current', {{'packages':['bar']}});

                            // Draw the pie chart and bar chart when Charts is loaded.
                            google.charts.setOnLoadCallback(drawChart);

                            function drawChart() {{

                                var pie_data = new google.visualization.DataTable();
                                pie_data.addColumn('string', 'Commune');
                                pie_data.addColumn('number', 'Cashew Tree Cover');
                                pie_data.addRows({1});

                                var piechart_options = {{title:'Pie Chart: Predicted Cashew Tree Cover Communes Statistics In {0}',
                                            width:400,
                                            height:350,
                                            is3D: true}};
                                var piechart = new google.visualization.PieChart(document.getElementById('piechart_div'));
                                piechart.draw(pie_data, piechart_options);

                                var data = new google.visualization.arrayToDataTable({2});

                                var options = {{
                                    chart: {{
                                        title: 'Cashew Tree Cover Relative Statistics in {0}',
                                    }},
                                    bars: 'horizontal', // Required for Material Bar Charts.
                                    colors: ['#02a8b1', '#242526'],
                                    is3D: true,

                                    axes: {{
                                            x: {{
                                            0: {{label: 'Cashew Tree Cover (ha)'}}, // Bottom x-axis.
                                            }}
                                        }}
                                        }};

                                var chart = new google.charts.Bar(document.getElementById('dual_x_div'));
                                chart.draw(data, options);

                                var data_donut = google.visualization.arrayToDataTable([
                                ['Tree Type', 'Number of Trees'],
                                ['Active Trees',      {14}],
                                ['Sick Trees',      {11}],
                                ['Dead Trees',     {13}],
                                ['Out of Production Trees',      {12}],
                                ]);

                                var options_donut = {{
                                title: 'Cashew Trees Status in {0}',
                                pieHole: 0.5,
                                colors: ['007f00', '#02a8b1', '9e1a1a', '#242526'],
                                }};

                                var chart_donut = new google.visualization.PieChart(document.getElementById('donutchart'));
                                chart_donut.draw(data_donut, options_donut);

                                }};
                            </script>
                        </head>
                        <body>
                            <h2>{0}</h2>
                            <h4>In 2020, {0} was ranked <b>{5}</b> among Benin departments in terms of total cashew yield according to the TNS Yield Survey.</h4>
                            <table>
                            <tr>
                                <th></th>
                                <th>Satellite Est</th>
                                <th>TNS Survey</th>
                                <th>Port Data</th>
                            </tr>
                            <tr>
                                <td>Total Cashew Yield (kg)</td>
                                <td></td>
                                <td>{3}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Cashew Tree Cover (ha)</td>
                                <td>{4}</td>
                                <td>{5}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield/Hectare (kg/ha)</td>
                                <td></td>
                                <td>{8}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield per Tree (kg/tree)</td>
                                <td></td>
                                <td>{9}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Number of Trees</td>
                                <td></td>
                                <td>{10}</td>
                                <td></td>
                            </tr>
                            </table>
                            <h5>
                            *Disclaimer: The data shown above are just for presentation purpose, they do not represent the real cashew statistics in Benin republic.
                            </h5>
                            <table>
                                <td><div id="piechart_div" style="border: 3px solid #00a5a7"></div></td>
                            </table>
                            <table>
                                <td><div id="dual_x_div" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>
                            <table>
                                <td><div id="donutchart" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>
                        </body>
                        </html>
                    '''.format(name, pred_dept_data, pred_ground_dept_data, total_yieldD, tree_ha_pred_dept, surface_areaD, abs(round(surface_areaD - tree_ha_pred_dept,2)), my_dict[str(position)],
                            yield_haD, yield_treeD, num_treeD, sick_treeD, out_prod_treeD, dead_treeD, num_treeD-sick_treeD-out_prod_treeD-dead_treeD)

            iframe = folium.IFrame(html=html3, width=450, height=380)

            folium.Popup(iframe, max_width=2000).add_to(temp_layer1)

            # consolidate individual features back into the main layer



            folium.GeoJsonTooltip(fields=["NAME_1"],
                aliases = ["Department:"],
                labels = True,
                sticky = False,
                style=("background-color: white; color: black; font-family: sans-serif; font-size: 12px; padding: 4px;")
                ).add_to(temp_layer1)

            temp_layer1.add_to(layer)

        layer.add_to(m)

        # Communes section

        layer2 = folium.FeatureGroup(name='Benin Communes', show=False, overlay = False)


        temp_geojson2 = folium.GeoJson(data = benin_adm2_json,
            name = 'Benin-Adm2 Communes',
            highlight_function = highlight_function)


        for feature in temp_geojson2.data['features']:
            # GEOJSON layer consisting of a single feature
            name = feature["properties"]["NAME_2"]

            c_y2 = dtstats_df['Communes']

            z_list_2 = []
            for c_y in c_y2:
                c_x = round(sum(ben_yield[ben_yield['Commune']==c_y]['2020 estimated surface (ha)'].dropna())*100,2)
                z_list_2.append((c_y, c_x))

            sorted_by_second2 = sorted(z_list_2, reverse = True, key=lambda tup: tup[1])
            list2, _ = zip(*sorted_by_second2)
            position2 = list2.index(name)          
            my_dict_communes = {'1': 'highest',
                    '2': '2nd',
                    '3': '3rd',
                    '4': '4th',
                    '5': '5th',
                    '6': '6th',
                    '7': '7th',
                    '8': '8th',
                    '9': '9th',
                    '10': '10th',
                    '11': '11th',
                    '12': '12th',
                    '13': '13th',
                    '14': '14th',
                    '15': '15th',
                    '16': '16th',
                    '17': '17th',
                    '18': '18th',
                    '19': '19th',
                    '20': '20th',
                    '21': '21st',
                    '22': '22nd',
                    '23': '23rd',
                    '24': '24th',
                    '25': '25th',
                    '26': '26th',
                    '27': '27th',
                    '28': '28th',
                    '29': '29th',
                    '30': '30th',
                    '31': '31st',
                    '32': '32nd',
                    '33': '33rd',
                    '34': '34th',
                    '35': '35th',
                    '36': '36th',
                    '37': '37th',
                    '38': '38th',
                    '39': '39th',
                    '40': '40th',
                    '41': '41st',
                    '42': '42nd',
                    '43': '43rd',
                    '44': '44th',
                    '45': '45th',
                    '46': '46th',
                    '47': '47th',
                    '48': '48th',
                    '49': '49th',
                    '50': '50th',
                    '51': '51st',
                    '52': '52nd',
                    '53': '53rd',
                    '54': '54th',
                    '55': '55th',
                    '56': '56th',
                    '57': '57th',
                    '58': '58th',
                    '59': '59th',
                    '60': '60th',
                    '61': '61st',
                    '62': '62nd',
                    '63': '63rd',
                    '64': '64th',
                    '65': '65th',
                    '66': '66th',
                    '67': '67th',
                    '68': '68th',
                    '69': '69th',
                    '70': '70th',
                    '71': '71st',
                    '72': '72nd',
                    '73': '73rd',
                    '74': '74th',
                    '75': '75th',
                    '76': 'lowest'}

            temp_layer2 = folium.GeoJson(feature,  zoom_on_click = True, highlight_function = highlight_function)

            name = feature['properties']['NAME_2']
            tree_ha_pred_comm = round(sum(dtstats_df[dtstats_df['Communes']==name].Cashew_Yield)/10000,2)
            surface_areaC = round(sum(ben_yield[ben_yield['Commune']==name]['2020 estimated surface (ha)'].dropna())*100,2)
            total_yieldC = round(sum(ben_yield[ben_yield['Commune']==name]['2020 total yield (kg)'].dropna()),2)
            yield_haC = round(np.mean(ben_yield[ben_yield['Commune']==name]['2020 yield per ha (kg)'].dropna()),2)
            yield_treeC = round(sum(ben_yield[ben_yield['Commune']==name]['2020 yield per tree (kg)'].dropna()),2)
            num_treeC = int(sum(ben_yield[ben_yield['Commune']==name]['Number of trees'].dropna()))
            sick_treeC = int(sum(ben_yield[ben_yield['Commune']==name]['Number of sick trees'].dropna()))
            out_prod_treeC = int(sum(ben_yield[ben_yield['Commune']==name]['Number of trees out of production'].dropna()))
            dead_treeC = int(sum(ben_yield[ben_yield['Commune']==name]['Number of dead trees'].dropna()))


            html3 = '''
                    <html>
                    <head>
                        <style>
                            table {{
                            font-family: arial, sans-serif;
                            border-collapse: collapse;
                            width: 100%;
                            }}


                            table th {{
                            background-color: #004b55;
                            text-align: left;
                            color: #FFF;
                            padding: 4px 30px 4px 8px;
                            }}


                            table td {{
                            border: 1px solid #e3e3e3;
                            padding: 4px 8px;
                            }}


                            table tr:nth-child(odd) td{{
                            background-color: #e7edf0;
                            }}
                            </style>
                            <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
                            <script type="text/javascript">
                            // Load Charts and the corechart and barchart packages.
                            google.charts.load('current', {{'packages':['corechart']}});
                            google.charts.load('current', {{'packages':['bar']}});

                            // Draw the pie chart and bar chart when Charts is loaded.
                            google.charts.setOnLoadCallback(drawChart);

                            function drawChart() {{

                                var data_donut = google.visualization.arrayToDataTable([
                                ['Tree Type', 'Number of Trees'],
                                ['Active Trees',      {12}],
                                ['Sick Trees',      {9}],
                                ['Dead Trees',     {11}],
                                ['Out of Production Trees',      {10}],
                                ]);

                                var options_donut = {{
                                title: 'Cashew Trees Status in {0}',
                                pieHole: 0.5,
                                colors: ['007f00', '#02a8b1', '9e1a1a', '#242526'],
                                }};

                                var chart_donut = new google.visualization.PieChart(document.getElementById('donutchart'));
                                chart_donut.draw(data_donut, options_donut);

                                }};
                            </script>
                        </head>
                        <body>

                            <h2>{0}</h2>
                            <h4>In 2020, {0} was ranked <b>{5}</b> among Benin communes in terms of total cashew yield according to the TNS Yield Survey.</h4>
                            <table>
                            <tr>
                                <th></th>
                                <th>Satellite Est</th>
                                <th>TNS Survey</th>
                                <th>Port Data</th>
                            </tr>
                            <tr>
                                <td>Total Cashew Yield (kg)</td>
                                <td></td>
                                <td>{1}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Cashew Tree Cover (ha)</td>
                                <td>{2}</td>
                                <td>{3}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield/Hectare (kg/ha)</td>
                                <td></td>
                                <td>{6}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Yield per Tree (kg/tree)</td>
                                <td></td>
                                <td>{7}</td>
                                <td></td>
                            </tr>
                            <tr>
                                <td>Number of Trees</td>
                                <td></td>
                                <td>{8}</td>
                                <td></td>
                            </tr>
                            </table>
                            <h5>
                            *Disclaimer: The data shown above are just for presentation purpose, they do not represent the real cashew statistics in Benin republic.
                            </h5>
                            <table>
                                <td><div id="donutchart" style="width: 400; height: 350;border: 3px solid #00a5a7"></div></td>
                            </table>
                        </body>
                        </html>
                    '''.format(name, total_yieldC, tree_ha_pred_comm, surface_areaC, abs(round(surface_areaC - tree_ha_pred_comm,2)), my_dict_communes[str(position2+1)],
                            yield_haC, yield_treeC, num_treeC, sick_treeC, out_prod_treeC, dead_treeC,num_treeC-sick_treeC-out_prod_treeC-dead_treeC)

            iframe = folium.IFrame(html=html3, width=450, height=380)

            folium.Popup(iframe, max_width=2000).add_to(temp_layer2)

            # consolidate individual features back into the main layer



        # m.add_child(json_layer_ben)

            folium.GeoJsonTooltip(fields=["NAME_2"],
                aliases = ["Commune:"],
                labels = True,
                sticky = False,
                style=("background-color: white; color: black; font-family: sans-serif; font-size: 12px; padding: 4px;")
                ).add_to(temp_layer2)

            temp_layer2.add_to(layer2)

        layer2.add_to(m)

        m.add_child(folium.LayerControl())


        m=m._repr_html_()
        context = {'my_map': m}

        ## rendering
        return context


@login_required(login_url="/login/")
def index(request):

    home_obj = my_home()
    context = home_obj.get_context_data()
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
