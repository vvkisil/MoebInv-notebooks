# MoebInv notebooks
This is a collections of Jupyter notebooks on Lie-Möbius sphere geometry [ [3] ](#[3]) and MoebInv package [ [4] ](#[4]). We discuss and discover mathematical aspects of the theory using the dedicated software.  The project is [hosted on GitHub](https://github.com/vvkisil/MoebInv-notebooks).

See the [annotated Table of Contents](https://github.com/vvkisil/MoebInv-notebooks/blob/master/Table_of_contents.md) as a Jupyter notebook.


## Running MoebInv notebooks
The code from these notebooks can be executed at Google CoLab after the installation of MoebInv library by a couple of mouse clicks.

Specifically, open the notebook with [library installation instructions](https://colab.research.google.com/github/vvkisil/MoebInv-notebooks/blob/master/Introduction/Software_installation_GUI_integration.ipynb) and execute one cells with scripts. Then you can run all other notebooks until your CoLab session will expire.

Alternatively these notebooks can be executed from  a [CodeOcean capsule](https://codeocean.com/capsule/7952650/tree).


## Introductory examples

+ **Euclidean and Lobachevsky lines** This notebook also show how to make initial software installation

   [⌘ View on Github](https://github.com/vvkisil/MoebInv-notebooks/blob/master/Introduction/Euclidean_and_Lobachevsky_lines.ipynb),  or [👁 HTML view](http://www1.maths.leeds.ac.uk/~kisilv/MoebInv-notebooks/Introduction/Euclidean_and_Lobachevsky_lines.html) or [⚙ Execute on Colab](https://colab.research.google.com/github/vvkisil/MoebInv-notebooks/blob/master/Introduction/Euclidean_and_Lobachevsky_lines.ipynb).

+ **Nine point theorem**: Some non-trivial illustrations on the celebrated result

   [⌘ View on
  Github](https://github.com/vvkisil/MoebInv-notebooks/blob/master/Introduction/Nine_point_theorem.ipynb),   or [👁 HTML view](http://www1.maths.leeds.ac.uk/~kisilv/MoebInv-notebooks/Introduction/Nine_point_theorem.html) or  [⚙ Execute on CoLab](https://colab.research.google.com/github/vvkisil/MoebInv-notebooks/blob/master/Introduction/Nine_point_theorem.ipynb).

* **Example of symbolic computations** Analytic proof of a simple geometric statement

   [⌘ View on
  Github](https://github.com/vvkisil/MoebInv-notebooks/blob/master/Introduction/Example_of_symbolic_computations.ipynb) or [👁 HTML view](http://www1.maths.leeds.ac.uk/~kisilv/MoebInv-notebooks/Introduction/Example_of_symbolic_computations.html) or  [⚙ Execute on CoLab](https://colab.research.google.com/github/vvkisil/MoebInv-notebooks/blob/master/Introduction/Example_of_symbolic_computations.ipynb).

+ **What is PyGiNaC?** Find out what Math can be done with it. 

  [⌘ View on GitHub](https://github.com/vvkisil/MoebInv-notebooks/tree/master/Geometry_of_cycles/Start_from_Basics/pyGiNaC.ipynb) or [👁 HTML view](http://www1.maths.leeds.ac.uk/~kisilv/MoebInv-notebooks/Geometry_of_cycles/Start_from_Basics/pyGiNaC.html) or [⚙ Execute on CoLab](https://colab.research.google.com/github/vvkisil/MoebInv-notebooks/blob/master/Geometry_of_cycles/Start_from_Basics/pyGiNaC.ipynb).

## Main folders

 + [Introduction](Introduction) -- a collection of quick-start examples

 + [Geometry_of_cycles](Geometry_of_cycles) -- main collection of notebooks

 + [EPAL-v1](EPAL-v1) -- Notebooks with all computer-assisted solutions of exercises from [ [2] ](#[2]).
 
 + [Appendix: illustrations](Appendix_Illustrations/) -- some examples of `MoebInv` usage which generate attractive graphics.

## Jupyter and MoebInv-GUI integration
There is a Graphical User Interface (GUI) to the MoebInv library. It allows to create and research geometrical constructions by mouse clicks. You may find a pre-compiled GUI binary distribution for your desktop platform at [SourceForge](https://sourceforge.net/projects/moebinv/files/binary/). 

There is bidirectional integration beetween Jupyter and GUI:

* From Jupyter (or any coding system in C++ or Python) use
 ``` python
 F.save("my-figure-archive.gar")
 ```
 to save GiNaC Gar archive. Later it can be loaded into GUI (or any other front-end, indeed).

* From GUI select
 ```
 File → Export figure → Export Python script
 ```
 in Main Menu and save the script file. Then it can be executed in the IPython or Jupyter cell.

 Furthermore, to use such code as Jupyter notebook I recommend to post-process the   generated Python script with [p2j (Python to Jupyter)](https://pypi.org/project/p2j/) utility.

 Here is an
[Example](https://github.com/vvkisil/MoebInv-notebooks/blob/master/Introduction/Nine_point_auto_script.ipynb) or its [👁 HTML view](http://www1.maths.leeds.ac.uk/~kisilv/MoebInv-notebooks/Introduction/Nine_point_auto_script.html) of a Python script and Jupyter notebook automatically created from the GUI.

<a id="references"></a>
### References

<a id="[1]"></a>
1. Vladimir V. Kisil, *Fillmore–Springer–Cnops Construction Implemented in GiNaC*, Advances in Applied Clifford Algebras, **17**(2007), no. 1, pp. 59–70, [on-line](http://dx.doi.org/10.1007/s00006-006-0017-4) [arXiv:cs.MS/0512073](http://arxiv.org/abs/cs.MS/0512073).

<a id="[2]"></a>
2. Vladimir V. Kisil. *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of SL(2, **R**)*. [Imperial College Press](https://www.worldscientific.com/worldscibooks/10.1142/p835), London, 2012. Includes a live DVD.

<a id="[3]"></a>
3. Vladimir V. Kisil, *An Extension of Mobius–Lie Geometry With Conformal Ensembles of Cycles and Its Implementation in a GiNaC Library*, Proc. Int. Geom. Cent., **11**(2018), n.3, pp.45–67, [on-line](https://doi.org/10.15673/tmgc.v11i3.1203) [arXiv:1512.02960](http://arxiv.org/abs/1512.02960)

<a id="[4]"></a>
4. Vladimir V. Kisil, *MoebInv: C++ Libraries for Manipulations in Non-Euclidean Geometry*, SoftwareX, **11**(2020), [100385](https://doi.org/10.1016/j.softx.2019.100385). arXiv:[1912.03489](https://arxiv.org/abs/1912.03489).
