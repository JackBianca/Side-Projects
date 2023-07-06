# Jack Bianca - 5/26/23
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.transform import transform, factor_cmap
from bokeh.models import LinearColorMapper
from bokeh.palettes import RdYlBu, Viridis256
import numpy as np
import pandas as pd

# Read in csv file
#df = pd.read_csv('3dMesh.csv')

#temp data
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(x**2 + y**2))


# Create ColumnDataSource from data frame
#source = ColumnDataSource(data=dict(
#    x=df['x'],
#    y=['y'],
#    z=['z']
#))

# output html file
output_file('3D_Mesh_Plot.html')

# Mesh list
#mesh_list = source.data['Mesh'].tolist()

# Add 3d plot
p = figure(
    title='3D Mesh Plot',
    sizing_mode='stretch_both',
    toolbar_location='above'
)
color_mapper = LinearColorMapper(
    palette = Viridis256,
    low=Z.min(), 
    high=Z.max()
),
p.wedge(
    x=X.flatten(),
    y=Y.flatten(),
    radius=0.05,
    start_angle=0,
    end_angle=2*np.pi,
    radius_units='data',
    fill_color=transform(
        'z',
        color_mapper
    ),
    line_color=None,
    alpha=0.6,
    source={
        'x':X.flatten(),
        'y':Y.flatten(),
        'z':Z.flatten()
    }
)

#x_axis_label = 'X Axis',
#y_axis_label = 'Y Axis',
#z_axis_label = 'Z Axis',
#tools="pan, wheel_zoom, box_zoom, save, reset, help"


# Create mesh glyph
#p.mesh(
#    x='x',
#    y='y',
#    z='z',
#    #source=source,
#    fill_color = factor_cmap(
#        'Mesh',
#        palette='RdYlBu',
#        factors=mesh_list
#    ),
#    alpha=0.8,
#    legend_field='Mesh'
#)

# Add Legend
p.legend.location='top_right'
p.legend.label_text_font_size='10px'
p.legend.label = 'Mesh'

# Show Results
show(p)

# Save File
#save(p)
