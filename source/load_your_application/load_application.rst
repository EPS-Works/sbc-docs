.. |br| raw:: html

     <br>

Load your application
=====================

There are two ways to load your application to the SBC:

	1. Run it directly from your :ref:`preferred IDE or terminal <ide>`. |br|
	This option is perfect during the development of your code since it will allow you to iterate fast during the coding process. |br|
	If you use this option, when you reset the power of your SBC, your application will not run since it is not stored in the non volatile memory.
	
	2. Rename your application *.py* file as **main.py** and drag and drop it to the SBC memory which is accessible with the Windows explorer as an external drive. |br|
	After rebooting your SBC, your application will run automatically. |br|
	This method is great to deploy your application.
	
	3. Compile your *.py* file and name it **main.mpy**, drag and drop it to the SBC memory which is accessible with the Windows explorer as an external drive. |br|
	After rebooting your SBC, your application will run automatically. |br|
	This method is great to deploy your application while hiding its content to the final customer to prevent any modifications. |br|
	Instructions on how to generate compiled *mpy* files can be found `here <https://www.ardusimple.com/distribute-mpy-precompiled-files/>`_.
	
	.. admonition:: Important
		:class: attention
	  
		By using methods **2** or **3** you can lock temporaly the SBC (e.g.: if you use a watchdog without feeding it, the SBC will reset continuously). |br|
		If this happens, try to:
		
			* If you are using the microSD memory, remove the microSD card and delete/rename the main.py/mpy file on it by inserting the card directly to your computer.
			* If you are using the SBC internal memory, reset the SBC and remove/rename the main.py/mpy as soon as the SBC memory is available.
			* Sometimes the SBC resets too fast and it is not possible to remove/rename the main.py/mpy. If this is your case you will need to return the SBC to its default setting by :ref:`loading the firmware <fw>` again.
			
			