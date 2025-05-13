 .. |br| raw:: html

      <br>

.. _ide:

microPython IDEs for SBC
========================
    |                       *if you want to write your own software...*
    
An IDE (Integrated Development Environment) is a software application that facilitates the programming task. |br|
The SBC is compatible with any IDE that supports microPython. |br|
In this section we want to introduce some of the IDEs that our engineers use on a daily basis to program the SBC:

* :ref:`Generic Notepad <notepad>`
* :ref:`Thonny <thonny_ide>` **--> if you don't know where to start, for simplicity and ease of use, we suggest this one**
* :ref:`Terminal <terminal>`
* :ref:`Jupyter <jupyter>`

.. _notepad:

Generic Notepad
---------------

Not much to say here :) |br|
This is the simplest way to edit your code. You can use your preferred Notepad application, although `Notepad++ <https://notepad-plus-plus.org/downloads/>`_ is a nice one since it highlight Python syntaxis.

We use this editor to make quick changes to existing code that does not need much testing.

.. image:: img/notepadpp.png
   :width: 400
   :align: center

.. _thonny_ide:

Thonny
------

`Thonny <https://thonny.org/>`_ is a Python and microPython IDE. |br|
We like it because it is free, multiplatform, light and easy to use.

In this quick tutorial we will only cover the basics, you can find more information on their `website <https://thonny.org/>`_.

1. Connect your SBC to your PC via USB
2. Run Thonny
3. Go to Tools > Options > Interpreter

	Select MicroPython (generic) as interpreter |br|
	Select your SBC Port |br|
	Click OK
	
	.. image:: img/Thonny_cfg.png
	   :width: 400
	   :align: center
   
4. Press the STOP button

	.. image:: img/Thonny_stop.png
	   :width: 400
	   :align: center

5. If everything went ok, you should see a similar message in the shell which indicates that you connected successfully to the SBC microPython terminal.

	.. image:: img/Thonny_welcome.png
	   :width: 400
	   :align: center

6. You can now write your application in the main window and click the Play button to run it. |br|
You will see your application output in the shell (window at the bottom).

Notice that you can also write commands directly in the shell.

	.. image:: img/Thonny_test.png
	   :width: 400
	   :align: center
	   
.. _terminal:

Terminal
--------

You can run or code any Python application directly from a terminal (`Putty <https://www.putty.org/>`_, `Realterm <https://sourceforge.net/projects/realterm/>`_, ...).

We will make a quick tutorial explaining how to connect to your SBC via Putty.

* Configuration 

   Choose Connection type: Serial, desired COMx port and Speed as 115200, click Open. |br|
   If you don't know your SBC COM port, you can use Windows device manager.
   
.. image:: img/putty_config.png
   :width: 400
   :align: center

* Welcome 

   If the connection is succesfull, SBC will show a welcome message and the microPython prompt ">>>"

.. image:: img/putty_welcome.png
   :width: 400
   :align: center

* Write your code

	* REPL

	   REPL means "Read Eval Print Loop" and it is a native feature of python and micropython. |br|
	   Here the user can develop scripts line by line, define functions or examine variables.
	   
	   Just write a line of code and hit enter to execute it.
	   
	.. image:: img/putty_REPL.png
	   :width: 400
	   :align: center

	* Paste mode

	   For more complex scripts, micropython supports paste mode. This mode allows paste longer scritps to the REPL. |br|
	   To enter paste mode, press CRTL+D in a BLANK LINE. Micropython should change promt to "===". |br|
	   Now you can paste your scritps. Remember that Putty uses mouse right click as paste command. |br|
	   Press CTRL-E to exit from the paste mode and execute your script.
   
.. _jupyter:

Jupyter
--------
Before start with jupyter notebooks, you can read the basic guide here: `Notebook Basics <https://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb>`_.

* New notebook

   The first step is to add a new notebook, for that you need to press new notebook button and select Micropython-USB kernel.

.. image:: img/jupyter_new_notebook.png
   :width: 400
   :align: center

* Insert cell

   Cells are small scripts that can be executed in micropython. Press "+" button to add new cells

.. image:: img/jupyter_insert_cell.png
   :width: 400
   :align: center

* Run cell

   To tun cells, select cell and press "RUN" button

.. image:: img/jupyter_run_cell.png
   :width: 400
   :align: center

* Serial connect

   Before executing any sript in micropython, the user should connect to the SBC. 
   To do so, run a cell with %serialconnect command.

.. image:: img/jupyter_run_cell.png
   :width: 400
   :align: center

* Rename

   Click the notebook title to rename it

.. image:: img/jupyter_rename.png
   :width: 400
   :align: center

* Download

   When your script is done, you can save it as a Jupyter notebook (.pynb) or download it as an .html file

.. image:: img/jupyter_download.png
   :width: 400
   :align: center