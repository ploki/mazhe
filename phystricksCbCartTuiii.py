from phystricks import *
def CbCartTuiii():
    pspict,fig = SinglePicture("CbCartTuiii")

    x=var('x')
    f1=phyFunction(sin(2*x))
    f2=phyFunction(sin(3*x))

    courbe=ParametricCurve(f1,f2).graph(0,2*pi)

    pspict.DrawGraphs(courbe)
    pspict.DrawDefaultAxes()
    pspict.dilatation(2)
    fig.conclude()
    fig.write_the_file()
