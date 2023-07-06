from bokeh.io import output_file, show
from bokeh.plotting import figure

# Define the data for the sphere
x=[0]
y=[0]
z=[0]
radius=[1]

# Define the bokeh plot
output_file('3d_sphere_plot.html')
p = figure(
    title='3D Sphere Plot',
    sizing_mode = 'stretch_both',
    toolbar_location='above',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

# Creates wedge shape that acts as sphere
p.wedge(
    x=x,
    y=y,
    radius=radius,
    start_angle=0,
    end_angle=360,
    radius_units='data',
    alpha=0.6
)

# Show the plot
show(p)