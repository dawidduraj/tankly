# Tankly

[Tankly](https://tanklyapp.herokuapp.com) is a online service for comparing German gas station prices made with Flask.
[Live Preview](https://tanklyapp.herokuapp.com)

## Usage

- Pressing on the "Tankly" Logo takes you back to the homepage.
- Enter any address (in Germany) into the input field and select fuel type, radius and sorting option then press the search icon and if the inputs were valid the results will be displayed in a table under the form.
- To search again just change the parameters and press the icon again.

## Features
- The Application automatically geolocates the provided address and formats it into the correct form
- The Application pulls data from the [Tankerkönig API](https://creativecommons.tankerkoenig.de) to search for the stations.
- The Stations get displayed as a sorted table.
- An error message shows up on invalid inputs or other exceptions.

## Issues
- The Tankerkönig API key is publicly exposed, which is a serious security issue. I am not hiding it since this application is only for demonstration purposes.
- Due to the API being unoffical and clumsy, some names/addresses are not being displayed correctly. To solve this the [MTS-K API](https://www.bundeskartellamt.de/DE/Wirtschaftsbereiche/Mineralöl/MTS-Kraftstoffe/mtskraftstoffe_node.html) could be used, but it is not availible to the public.
