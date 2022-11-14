import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

# loading the csv file and preprocessing it
data = pd.read_parquet('data.parquet')
print(data.head())
d_copy = data.copy()
print(d_copy.dtypes)

fig_1 = d_copy.groupby(["year", 'month', 'member_casual'], as_index=False).count()
fig_1 = fig_1[fig_1['ride_id'] != 0]
fig_2 = d_copy.groupby(["day_of_week", "member_casual"], as_index=False).count()
fig_3 = d_copy.groupby(['hour', 'member_casual'], as_index=False).count()
fig_4 = round(d_copy.groupby('member_casual', as_index=False).mean(), 0)
fig_5 = round(d_copy.groupby(["year", 'month', 'member_casual'], as_index=False).mean(), 1).dropna()
fig_6 = round(d_copy.groupby(['day_of_week', 'member_casual'], as_index=False).mean(), 1)
fig_7 = d_copy.groupby(['rideable_type', 'member_casual'], as_index=False).count()

total_rides = d_copy["member_casual"].value_counts().reset_index(name="Total_Rides")
total_rides['Total_Rides%'] = total_rides['Total_Rides'] / sum(total_rides['Total_Rides']) * 100

# Page 1 cards
card_1_1 = dbc.Card([
    dbc.CardHeader("% of Rides"),
    dbc.CardBody(
        [
            html.H3("Casual", className="card-title"),
            html.H5(
                "43.4%",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_2_1 = dbc.Card([
    dbc.CardHeader("% of Rides"),
    dbc.CardBody(
        [
            html.H3("Members", className="card-title"),
            html.H5(
                "56.6%",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_3_1 = dbc.Card([
    dbc.CardHeader("Most Used Bike"),
    dbc.CardBody(
        [
            html.H3("Casual", className="card-title"),
            html.H5(
                "Classic Bike",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_4_1 = dbc.Card([
    dbc.CardHeader("Least Used Bike"),
    dbc.CardBody(
        [
            html.H3("Casual", className="card-title"),
            html.H5(
                "Docked",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_5_1 = dbc.Card([
    dbc.CardHeader("Most Used Bike"),
    dbc.CardBody(
        [
            html.H3("Member", className="card-title"),
            html.H5(
                "Classic",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_6_1 = dbc.Card([
    dbc.CardHeader("Least Used Bike"),
    dbc.CardBody(
        [
            html.H3("Member", className="card-title"),
            html.H5(
                "Docked",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

# Page 2 cards
# card_1_2 = dbc.Card([
#     dbc.CardHeader("Highest Month Casual"),
#     dbc.CardBody(
#         [
#             html.H3("June", className="card-title"),
#             html.H5(
#                 "364.197k",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_2_2 = dbc.Card([
#     dbc.CardHeader("Lowest Month Casual"),
#     dbc.CardBody(
#         [
#             html.H3("January", className="card-title"),
#             html.H5(
#                 "12.433k",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_3_2 = dbc.Card([
#     dbc.CardHeader("Highest Month Member"),
#     dbc.CardBody(
#         [
#             html.H3("August", className="card-title"),
#             html.H5(
#                 "326.15k",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_4_2 = dbc.Card([
#     dbc.CardHeader("Lowest Month Member"),
#     dbc.CardBody(
#         [
#             html.H3("January", className="card-title"),
#             html.H5(
#                 "66.126k",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_5_2 = dbc.Card([
#     dbc.CardHeader("Highest Day Casual"),
#     dbc.CardBody(
#         [
#             html.H3("Saturday", className="card-title"),
#             html.H5(
#                 "441.549k",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_6_2 = dbc.Card([
#     dbc.CardHeader("Lowest Day Casual"),
#     dbc.CardBody(
#         [
#             html.H3("Tuesday", className="card-title"),
#             html.H5(
#                 "215.022k",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_7_2 = dbc.Card([
#     dbc.CardHeader("Highest Day Member"),
#     dbc.CardBody(
#         [
#             html.H3("Tuesday", className="card-title"),
#             html.H5(
#                 "416.059k",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_8_2 = dbc.Card([
#     dbc.CardHeader("Lowest Day Member"),
#     dbc.CardBody(
#         [
#             html.H3("Sunday", className="card-title"),
#             html.H5(
#                 "306.755k",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

# Page 3 cards
card_1_3 = dbc.Card([
    dbc.CardHeader("Busiest Hour Casual"),
    dbc.CardBody(
        [
            html.H3("17th", className="card-title"),
            html.H5(
                "189.28k",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_2_3 = dbc.Card([
    dbc.CardHeader("Slowest Hour Casual"),
    dbc.CardBody(
        [
            html.H3("4th", className="card-title"),
            html.H5(
                "6.571k",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_3_3 = dbc.Card([
    dbc.CardHeader("Busiest Hour Member"),
    dbc.CardBody(
        [
            html.H3("17th", className="card-title"),
            html.H5(
                "280.583k",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_4_3 = dbc.Card([
    dbc.CardHeader("Slowest Hour Member"),
    dbc.CardBody(
        [
            html.H3("3rd", className="card-title"),
            html.H5(
                "5.404k",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_5_3 = dbc.Card([
    dbc.CardHeader("Av. Ride Length"),
    dbc.CardBody(
        [
            html.H3("Casual", className="card-title"),
            html.H5(
                "31 min",
                className="card-title", style={"color": "green"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

card_6_3 = dbc.Card([
    dbc.CardHeader("Av. Ride Length"),
    dbc.CardBody(
        [
            html.H3("Member", className="card-title"),
            html.H5(
                "13 min",
                className="card-title", style={"color": "red"}
            ),
        ]
    ),
], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

# Page 4 cards
# card_1_4 = dbc.Card([
#     dbc.CardHeader("Longest Rides Casual"),
#     dbc.CardBody(
#         [
#             html.H3("June", className="card-title"),
#             html.H5(
#                 "39.1 min",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_2_4 = dbc.Card([
#     dbc.CardHeader("Shortest Rides Casual"),
#     dbc.CardBody(
#         [
#             html.H3("November", className="card-title"),
#             html.H5(
#                 "22.8 min",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_3_4 = dbc.Card([
#     dbc.CardHeader("Longest Rides Member"),
#     dbc.CardBody(
#         [
#             html.H3("June", className="card-title"),
#             html.H5(
#                 "14.4 min",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_4_4 = dbc.Card([
#     dbc.CardHeader("Shortest Rides Member"),
#     dbc.CardBody(
#         [
#             html.H3("January", className="card-title"),
#             html.H5(
#                 "10.5 min",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_5_4 = dbc.Card([
#     dbc.CardHeader("Longest Rides Casual"),
#     dbc.CardBody(
#         [
#             html.H3("Sunday", className="card-title"),
#             html.H5(
#                 "34.7 min",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_6_4 = dbc.Card([
#     dbc.CardHeader("Shortest Rides Casual"),
#     dbc.CardBody(
#         [
#             html.H3("Tuesday", className="card-title"),
#             html.H5(
#                 "26.5 min",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_7_4 = dbc.Card([
#     dbc.CardHeader("Longest Rides Member"),
#     dbc.CardBody(
#         [
#             html.H3("Sunday", className="card-title"),
#             html.H5(
#                 "14.8 min",
#                 className="card-title", style={"color": "green"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})
#
# card_8_4 = dbc.Card([
#     dbc.CardHeader("Shortest Rides Member"),
#     dbc.CardBody(
#         [
#             html.H3("Tuesday", className="card-title"),
#             html.H5(
#                 "12.1 min",
#                 className="card-title", style={"color": "red"}
#             ),
#         ]
#     ),
# ], style={"font-family": "Georgia, serif", "textAlign": "center", "fontWeight": "bold", "fontSize": "13px"})

# instantiating the dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

# sidebar
sidebar = dbc.Card([
    dbc.CardBody([
        html.P("Casual Riders Vs Annual Members", className="lead",
               style={"font-family": "Comic Sans MS"}),
        html.Hr(),
        html.P(
            "Navigation", className="lead",
            style={"font-family": "Comic Sans MS"}
        ),
        dbc.Nav([
            dbc.NavLink("Home", href="/", active="exact"),
            # dbc.NavLink("Page 2", href="/page-2", active="exact"),
            dbc.NavLink("Page 3", href="/page-3", active="exact"),
            # dbc.NavLink("Page 4", href="/page-4", active="exact")
        ], vertical=True, pills=True, style={"font-family": "Comic Sans MS"}),
        dcc.Markdown('''
                * [Analysis Notebook](https://www.kaggle.com/chrispinetot/cyclistic-bike-share-python)

        ''',
                     link_target="_blank", style={"font-family": "Comic Sans MS"})

    ])
], color="#353935", style={"height": "100vh",
                           "width": "16rem", "position": "fixed"})

content = html.Div(id="page-content", style={"padding": "2rem"})

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(sidebar, width=2),
        dbc.Col(content, width=9, style={"margin-left": "16rem"})
    ]),

], fluid=True)


# callback
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            dbc.Row([
                dbc.Col([html.A(
                    href="https://www.coursera.org/account/accomplishments/specialization/certificate/X9KV8JFNGKL2",
                    target="_blank",
                    children=[
                        html.Img(
                            alt="link to Certificate",
                            src="assets/bike_2.png",
                            style={
                                'height': '60px',
                                'width': 'auto',
                                'margin-bottom': '25px'
                            }
                        )
                    ]
                )], width=1),
                dbc.Col([html.H2("Cyclistic Bike Share Dashboard",
                                 style={"textAlign": "center", "font-family": "Georgia, serif"})
                         ], style={"margin-right": "4rem"})
            ], justify="center"),
            dbc.Row([
                dbc.Col(card_1_1, width=3),
                dbc.Col(card_2_1, width=3)
            ], justify="center"),
            dcc.Graph(id="piechart", config={'displayModeBar': False},
                      figure=px.pie(total_rides, values="Total_Rides%", names="index",
                                    color_discrete_sequence=px.colors.qualitative.Vivid,
                                    labels={"index": "Membership_Type"},
                                    hole=0.6).update_layout(font_family="Georgia, serif",
                                                            font_color="#0070ff",
                                                            legend_title_font_color="green",
                                                            paper_bgcolor='rgba(0,0,0,0)').update_xaxes(
                          title_font_family="Georgia, serif").update_traces(textposition="outside",
                                                                            textinfo="percent+label",
                                                                            marker=dict(line=dict(width=1)),
                                                                            pull=[0, 0],
                                                                            rotation=0)),
            dbc.Row([
                dbc.Col(card_3_1, width=3),
                dbc.Col(card_4_1, width=3),
                dbc.Col(card_5_1, width=3),
                dbc.Col(card_6_1, width=3)
            ]),
            dcc.Graph(id="bargraph", config={'displayModeBar': False},
                      figure=px.bar(fig_7, x='rideable_type', y='ride_id',
                                    color='member_casual',
                                    barmode='group',
                                    labels={'ride_id': 'No. of Rides', 'member_casual': "Membership_Type",
                                            'rideable_type': 'Bike Type'},
                                    hover_name='ride_id',
                                    hover_data={'member_casual': True, 'ride_length': False, "ride_id": False},
                                    color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
                          font_family="Georgia, serif",
                          font_color="#0070ff",
                          legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)').update_xaxes(showgrid=False, showline=False,
                                                                     title_font_family="Georgia, serif").update_yaxes(
                          zeroline=False, showgrid=False)
                      )
        ]
    # elif pathname == "/page-2":
    #     return [
    #         html.Link(rel='shortcut icon', type='favicon.ico', href="assets/bike_2.png"),
    #         dbc.Row([
    #             dbc.Col([html.A(
    #                 href="https://www.coursera.org/account/accomplishments/specialization/certificate/X9KV8JFNGKL2",
    #                 target="_blank",
    #                 children=[
    #                     html.Img(
    #                         alt="link to Certificate",
    #                         src="assets/bike_2.png",
    #                         style={
    #                             'height': '60px',
    #                             'width': 'auto',
    #                             'margin-bottom': '25px'
    #                         }
    #                     )
    #                 ]
    #             )], width=1),
    #             dbc.Col([html.H2("Cyclistic Bike Share Dashboard",
    #                              style={"textAlign": "center", "font-family": "Georgia, serif"})
    #                      ], style={"margin-right": "4rem"})
    #         ], justify="center"),
    #         dbc.Row([
    #             dbc.Col(card_1_2, width=3),
    #             dbc.Col(card_2_2, width=3),
    #             dbc.Col(card_3_2, width=3),
    #             dbc.Col(card_4_2, width=3)
    #         ]),
    #
    #         dcc.Graph(id="linegraph", config={'displayModeBar': False},
    #                   figure=px.line(fig_1, x=fig_1['month'], y='ride_id', range_y=[0, 400000],
    #                                  color='member_casual',
    #                                  line_shape='linear',
    #                                  markers=True,
    #                                  labels={'ride_id': 'No. of Rides',
    #                                          'month': '',
    #                                          'member_casual': 'Membership_Type'},
    #                                  hover_name='year',
    #                                  hover_data={'member_casual': False, 'month': True, 'ride_id': True},
    #                                  color_discrete_sequence=px.colors.qualitative.Vivid,
    #                                  ).update_layout(font_family="Georgia, serif",
    #                                                  font_color="#0070ff",
    #                                                  legend_title_font_color="green",
    #                                                  paper_bgcolor='rgba(0,0,0,0)',
    #                                                  plot_bgcolor='rgba(0,0,0,0)').update_xaxes(
    #                       title_font_family="Georgia, serif",
    #                       showgrid=False).update_yaxes(zeroline=False, showgrid=False)),
    #         dbc.Row([
    #             dbc.Col(card_5_2, width=3),
    #             dbc.Col(card_6_2, width=3),
    #             dbc.Col(card_7_2, width=3),
    #             dbc.Col(card_8_2, width=3)
    #         ]),
    #         dcc.Graph(id="bargraph", config={'displayModeBar': False},
    #                   figure=px.line(fig_2, x='day_of_week', y='ride_id', range_y=[0, 500000],
    #                                  color='member_casual',
    #                                  line_shape='linear',
    #                                  markers=True,
    #                                  labels={'ride_id': 'No. of Rides', 'day_of_week': 'Day',
    #                                          'member_casual': 'Membership_Type'},
    #                                  hover_name='member_casual',
    #                                  hover_data={'member_casual': False, 'month': False, 'ride_id': True},
    #                                  color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
    #                       font_family="Georgia, serif",
    #                       font_color="#0070ff",
    #                       legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
    #                       plot_bgcolor='rgba(0,0,0,0)').update_xaxes(showgrid=False, zeroline=False,
    #                                                                  title_font_family="Georgia, serif").update_yaxes(
    #                       zeroline=False, showgrid=False))
    #     ]
    elif pathname == "/page-3":
        return [
            html.Link(rel='shortcut icon', type='favicon.ico', href="assets/bike_2.png"),
            dbc.Row([
                dbc.Col([html.A(
                    href="https://www.coursera.org/account/accomplishments/specialization/certificate/X9KV8JFNGKL2",
                    target="_blank",
                    children=[
                        html.Img(
                            alt="link to Certificate",
                            src="assets/bike_2.png",
                            style={
                                'height': '60px',
                                'width': 'auto',
                                'margin-bottom': '25px'
                            }
                        )
                    ]
                )], width=1),
                dbc.Col([html.H2("Cyclistic Bike Share Dashboard",
                                 style={"textAlign": "center", "font-family": "Georgia, serif"})
                         ], style={"margin-right": "4rem"})
            ], justify="center"),
            dbc.Row([
                dbc.Col(card_1_3, width=3),
                dbc.Col(card_2_3, width=3),
                dbc.Col(card_3_3, width=3),
                dbc.Col(card_4_3, width=3)
            ]),
            dcc.Graph(id="bargraph", config={'displayModeBar': False},
                      figure=px.line(fig_3, x='hour', y='ride_id', range_x=[0, 23], range_y=[0, 300000],
                                     color='member_casual',
                                     line_shape='linear',
                                     markers=True,
                                     labels={'ride_id': 'No. of Rides', 'hour': 'Hour',
                                             'member_casual': 'Membership_Type'},
                                     hover_name='member_casual',
                                     hover_data={'member_casual': False, 'month': False, 'ride_id': True},
                                     color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
                          font_family="Georgia, serif",
                          font_color="#0070ff",
                          legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)').update_xaxes(zeroline=False, showgrid=False,
                                                                     title_font_family="Georgia, serif", dtick=1,
                                                                     rangeslider_visible=False).update_yaxes(
                          zeroline=False, showgrid=False)),
            dbc.Row([
                dbc.Col(card_5_3, width=3),
                dbc.Col(card_6_3, width=3)
            ], justify="center"),
            dcc.Graph(id="bargraph2", config={'displayModeBar': False},
                      figure=px.bar(fig_4, y='member_casual', x='ride_length', range_x=[0, 40],
                                    color='member_casual',
                                    height=300,
                                    text='ride_length',
                                    labels={'ride_length': 'Average Ride Length (min)',
                                            'member_casual': 'Membership_Type'},
                                    hover_name='member_casual',
                                    hover_data={'member_casual': False, 'ride_length': True},
                                    color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
                          font_family="Georgia, serif",
                          font_color="#0070ff",
                          legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)').update_xaxes(zeroline=False, showgrid=False,
                                                                     title_font_family="Georgia, serif").update_yaxes(
                          showgrid=False))
        ]
    # elif pathname == "/page-4":
    #     return [
    #         html.Link(rel='shortcut icon', type='favicon.ico', href="assets/bike_2.png"),
    #         dbc.Row([
    #             dbc.Col([html.A(
    #                 href="https://www.coursera.org/account/accomplishments/specialization/certificate/X9KV8JFNGKL2",
    #                 target="_blank",
    #                 children=[
    #                     html.Img(
    #                         alt="link to Certificate",
    #                         src="assets/bike_2.png",
    #                         style={
    #                             'height': '60px',
    #                             'width': 'auto',
    #                             'margin-bottom': '25px'
    #                         }
    #                     )
    #                 ]
    #             )], width=1),
    #             dbc.Col([html.H2("Cyclistic Bike Share Dashboard",
    #                              style={"textAlign": "center", "font-family": "Georgia, serif"})
    #                      ], style={"margin-right": "4rem"})
    #         ], justify="center"),
    #         dbc.Row([
    #             dbc.Col(card_1_4, width=3),
    #             dbc.Col(card_2_4, width=3),
    #             dbc.Col(card_3_4, width=3),
    #             dbc.Col(card_4_4, width=3)
    #         ]),
    #         dcc.Graph(id="bargraph", config={'displayModeBar': False},
    #                   figure=px.bar(fig_5, x='month', y='ride_length',
    #                                 color='member_casual',
    #                                 barmode='group',
    #                                 labels={'ride_length': 'Average Ride Length (min)',
    #                                         'member_casual': 'Membership_Type',
    #                                         'month': ''},
    #                                 hover_name="ride_length", hover_data={'member_casual': True, 'ride_length': False},
    #                                 color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
    #                       font_family="Georgia, serif",
    #                       font_color="#0070ff",
    #                       legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
    #                       plot_bgcolor='rgba(0,0,0,0)').update_xaxes(showgrid=False,
    #                                                                  title_font_family="Georgia, serif").update_yaxes(
    #                       zeroline=False, showgrid=False)
    #                   ),
    #         dbc.Row([
    #             dbc.Col(card_5_4, width=3),
    #             dbc.Col(card_6_4, width=3),
    #             dbc.Col(card_7_4, width=3),
    #             dbc.Col(card_8_4, width=3)
    #         ]),
    #         dcc.Graph(id="bargraph2", config={'displayModeBar': False},
    #                   figure=px.bar(fig_6, x='day_of_week', y='ride_length',
    #                                 color='member_casual',
    #                                 barmode='group',
    #                                 labels={'ride_length': 'Average Ride Length (minutes)',
    #                                         'member_casual': 'Membership_Type', 'day_of_week': 'Day'},
    #                                 hover_name='ride_length',
    #                                 hover_data={'member_casual': False, 'ride_length': True},
    #                                 color_discrete_sequence=px.colors.qualitative.Vivid).update_layout(
    #                       font_family="Georgia, serif",
    #                       font_color="#0070ff",
    #                       legend_title_font_color="green", paper_bgcolor='rgba(0,0,0,0)',
    #                       plot_bgcolor='rgba(0,0,0,0)').update_xaxes(showgrid=False,
    #                                                                  title_font_family="Georgia, serif").update_yaxes(
    #                       zeroline=False, showgrid=False))
    #     ]


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8080)
