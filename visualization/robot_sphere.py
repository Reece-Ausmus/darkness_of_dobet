import vtk

reader = vtk.vtkPNGReader()
reader.SetFileName("dobot_pic.png")
reader.Update()

texture = vtk.vtkTexture()
texture.SetInputConnection(reader.GetOutputPort())

sphere = vtk.vtkSphereSource()
sphere.SetThetaResolution(50)
sphere.SetPhiResolution(50)

texture_map = vtk.vtkTextureMapToSphere()
texture_map.SetInputConnection(sphere.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(texture_map.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.GradientBackgroundOn()
renderer.SetBackground(249/255, 242/255, 237/255)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(800, 600)
render_window.SetWindowName('robot_sphere.py')

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

render_window.Render()
interactor.Start()