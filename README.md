# Modern exercises for programming tutorials

This project is about modern exercises or examples for programming tutorials. This exercises/examples have a graphical user interface instead of the usual textual interface, which are less and less used, or even known, by those who are mainly using smartphones.

Simply retrieve the repository (`git clone https://github.com/epeios-q37/basic-exercises`, or get the corresponding *ZIP* file here: <https://q37.info/s/js7fm3vj>), go, in a console, to the root directory, then launch `python main.py` (you can change the language of the exercises by modifying `main.py`). You can also specifically launch an exercise with `python (en|fr)/(A|B|C|Z_(1|2(a|b)|3)).py` (for example: `python fr/B.py`). You can use `python3` instead of `python`.

Alternatively, you can also clone this repository on [*Repl.it*](https://q37.info/s/srnnb7hj), so you have nothing to install on your computer. Click on the `+ new repl` button, select *Python* as language, and put the address of this repository in the dedicated field.

The files found under the `en` and `fr` root directories are examples of what the students have to figure out.

The *A*, *B* and *C* exercises are variations of the famous [*Hello, World!*](https://q37.info/s/k9hfpjbq) program, and are intended to familiarize the student with strings, string concatenation, function calling and definition… Exercise *C* is interactive.

[!['Hello world' as exercise with the Atlas toolkit](https://q37.info/s/tmzd3rzv.png)](https://q37.info/s/xnmx7xqz)

The *Z* series of exercises deals with more advanced programming concepts.

The *Z_1* exercise deals with the solving of first-degree (in)equations. The student has to find out how to calculate the solutions of such an (in)equation, and can test if its code works properly through a convenient user interface, without having to program this interface.

[![First degrees (in)equation resolution as exercise with the Atlas toolkit](https://q37.info/s/3tmm4gmh.png)](https://q37.info/s/zkpdft9p)

The *Z_2a* and *Z_2b* exercises are example of use of the [turtle graphics](https://q37.info/s/3dwhcdfm) API. Exercise *Z_2b* is interactive.

[![Using the tortoise library as exercise with the Atlas toolkit](https://q37.info/s/34xmsbfb.png)](https://q37.info/s/3r4rn3fs)

The purpose of the *Z_3* exercise is to program the [hangman game](https://q37.info/s/gtdtk4hp). As for the other exercises, the student handles the user interface by using very simple functions and can therefore focus on the handling of the inputs from the user.

[![Using the tortoise library as exercise with the Atlas toolkit](https://q37.info/s/pnmjfw39)](https://q37.info/s/bftcf7wd)

*NOTA*: click on the above pictures to see the source code of the corresponding exercise.

The `workshop/assets` directory contains files used for the exercises. The `ab` sub-directory is for exercises *A* and *B*, the `c`, `z_1`, `z_2a`… respectively for the exercises *C*, *Z_1*, *Z_2a*… The content of the `Body.html` files will be put in the *body* section of the HTML main page, and the content of the `Head.html` files will be put in the *head* section of the same page. CSS rules are usually put in the latter file.

For the displaying, here are the currently available functions:

English | Français
-|-
`erase` | `efface`
`display` | `affiche`
`eraseAndDisplay` | `effaceEtAffiche`
`warn` | `alerte`
`ask` | `demande`

For the turtle graphics, here are the currently available functions:

English | Français
-|-
`up`| `hausse`
`down`| `baisse`
`forward` | `avance`
`turnRight` | `tourneDroite`
`turnLeft` | `tourneGauche`
`setColorRGB` | `fixeCouleurRVB`
`setColorHSL` | `fixeCouleurTSL`

To see other examples of exercises, go to <https://q37.info/s/cbms43s9>.

This project is based on the [*Atlas* toolkit](https://atlastk.org). Other projects using this toolkit can be found here: <https://q37.info/s/sssznrb4>.
